# -*- coding: utf-8 -*-
import pygame
import random
import os


# perset
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([0, 0, 0])
pygame.display.set_caption('2048')
running = True
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
board_temp = []
score = 0


def determine_not_the_end():
    test = 0

    for _ in range(4):
        if 0 in board[_]:
            test = 1

    if not test:
        for i in range(4):
            for j in range(4):
                adjacent = []

                if i-1 >= 0:
                    adjacent.append(board[i-1][j])
                if i+1 <= 3:
                    adjacent.append(board[i+1][j])
                if j-1 >= 0:
                    adjacent.append(board[i][j-1])
                if j+1 <= 3:
                    adjacent.append(board[i][j+1])

                if board[i][j] in adjacent:
                    return True
    else:
        return True


def initial_board():
    global board, score
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    score = 0
    random_generate()
    random_generate()


def plot():
    global board, screen

    if 'record.txt' in os.listdir():
        record_score = open('record.txt', 'r', encoding='utf-8').read()
        text = 'Highest Score: ' + record_score + ' pts'
        my_font = pygame.font.SysFont('arial', 32)
        text_surface = my_font.render(text, True, (255, 255, 0))
        screen.blit(text_surface, (165, 20))

    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                pygame.draw.rect(screen, [255, 255, 255], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 2:
                pygame.draw.rect(screen, [255, 255, 255], [j*40+j, i*40+i, 40, 40])

            elif board[i][j] == 4:
                pygame.draw.rect(screen, [255, 255, 100], [j*40+j, i*40+i, 40, 40])

            elif board[i][j] == 8:
                pygame.draw.rect(screen, [255, 255, 0], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 16:
                pygame.draw.rect(screen, [255, 100, 0], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 32:
                pygame.draw.rect(screen, [255, 0, 0], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 64:
                pygame.draw.rect(screen, [120, 255, 0], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 128:
                pygame.draw.rect(screen, [0, 255, 0], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 256:
                pygame.draw.rect(screen, [0, 255, 100], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 512:
                pygame.draw.rect(screen, [0, 255, 180], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 1024:
                pygame.draw.rect(screen, [0, 255, 255], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 2048:
                pygame.draw.rect(screen, [255, 255, 100], [j*40+j, i*40+i, 40, 40])
            elif board[i][j] == 4096:
                pygame.draw.rect(screen, [255, 0, 100], [j * 40 + j, i * 40 + i, 40, 40])
            elif board[i][j] == 8192:
                pygame.draw.rect(screen, [255, 0, 255], [j * 40 + j, i * 40 + i, 40, 40])
            elif board[i][j] == 16384:
                pygame.draw.rect(screen, [200, 200, 200], [j * 40 + j, i * 40 + i, 40, 40])

            if board[i][j] == 0:
                pass
            elif board[i][j] < 10:
                my_font = pygame.font.SysFont('arial', 32)
                text_surface = my_font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text_surface, (13+j*41, 3+i*41))
            elif board[i][j] >= 10 and board[i][j] < 100:
                my_font = pygame.font.SysFont('arial', 28)
                text_surface = my_font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text_surface, (9+j*41, 4+i*41))
            elif board[i][j] >= 100 and board[i][j] < 1000:
                my_font = pygame.font.SysFont('arial', 23)
                text_surface = my_font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text_surface, (5+j*41, 6+i*41))
            elif board[i][j] >= 1000 and board[i][j] < 10000:
                my_font = pygame.font.SysFont('arial', 18)
                text_surface = my_font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text_surface, (4+j*41, 9+i*41))
            else:
                my_font = pygame.font.SysFont('arial', 16)
                text_surface = my_font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text_surface, (3+j*41, 10+i*41))

        my_font = pygame.font.SysFont('arial', 23)
        text = 'Score: ' + str(score) + ' pts'
        text_surface = my_font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (170, 128))
    pygame.display.flip()
    pygame.display.update()


def random_generate():
    global board

    test = 0

    for _ in range(4):
        if 0 in board[_]:
            test = 1

    while test:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if board[x][y] != 0:
            continue
        else:
            mutation = random.randint(1, 6)
            if mutation == 3:
                board[x][y] = 4
            else:
                board[x][y] = 2
            break


def left_move():
    global board, score, board_temp

    for i in range(4):
        temp = [0, 0, 0]

        for j in range(4):
            if board[i][j] != 0 and temp[2] == 0:
                temp = [i, j, board[i][j]]
            elif board[i][j] != 0 and temp[2] != 0:
                if board[i][j] == temp[2]:
                    board[temp[0]][temp[1]] = temp[2]*2
                    score += temp[2]*2
                    board[i][j] = 0
                    temp = [0, 0, 0]
                else:
                    temp = [i, j, board[i][j]]

    for _ in range(4):
        zero_num = 0
        while True:
            if 0 in board[_]:
                board[_].remove(0)
                zero_num += 1
            else:
                for n in range(zero_num):
                    board[_].append(0)
                break

    board_copy = [board[x][y] for x in range(4) for y in range(4)]
    if board_copy != board_temp:
        random_generate()
    board_temp = [board[x][y] for x in range(4) for y in range(4)]


def right_move():
    global board, score, board_temp

    for i in range(4):
        temp = [0, 0, 0]

        for j in [3, 2, 1, 0]:
            if board[i][j] != 0 and temp[2] == 0:
                temp = [i, j, board[i][j]]
            elif board[i][j] != 0 and temp[2] != 0:
                if board[i][j] == temp[2]:
                    board[temp[0]][temp[1]] = temp[2]*2
                    score += temp[2] * 2
                    board[i][j] = 0
                    temp = [0, 0, 0]
                else:
                    temp = [i, j, board[i][j]]

    for _ in range(4):
        zero_num = 0
        while True:
            if 0 in board[_]:
                board[_].remove(0)
                zero_num += 1
            else:
                board[_].reverse()
                for n in range(zero_num):
                    board[_].append(0)
                break

        board[_].reverse()

    board_copy = [board[x][y] for x in range(4) for y in range(4)]
    if board_copy != board_temp:
        random_generate()
    board_temp = [board[x][y] for x in range(4) for y in range(4)]


def up_move():
    global board, score, board_temp

    for j in range(4):
        temp = [0, 0, 0]

        for i in range(4):
            if board[i][j] != 0 and temp[2] == 0:
                temp = [i, j, board[i][j]]
            elif board[i][j] != 0 and temp[2] != 0:
                if board[i][j] == temp[2]:
                    board[temp[0]][temp[1]] = temp[2]*2
                    score += temp[2] * 2
                    board[i][j] = 0
                    temp = [0, 0, 0]
                else:
                    temp = [i, j, board[i][j]]

    for j in range(4):
        column = []
        for i in range(4):
            column.append(board[i][j])
            zero_num = 0
            while True:
                if 0 in column:
                    column.remove(0)
                    zero_num += 1
                else:
                    for n in range(zero_num):
                        column.append(0)
                    break

        for i in range(4):
            board[i][j] = column[i]

    board_copy = [board[x][y] for x in range(4) for y in range(4)]
    if board_copy != board_temp:
        random_generate()
    board_temp = [board[x][y] for x in range(4) for y in range(4)]


def down_move():
    global board, score, board_temp

    for j in range(4):
        temp = [0, 0, 0]
        for i in [3, 2, 1, 0]:
            if board[i][j] != 0 and temp[2] == 0:
                temp = [i, j, board[i][j]]
            elif board[i][j] != 0 and temp[2] != 0:
                if board[i][j] == temp[2]:
                    board[temp[0]][temp[1]] = temp[2]*2
                    score += temp[2] * 2
                    board[i][j] = 0
                    temp = [0, 0, 0]
                else:
                    temp = [i, j, board[i][j]]

    for j in range(4):
        column = []
        for i in range(4):
            column.append(board[i][j])
            zero_num = 0
            while True:
                if 0 in column:
                    column.remove(0)
                    zero_num += 1
                else:
                    column.reverse()
                    for n in range(zero_num):
                        column.append(0)
                    column.reverse()
                    break

        for i in [3, 2, 1, 0]:
            board[i][j] = column[i]

    board_copy = [board[x][y] for x in range(4) for y in range(4)]
    if board_copy != board_temp:
        random_generate()
    board_temp = [board[x][y] for x in range(4) for y in range(4)]


def record(score):
    if 'record.txt' not in os.listdir():
        open('record.txt', 'w', encoding='utf-8').write(str(score))
    else:
        record_score = open('record.txt', 'r+', encoding='utf-8').read()
        record_score = int(record_score)
        if score > record_score:
            open('record.txt', 'w+', encoding='utf-8').write(str(score))


def run():
    global running, board, board_temp

    while running:
        plot()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                screen.fill([0, 0, 0])

                if event.key == pygame.K_LEFT:
                    left_move()
                elif event.key == pygame.K_RIGHT:
                    right_move()
                elif event.key == pygame.K_DOWN:
                    down_move()
                elif event.key == pygame.K_UP:
                    up_move()
                elif event.key == pygame.K_r:
                    initial_board()

                end = determine_not_the_end()

                if not end:
                    my_font = pygame.font.SysFont('arial', 32)
                    text_surface = my_font.render('GAME OVER! press R to restart', True, (255, 0, 0))
                    screen.blit(text_surface, (165, 70))
                    record(score)

    pygame.quit()


if __name__ == '__main__':
    initial_board()
    run()
