import pygame
from go_engine.GAME import Game
from go_engine.STONE import Stone
pygame.init()
screen_mode = "menu"
button_9 = pygame.Rect(180, 140, 140, 50)
button_13 = pygame.Rect(180, 210, 140, 50)
button_19 = pygame.Rect(180, 280, 140, 50)
SIZE = None
CELL_SIZE = None
MARGIN = None
BOARD_WIDTH = None
g1 = None
pass_count = 0
WIDTH = 500
HEIGHT = 500
screen_mode = "menu"
pass_button = None
resign_button = None

def draw_menu():
    screen.fill((224, 180, 110))

    font_title = pygame.font.SysFont(None, 42)
    font_button = pygame.font.SysFont(None, 32)

    title = font_title.render("Choose board size", True, (0, 0, 0))
    screen.blit(title, (110, 70))

    pygame.draw.rect(screen, (230, 230, 230), button_9)
    pygame.draw.rect(screen, (230, 230, 230), button_13)
    pygame.draw.rect(screen, (230, 230, 230), button_19)

    pygame.draw.rect(screen, (0, 0, 0), button_9, 2)
    pygame.draw.rect(screen, (0, 0, 0), button_13, 2)
    pygame.draw.rect(screen, (0, 0, 0), button_19, 2)

    text_9 = font_button.render("9 x 9", True, (0, 0, 0))
    text_13 = font_button.render("13 x 13", True, (0, 0, 0))
    text_19 = font_button.render("19 x 19", True, (0, 0, 0))

    screen.blit(text_9, (button_9.x + 38, button_9.y + 13))
    screen.blit(text_13, (button_13.x + 32, button_13.y + 13))
    screen.blit(text_19, (button_19.x + 32, button_19.y + 13))

def start_game(selected_size):
    global SIZE, CELL_SIZE, MARGIN, BOARD_WIDTH, WIDTH, HEIGHT
    global screen, g1, pass_count, screen_mode
    global pass_button, resign_button

    SIZE = selected_size

    if SIZE == 9:
        CELL_SIZE = 50
    elif SIZE == 13:
        CELL_SIZE = 35
    else:
        CELL_SIZE = 25

    MARGIN = 50

    BOARD_WIDTH = MARGIN * 2 + CELL_SIZE * (SIZE - 1)
    WIDTH = BOARD_WIDTH + 160
    HEIGHT = BOARD_WIDTH

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pass_button = pygame.Rect(BOARD_WIDTH + 30, 120, 100, 40)
    resign_button = pygame.Rect(BOARD_WIDTH + 30, 180, 100, 40)

    g1 = Game(SIZE, Stone.BLACK.value)
    pass_count = 0
    screen_mode = "game"

def draw_buttons():
    pygame.draw.rect(screen, (200, 200, 200), pass_button)
    pygame.draw.rect(screen, (200, 200, 200), resign_button)

    pygame.draw.rect(screen, (0, 0, 0), pass_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), resign_button, 2)

    font = pygame.font.SysFont(None, 28)

    pass_text = font.render("PASS", True, (0, 0, 0))
    resign_text = font.render("RESIGN", True, (0, 0, 0))

    screen.blit(pass_text, (pass_button.x + 22, pass_button.y + 10))
    screen.blit(resign_text, (resign_button.x + 10, resign_button.y + 10))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Go Game")

running = True

def draw_board():
    screen.fill((224, 180, 110))

    for i in range(SIZE):
        y = MARGIN + i * CELL_SIZE
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (MARGIN, y),
            (MARGIN + CELL_SIZE * (SIZE - 1), y),
            2
        )

        x = MARGIN + i * CELL_SIZE
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (x, MARGIN),
            (x, MARGIN + CELL_SIZE * (SIZE - 1)),
            2
        )
def draw_stones():
    for row in range(SIZE):
        for column in range(SIZE):
            stone = g1.board.board[row][column]

            if stone == Stone.BLACK.value:
                color = (0, 0, 0)
            elif stone == Stone.WHITE.value:
                color = (255, 255, 255)
            else:
                continue

            x = MARGIN + column * CELL_SIZE
            y = MARGIN + row * CELL_SIZE

            stone_radius = CELL_SIZE // 2 - 3

            pygame.draw.circle(screen, color, (x, y), stone_radius)
            pygame.draw.circle(screen, (0, 0, 0), (x, y), stone_radius, 1)


def draw_current_turn():
    font = pygame.font.SysFont(None, 30)

    text = "Turn:"
    turn_text = font.render(text, True, (0, 0, 0))
    screen.blit(turn_text, (BOARD_WIDTH + 35, 60))

    if g1.current_player == Stone.BLACK.value:
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)

    pygame.draw.circle(screen, color, (BOARD_WIDTH + 105, 72), 12)
    pygame.draw.circle(screen, (0, 0, 0), (BOARD_WIDTH + 105, 72), 12, 1)


result_message = ""
black_score = 0
white_score = 0
game_end_reason = ""

def end_game(message, reason):
    global screen_mode, result_message, black_score, white_score, game_end_reason

    result_message = message
    game_end_reason = reason

    black_score, white_score = g1.total_score()

    screen_mode = "result"

def draw_result():
    screen.fill((224, 180, 110))

    title_font = pygame.font.SysFont(None, 48)
    normal_font = pygame.font.SysFont(None, 32)

    title = title_font.render("Game Over", True, (0, 0, 0))
    message = normal_font.render(result_message, True, (0, 0, 0))

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, 190))


    black_text = normal_font.render(f"Black score: {black_score}", True, (0, 0, 0))
    white_text = normal_font.render(f"White score: {white_score}", True, (0, 0, 0))

    screen.blit(black_text, (WIDTH // 2 - black_text.get_width() // 2, 240))
    screen.blit(white_text, (WIDTH // 2 - white_text.get_width() // 2, 280))
    if black_score > white_score:
        winner = "Black wins!"
    elif white_score > black_score:
        winner = "White wins!"
    else:
        winner = "Draw!"

    winner_text = normal_font.render(winner, True, (0, 0, 0))
    screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, 330))



pass_count = 0            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if screen_mode == "menu":
                if button_9.collidepoint(mouse_x, mouse_y):
                    start_game(9)

                elif button_13.collidepoint(mouse_x, mouse_y):
                    start_game(13)

                elif button_19.collidepoint(mouse_x, mouse_y):
                    start_game(19)

                continue
            if screen_mode == "game":
    # xử lý pass button
    # xử lý resign button
    # xử lý click bàn cờ
                if pass_button.collidepoint(mouse_x, mouse_y):
                    pass_count += 1

                    if pass_count >= 2:
                        end_game("Both players passed","resign")
                       
                    else:
                        g1.pass_turn()

                    continue

                if resign_button.collidepoint(mouse_x, mouse_y):
                    if g1.current_player == Stone.BLACK.value:
                        end_game("Black resigned. White wins!","resign")
                    else:
                        end_game("White resigned. Black wins!","resign")

                    continue

            column = round((mouse_x - MARGIN) / CELL_SIZE)
            row = round((mouse_y - MARGIN) / CELL_SIZE)

            if 0 <= row < SIZE and 0 <= column < SIZE:
                g1.play(row, column)
                pass_count = 0
            else:
                print("Ngoài bàn cờ")

    if screen_mode == "menu":
        draw_menu()

    elif screen_mode == "game":
        draw_board()
        draw_stones()
        draw_buttons()
        draw_current_turn()

    elif screen_mode == "result":
        draw_result()
    pygame.display.flip()

pygame.quit()