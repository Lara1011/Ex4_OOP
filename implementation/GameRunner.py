import math

from graph.implementation.GraphAlgo import GraphAlgo
from implementation.GameBuilder import GameBuilder
import pygame
from pygame import display
from UI import GameUI

from graph.implementation.DiGraph import DiGraph

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

def main(self):
    game_builder = GameBuilder()
    game_builder.Client.start_connection()
    screen = GameUI.SCREEN
    GameBuilder.get_game_info()
    global global_graph
    global_graph = game_builder.get_graph()

    game_ui = GameUI.main_menu()
    client = game_builder.Client
    game_builder.start_game()

    game_info = ""
    while game_builder.Client.is_running() == 'true':
        GameUI.draw_node(graph)
        GameUI.draw_edge(graph)
        GameUI.draw_agent(graph)
        GameUI.draw_pokemon(graph)
