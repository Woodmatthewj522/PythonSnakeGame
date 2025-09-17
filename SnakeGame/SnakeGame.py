#This is a simple Snake game made using Python on VS 2022
#mw09/17/2025

import os
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_gray = (40, 40, 40)
pause_gray = (25, 25, 25)  

# Display size
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Matts OG Snake!')

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
small_font = pygame.font.SysFont("bahnschrift", 18)

# Score function
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    value_rect = value.get_rect(center=(dis_width // 2, 30))
    dis.blit(value, value_rect)

# Snake drawing function
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Message function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

class Leaderboard:
    def __init__(self, filename="leaderboard.txt", max_entries=5):
        self.filename = filename
        self.max_entries = max_entries
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            lines = f.readlines()
        scores = []
        for line in lines:
            line = line.strip()
            if line:
                try:
                    name, score = line.split(",")
                    scores.append((name, int(score)))
                except ValueError:
                    continue
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:self.max_entries]

    def add_score(self, name, score):
        self.scores.append((name, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.scores = self.scores[:self.max_entries]
        self.save_scores()

    def save_scores(self):
        with open(self.filename, "w") as f:
            for name, score in self.scores:
                f.write(f"{name},{score}\n")

    def get_scores(self):
        return self.scores

    def display(self, surface, font, color, x, y):
        # Only show the top 3 scores
        for idx, (name, score) in enumerate(self.scores[:3]):
            text = font.render(f"{idx+1}. {name}: {score}", True, color)
            surface.blit(text, (x, y + idx * 30))

    def clear(self):
        self.scores = []
        self.save_scores()

# Main game loop
def gameLoop():
    game_over = False
    game_close = False
    paused = False

    # Initialize leaderboard
    leaderboard = Leaderboard()

    # Snake starting position
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Movement
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    player_name = ""

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Enter Initials and Press ENTER", red) #NEEDS INPUT PARAMETERS
            Your_score(Length_of_snake - 1)

            # Draw input box for name
            input_box = pygame.Rect(dis_width // 6, dis_height // 2, 200, 32)
            pygame.draw.rect(dis, white, input_box)
            name_surface = font_style.render(player_name, True, black)
            dis.blit(name_surface, (input_box.x + 5, input_box.y + 5))

            # Show leaderboard
            leaderboard.display(dis, font_style, yellow, dis_width // 2, dis_height // 2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name.strip():
                        leaderboard.add_score(player_name.strip(), Length_of_snake - 1)
                        player_name = ""
                        game_close = False
                        gameLoop()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        player_name = ""
                        gameLoop()
                        return
                    else:
                        if len(player_name) < 12 and event.unicode.isprintable():
                            player_name += event.unicode
        
        # Input key assignments
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  
                if not paused:
                    if event.key == pygame.K_a and x1_change == 0:  
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_d and x1_change == 0:  
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_w and y1_change == 0:  
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_s and y1_change == 0:  
                        y1_change = snake_block
                        x1_change = 0

        if paused:
            dis.fill(pause_gray)
            # Center the pause message
            pause_msg = "Paused. Press SPACE to resume."
            mesg_surface = font_style.render(pause_msg, True, yellow)
            mesg_rect = mesg_surface.get_rect(center=(dis_width // 2, dis_height // 4))
            dis.blit(mesg_surface, mesg_rect)

            # Show current score centered at the top
            score_value = score_font.render("Your Score: " + str(Length_of_snake - 1), True, yellow)
            score_rect = score_value.get_rect(center=(dis_width // 2, 30))
            dis.blit(score_value, score_rect)

            # Center the leaderboard title
            leaderboard_title = "Leaderboard"
            title_surface = font_style.render(leaderboard_title, True, yellow)
            title_rect = title_surface.get_rect(center=(dis_width // 2, dis_height // 2 - 80))
            dis.blit(title_surface, title_rect)

            # Center the top 3 leaderboard entries
            scores = leaderboard.get_scores()[:3]
            for idx, (name, score) in enumerate(scores):
                entry_text = f"{idx+1}. {name}: {score}"
                entry_surface = font_style.render(entry_text, True, yellow)
                entry_rect = entry_surface.get_rect(center=(dis_width // 2, dis_height // 2 - 40 + idx * 30))
                dis.blit(entry_surface, entry_rect)

            # Leaderboard Clear Message
            clear_msg = "Press R to clear leaderboard"
            clear_surface = small_font.render(clear_msg, True, yellow)
            clear_rect = clear_surface.get_rect(center=(dis_width // 2, dis_height - 40))
            dis.blit(clear_surface, clear_rect)

            pygame.display.update()
            clock.tick(5)

            # Handles quit, clear, and unpause events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        leaderboard.clear()
                    elif event.key == pygame.K_SPACE:
                        paused = False
            continue

        # Borders
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(dark_gray)

        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Eating food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
