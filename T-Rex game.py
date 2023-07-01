import pygame
import random
from Dino import Dino
from Ground import Ground
from Obstacle import Obstacle
from Stone import Stone

# Initialize pygame
pygame.init()

# Window settings
window_width = 1000
window_height = 500
window = (window_width, window_height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("T-Rex Game")
game_font = pygame.font.Font(None, 50)  # Font for game over text

# Game variables
vel = 15
score = 0
best_score = 0
running = True
alive = True

# Object initializers
dino = Dino(100, 240, 40, 60, 15, False, (255, 0, 0))
obstacle = Obstacle(800, 240, 40, 60)
ground = Ground(screen, 200, vel)

# Collision detection function
def collision(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2)) > 0

# Function to draw the game over screen
def draw_game_over(score, best_score):
    game_over_text = game_font.render(f"Game Over", True, (0, 0, 0))
    score_text = game_font.render(f"Your Score: {score}", True, (0, 0, 0))
    best_score_text = game_font.render(f"Your Best Score: {best_score}", True, (0, 0, 0))
    reset_text = game_font.render(f"Jump to Play Again", True, (250, 150, 0))

    screen.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, 150))
    screen.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2 - score_text.get_height() - 10))
    screen.blit(best_score_text, (window_width // 2 - best_score_text.get_width() // 2, window_height // 2 + 10))
    screen.blit(reset_text, (window_width // 2 - reset_text.get_width() // 2, window_height // 2 + 80))

# Function to draw the score on the screen
def draw_score(score):
    score_text = game_font.render(f"Your Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (40, 20))

# Generate random stones
stones = []
for i in range(10):
    x = random.randint(0, window_width)
    y = random.randint(320,360)
    size = 10
    color = (10,10,10)
    stone = Stone(screen,x, y, size, color, vel)
    stones.append(stone)

# Game loop
clock = pygame.time.Clock()

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_ESCAPE]:
        running = False

    # Toggle rainbow effect when the 'R' key is pressed
    if keys[pygame.K_r]:
        dino.toggle_rainbow()

    # Check for jump input
    if not dino.is_jump:
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            dino.is_jump = True

    # Perform jump action
    if dino.is_jump:
        dino.jump()

    # Apply rainbow effect to the dinosaur
    dino.rainbow()

    # Move the obstacle and update the score
    obstacle.move(vel)
    score += vel / 60
    if score > best_score:
        best_score = int(score)

    # Adjust velocity increment based on score
    if score <= 1000:
        inc_vel = (score / 100) % 100
    elif score > 1000 and score <= 10000:
        inc_vel = (score / 500) % 100

    # Update the velocity based on the increment
    vel = 15 + int(inc_vel)

    # Move and draw stones
    for stone in stones:
        stone.velocity = vel
        stone.move(alive)
        stone.draw()

        # Check if stone is off the screen
        if stone.x < -stone.size:
            # Reset stone position
            stone.x = window_width
            stone.y = random.randint(320, 360)

    # Check for collision between the dinosaur and the obstacle
    if collision(dino.collider()[0], obstacle.collider()[0]) and collision(dino.collider()[1], obstacle.collider()[1]):
        alive = False

    # Draw the game elements on the screen
    screen.fill((220, 220, 220))
    pygame.draw.rect(screen, (0, 150, 150), (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
    ground.draw()
    pygame.draw.rect(screen, dino.color, (dino.x, dino.y, dino.width, dino.height))
    draw_score(int(score))

    # Check if the game is over
    if not alive:
        vel = 0
        dino.jump_height = 0
        draw_game_over(int(score), best_score)
        # Check if the player wants to play again
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            # Reset game variables and objects
            dino.reset()
            obstacle.reset()
            alive = True
            vel = 15
            score = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
