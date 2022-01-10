import math
import sys

import pygame
from matplotlib.font_manager import get_font
from pygame import gfxdraw
from graph.implementation.GraphAlgo import GraphAlgo
import UI.ButtonsUI
from UI.ButtonsUI import ButtonUI
import time

pygame.init()
SCREEN = pygame.display.set_mode((1270, 720))
pygame.display.set_caption("Menu")
BACKGROUD_PIC = pygame.image.load("C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\menuBackGround.png")
BIG_POKEMON_SURF = pygame.image.load(
    "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\pikachuBig.png").convert_alpha()
SMALL_POKEMON_SURF = pygame.image.load(
    "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\pikachu.png").convert_alpha()
BIG_AGENT_SURF = pygame.image.load(
    "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\KantoashBIG.png").convert_alpha()
SMALL_AGENT_SURF = pygame.image.load(
    "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\Kantoash.png").convert_alpha()

CLOCK = pygame.time.Clock()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\font.ttf", size)


def play():
    t_end = time.time() + 120
    GAME_ACTIVE = True

    if GAME_ACTIVE:
        pygame.display.set_caption("Play")

        while GAME_ACTIVE and t_end > time.time():
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("#003366")
            display_while_run(math.ceil(t_end - time.time()))

            # SCREEN.blit(BACKGROUD_PIC, (0, 0))

            STOP_BUTTON = ButtonUI(image=None, pos=(100, 680),
                                   text_input="stop", font=get_font(30), base_color="red", hovering_color="white")

            STOP_BUTTON.changeColor(PLAY_MOUSE_POS)
            STOP_BUTTON.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if STOP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
            print(time.time())
            pygame.display.update()
        GAME_FINISHED()


def GAME_FINISHED():
    pygame.display.set_caption("Game Finished!")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#d7fcf4")

        GameFinished_TEXT = get_font(45).render("Game Finished.", True, "Black")
        GameFinished_RECT = GameFinished_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(GameFinished_TEXT, GameFinished_RECT)

        Score_TEXT = get_font(45).render("Score:", True, "Black")
        Score_RECT = Score_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Score_TEXT, Score_RECT)

        OPTIONS_BACK = ButtonUI(image=None, pos=(640, 560),
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:

        SCREEN.blit(BACKGROUD_PIC, (0, 0))
        SCREEN.blit(BIG_POKEMON_SURF, (750, 200))
        SCREEN.blit(BIG_AGENT_SURF, (200, 300))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#d7fcf4")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 130))

        PLAY_BUTTON = UI.ButtonsUI.ButtonUI(
            image=pygame.image.load("C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\Play Rect.png"),
            pos=(640, 350), text_input="PLAY",
            font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = UI.ButtonsUI.ButtonUI(
            image=pygame.image.load("C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\Quit Rect.png"),
            pos=(640, 550),
            text_input="QUIT",
            font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for ButtonUI in [PLAY_BUTTON, QUIT_BUTTON]:
            ButtonUI.changeColor(MENU_MOUSE_POS)
            ButtonUI.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        CLOCK.tick(60)


def draw_node(Graph: GraphAlgo):
    for node in Graph.graph.Nodes.values():
        x = node.getx()
        y = node.gety()
        gfxdraw.circle(SCREEN, x, y, 15, "#d7fcf4")
        id_surf = get_font(100).render(str(node.id), True, "white")
        rect = id_surf.get_rect(center=(x, y))
        SCREEN.blit(id_surf, rect)


def draw_edge(Graph: GraphAlgo):
    for edge in Graph.graph.Edges.values():
        srcX = edge.getSrc().getx()
        srcY = edge.getSrc().gety()
        destX = edge.getDest().getx()
        destY = edge.getDest().gety()
        gfxdraw.line(SCREEN, srcX, srcY, destX, destY, "#d7fcf4")

        weight_surf = get_font(100).render(str(edge.getWeight()), True, "white")
        rect = weight_surf.get_rect(center=((srcX + destX) / 2, (srcY + destY) / 2))
        SCREEN.blit(weight_surf, rect)


def draw_pokemon(Graph: GraphAlgo):
    for pokemon in Graph.get_pokemon().values():
        SCREEN.blit(SMALL_POKEMON_SURF, (pokemon.pos[0], pokemon.pos[1]))


def draw_agent(Graph: GraphAlgo):
    for agent in Graph.get_agent().values():
        SCREEN.blit(SMALL_AGENT_SURF, (agent.pos[0], agent.pos[1]))


def display_while_run(Time):
    SCORE_TEXT = get_font(18).render("Score: ", True, "red")
    center_h = SCREEN.get_height() / 2
    center_w = SCREEN.get_width() / 2
    SCORE_RECT = SCORE_TEXT.get_rect(center=(center_w - 500, center_h - 340))
    SCREEN.blit(SCORE_TEXT, SCORE_RECT)

    TIME_TEXT = get_font(18).render("Time Left: " + str(Time), True, "red")
    TIME_RECT = TIME_TEXT.get_rect(center=(center_w, center_h - 340))
    SCREEN.blit(TIME_TEXT, TIME_RECT)

    MOVES_TEXT = get_font(18).render("Moves: ", True, "red")
    MOVES_RECT = MOVES_TEXT.get_rect(center=(center_w + 500, center_h - 340))
    SCREEN.blit(MOVES_TEXT, MOVES_RECT)


main_menu()
