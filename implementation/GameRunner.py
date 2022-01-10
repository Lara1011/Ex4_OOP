import math

from graph.implementation.GraphAlgo import GraphAlgo
from implementation.GameBuilder import GameBuilder
import pygame
from pygame import display
from UI.GameUI import GameUI

from graph.implementation.DiGraph import DiGraph

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


def main():
    game_builder = GameBuilder()
    game_builder.Client.start_connection(HOST, PORT)
    GameBuilder.get_game_info()
    graph = game_builder.get_graph()
    game_UI = GameUI(graph)
    screen = game_UI.SCREEN

    game_ui = GameUI.main_menu()
    client = game_builder.Client
    game_builder.start_game()

    game_info = ""
    while game_builder.Client.is_running() == 'true':
        game_builder.load_all()
        game_UI.main_menu()
        game_builder.move_agent()
        game_info = game_builder.Client.get_info()
        game_builder.get_game_info()
    print(game_info)


if __name__ == '__main__':
    main()
