import pygame
import sys
import random

# Configuración
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

# Colores
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main():
    # Estado inicial
    snake = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
    direction = (CELL_SIZE, 0)  # inicialmente hacia la derecha
    food = (random.randrange(0, WINDOW_WIDTH//CELL_SIZE) * CELL_SIZE,
            random.randrange(0, WINDOW_HEIGHT//CELL_SIZE) * CELL_SIZE)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN:
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT:
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (CELL_SIZE, 0)

        # Mover la serpiente
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        snake.insert(0, new_head)

        # Verificar comida
        if new_head == food:
            score += 1
            food = (random.randrange(0, WINDOW_WIDTH//CELL_SIZE) * CELL_SIZE,
                    random.randrange(0, WINDOW_HEIGHT//CELL_SIZE) * CELL_SIZE)
        else:
            snake.pop()

        # Verificar colisiones con paredes o consigo misma
        if (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT or
            new_head in snake[1:]):
            # Game Over
            draw_text(f"Game Over! Score: {score}", RED, WINDOW_WIDTH//4, WINDOW_HEIGHT//2)
            pygame.display.update()
            pygame.time.wait(2000)
            return  # salir de main o reiniciar

        # Dibujar
        screen.fill(BLACK)
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.update()
        clock.tick(10)  # velocidad

if __name__ == "__main__":
    while True:
        main()
