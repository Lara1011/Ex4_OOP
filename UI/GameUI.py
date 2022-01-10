import math
import sys

import pygame
from pygame import gfxdraw
from graph.implementation.GraphAlgo import GraphAlgo
import UI.ButtonsUI
from UI.ButtonsUI import ButtonUI
import time


class GameUI:

    def __init__(self, graph):
        self.graph = graph
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1270, 720))
        pygame.display.set_caption("Menu")

        # self.BACKGROUD_PIC = pygame.image.load(
        #    "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\menuBackGround.png")
        # self.BIG_POKEMON_SURF = pygame.image.load(
        #     "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\pikachuBig.png").convert_alpha()
        # self.SMALL_POKEMON_SURF = pygame.image.load(
        #     "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\pikachu.png").convert_alpha()
        # self.BIG_AGENT_SURF = pygame.image.load(
        #     "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\KantoashBIG.png").convert_alpha()
        # self.SMALL_AGENT_SURF = pygame.image.load(
        #     "C:\\Users\\malak\\PycharmProjects\\Ex4_OOP\\UI\\pics\\Kantoash.png").convert_alpha()

        self.BACKGROUD_PIC = pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/menuBackGround.png")
        self.BIG_POKEMON_SURF = pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/pikachuBig.png")
        self.SMALL_POKEMON_SURF = pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/pikachu.png")
        self.BIG_AGENT_SURF = pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/KantoashBIG.png")
        self.SMALL_AGENT_SURF = pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/Kantoash.png")

        self.CLOCK = pygame.time.Clock()

    def get_font(self, size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/font.ttf", size)

    def play(self):
        t_end = time.time() + 120
        GAME_ACTIVE = True

        if GAME_ACTIVE:
            pygame.display.set_caption("Play")

            while GAME_ACTIVE and t_end > time.time():
                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                self.SCREEN.fill("#003366")
                self.main_display_while_playing(math.ceil(t_end - time.time()))
                self.display_while_playing()


                # SCREEN.blit(BACKGROUD_PIC, (0, 0))

                STOP_BUTTON = ButtonUI(image=None, pos=(100, 680),
                                       text_input="stop", font=self.get_font(30), base_color="red", hovering_color="white")

                STOP_BUTTON.changeColor(PLAY_MOUSE_POS)
                STOP_BUTTON.update(self.SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if STOP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            self.main_menu()
                pygame.display.update()
            self.GAME_FINISHED()

    def GAME_FINISHED(self):
        pygame.display.set_caption("Game Finished!")
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("#d7fcf4")

            GameFinished_TEXT = self.get_font(45).render("Game Finished.", True, "Black")
            GameFinished_RECT = GameFinished_TEXT.get_rect(center=(640, 160))
            self.SCREEN.blit(GameFinished_TEXT, GameFinished_RECT)

            Score_TEXT = self.get_font(45).render("Score:", True, "Black")
            Score_RECT = Score_TEXT.get_rect(center=(640, 290))
            self.SCREEN.blit(Score_TEXT, Score_RECT)

            OPTIONS_BACK = ButtonUI(image=None, pos=(640, 560),
                                    text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        pygame.display.set_caption("Menu")

        while True:

            self.SCREEN.blit(self.BACKGROUD_PIC, (0, 0))
            self.SCREEN.blit(self.BIG_POKEMON_SURF, (750, 200))
            self.SCREEN.blit(self.BIG_AGENT_SURF, (200, 300))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#d7fcf4")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 130))

            PLAY_BUTTON = UI.ButtonsUI.ButtonUI(
                image=pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/Play Rect.png"),
                pos=(640, 350), text_input="PLAY",
                font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            QUIT_BUTTON = UI.ButtonsUI.ButtonUI(
                image=pygame.image.load("/Users/laraabu/PycharmProjects/Ex4_OOP/UI/pics/Quit Rect.png"),
                pos=(640, 550),
                text_input="QUIT",
                font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for ButtonUI in [PLAY_BUTTON, QUIT_BUTTON]:
                ButtonUI.changeColor(MENU_MOUSE_POS)
                ButtonUI.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            self.CLOCK.tick(60)

    def draw_node(self):
        for node in self.graph.Nodes.values():
            x = node.getx()
            y = node.gety()
            gfxdraw.circle(self.SCREEN, int(x), int(y), 15, (13,45,234))
            id_surf = self.get_font(100).render(str(node.id), True, "white")
            id_rect = id_surf.get_rect(center=(x, y))
            self.SCREEN.blit(id_surf, id_rect)
            self.SCREEN.blit(self.BIG_POKEMON_SURF, (0,0))

    def draw_edge(self):
        for edge in self.graph.Edges.values():
            srcX = self.graph.Nodes[edge.getSrc()].getx()
            srcY = self.graph.Nodes[edge.getSrc()].gety()
            destX = self.graph.Nodes[edge.getDest()].getx()
            destY = self.graph.Nodes[edge.getDest()].gety()
            gfxdraw.line(self.SCREEN, int(srcX), int(srcY), int(destX), int(destY), (67,228,11))
#"#d7fcf4"
            weight_surf = self.get_font(100).render(str(edge.getWeight()), True, "white")
            weight_rect = weight_surf.get_rect(center=((srcX + destX) / 2, (srcY + destY) / 2))
            self.SCREEN.blit(weight_surf, weight_rect)

    def draw_pokemon(self):
        for pokemon in self.graph.Pokemons.values():
            x, y, _ = pokemon.pos.split(',')
            self.SCREEN.blit(self.SMALL_POKEMON_SURF, (float(x), float(y)))

    def draw_agent(self):
        for agent in self.graph.Agents.values():
            x, y, _ = agent.pos.split(',')
            self.SCREEN.blit(self.SMALL_AGENT_SURF, (float(x), float(y)))

    def main_display_while_playing(self, Time):
        SCORE_TEXT = self.get_font(18).render("Score: ", True, "red")
        center_h = self.SCREEN.get_height() / 2
        center_w = self.SCREEN.get_width() / 2
        SCORE_RECT = SCORE_TEXT.get_rect(center=(center_w - 500, center_h - 340))
        self.SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        TIME_TEXT = self.get_font(18).render("Time Left: " + str(Time), True, "red")
        TIME_RECT = TIME_TEXT.get_rect(center=(center_w, center_h - 340))
        self.SCREEN.blit(TIME_TEXT, TIME_RECT)

        MOVES_TEXT = self.get_font(18).render("Moves: ", True, "red")
        MOVES_RECT = MOVES_TEXT.get_rect(center=(center_w + 500, center_h - 340))
        self.SCREEN.blit(MOVES_TEXT, MOVES_RECT)

    def display_while_playing(self):
        # display_surf = pygame.Surface((1250, 620))
        # display_surf.fill("black")
        # self.SCREEN.blit(display_surf, (10, 40))
        self.draw_node()
        self.draw_edge()
        self.draw_pokemon()
        self.draw_agent()

    def set_graph(self, Graph):
        self.graph = Graph



