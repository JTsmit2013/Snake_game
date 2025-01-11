import pygame
import random
from pygame.math import Vector2

# Initialize pygame
pygame.init()
title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

# Screen dimensions and colors (Constant variable in UPPERCASE)
GRID_COLOR = (0, 0, 0)  # black
BACKGROUND_COLOR = (144, 238, 144)  # Light Green
SNAKE_COLOR = (0, 0, 0)  # black
FOOD_COLOR = (255, 0, 0)

cell_size = 20
number_of_cells = 15
WIDTH = cell_size * number_of_cells
HEIGHT = cell_size * number_of_cells

OFFSET = 75

# Food class
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_position(snake_body)

    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, FOOD_COLOR, food_rect, 5, 7)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)
    
    def generate_random_position(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position

# Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False

    def draw(self):
        for segment in self.body:
            segment_rect = (OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, SNAKE_COLOR, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body.pop()

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)  # pass snake body when initializing Food
        self.state = "RUNNING"
        self.score = 0
    
    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_position(self.snake.body)  # pass snake body here
            self.snake.add_segment = True
            self.score += 1
    
    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_position(self.snake.body)  # pass snake body here
        self.state = "STOPPED"
        self.score = 0

    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()
        

# Initialize screen
screen = pygame.display.set_mode((2*OFFSET + WIDTH, 2*OFFSET + HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

game = Game()  # Create an instance of the Game class

# Set the timer only once here
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)  # triggering snake update every 200 ms

# Main game loop
run = True
while run:
    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, GRID_COLOR,(OFFSET-5, OFFSET-5, WIDTH+10, HEIGHT+10), 5)
    game.draw()

    title_surface = title_font.render("Snake", True, GRID_COLOR)
    score_surface = score_font.render(str(game.score), True, GRID_COLOR)
    screen.blit(title_surface, (OFFSET-5, 20))
    screen.blit(score_surface, (OFFSET-5, OFFSET + WIDTH + 10 ))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
        
        if event.type == SNAKE_UPDATE:
            game.update()

    # Set frame rate
    pygame.display.update()
    clock.tick(60)  # 60 frames per second for smoother movement
