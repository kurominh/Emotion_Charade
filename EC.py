import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Fonts
FONT_LARGE = pygame.font.Font(None, 74)
FONT_MEDIUM = pygame.font.Font(None, 50)
FONT_SMALL = pygame.font.Font(None, 36)

# Sample list of words/phrases for charades
WORDS = [
    'Happy', 'Sad', 'Angry', 'Sick',
    'Worried', 'Excited', 'Tired', 'Scared', 'Nervous', 'Calm', 'Focused', 'Surprised', 'Bored', 'Confused', 'Disgust', 'Embarrassed', 'Shy'
]

# Initialize game state
current_word = ''
correct_answers = []
incorrect_answers = []
score = 0

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Charades for Kids")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(BLUE)
        draw_text("Emotion Charades", FONT_LARGE, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

        draw_button("Start Game", FONT_MEDIUM, GREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50, game_loop)
        draw_button("Settings", FONT_MEDIUM, YELLOW, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50, settings)
        draw_button("Instructions", FONT_MEDIUM, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, instructions)

        pygame.display.flip()
        check_quit_event()

def draw_button(text, font, color, x, y, action=None):
    text_obj = font.render(text, True, WHITE)
    text_rect = text_obj.get_rect(center=(x, y))
    pygame.draw.rect(screen, color, text_rect.inflate(20, 20))
    screen.blit(text_obj, text_rect)

    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse_pos = pygame.mouse.get_pos()
        if text_rect.inflate(20, 20).collidepoint(mouse_pos):
            pygame.time.delay(300)
            if action:
                action()

def settings():
    while True:
        screen.fill(YELLOW)
        draw_text("Settings", FONT_LARGE, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

        draw_button("Volume: [ + ]", FONT_MEDIUM, GREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, adjust_volume)
        draw_button("Back to Menu", FONT_SMALL, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, main_menu)

        pygame.display.flip()
        check_quit_event()

def adjust_volume():
    pass  # You can add functionality to adjust volume here

def instructions():
    while True:
        screen.fill(RED)
        draw_text("Instructions", FONT_LARGE, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        instructions_text = [
            "1. The game will show a word or phrase.",
            "2. Act out the word without speaking.",
            "3. Click 'Next' if the guess is correct.",
            "4. Click 'Pass' if the guess is incorrect."
        ]
        for i, line in enumerate(instructions_text):
            draw_text(line, FONT_SMALL, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + i * 40)

        draw_button("Back to Menu", FONT_SMALL, YELLOW, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, main_menu)

        pygame.display.flip()
        check_quit_event()

def game_loop():
    global current_word, correct_answers, incorrect_answers, score
    correct_answers = []
    incorrect_answers = []
    score = 0

    while True:
        screen.fill(GREEN)
        if not current_word:
            current_word = random.choice(WORDS)

        draw_text(f"Act out: {current_word}", FONT_LARGE, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        draw_button("Next (Correct)", FONT_MEDIUM, BLUE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, correct_guess)
        draw_button("Pass (Incorrect)", FONT_MEDIUM, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, incorrect_guess)

        pygame.display.flip()
        check_quit_event()

def correct_guess():
    global current_word, score
    correct_answers.append(current_word)
    score += 1
    current_word = ''
    if len(correct_answers) + len(incorrect_answers) >= len(WORDS):
        results_screen()

def incorrect_guess():
    global current_word
    incorrect_answers.append(current_word)
    current_word = ''
    if len(correct_answers) + len(incorrect_answers) >= len(WORDS):
        results_screen()

def results_screen():
    while True:
        screen.fill(BLUE)
        draw_text("Game Over!", FONT_LARGE, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        draw_text(f"Score: {score}", FONT_MEDIUM, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + 50)

        draw_text("Correct Answers:", FONT_SMALL, GREEN, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for i, word in enumerate(correct_answers):
            draw_text(word, FONT_SMALL, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40 + i * 30)

        draw_text("Incorrect Answers:", FONT_SMALL, RED, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)
        for i, word in enumerate(incorrect_answers):
            draw_text(word, FONT_SMALL, WHITE, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 190 + i * 30)

        draw_button("Play Again", FONT_SMALL, GREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 300, game_loop)
        draw_button("Main Menu", FONT_SMALL, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 350, main_menu)

        pygame.display.flip()
        check_quit_event()

def check_quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main_menu()
