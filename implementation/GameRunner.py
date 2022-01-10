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
    nc = game_builder.GraphAlgo.centerPoint()
    c_id = nc[0]
    center_text = "{\"id\":" + str(c_id) + "}"
    game_builder.Client.add_agent(center_text)
    game_builder.Client.add_agent(center_text)
    game_builder.Client.add_agent(center_text)
    game_builder.Client.add_agent(center_text)
    game_builder.get_game_info()
    game_builder.load_all()
    graph = game_builder.Client.get_graph()

    print("###")
    print(game_builder.GraphAlgo.graph.Edges.values())
    print(game_builder.GraphAlgo.graph.Nodes.values())
    print(game_builder.GraphAlgo.graph.Pokemons.values())
    print(game_builder.GraphAlgo.graph.Agents.values())
    print("###")
    game_builder.start_game()
    game_builder.load_all()
    graph = game_builder.get_graph()
    client = game_builder.Client
    game_UI = GameUI(graph, client)
    screen = game_UI.SCREEN
    print(graph)

    min_x = min(list(graph.Nodes.values()), key=lambda n: n.x)
    min_y = min(list(graph.Nodes.values()), key=lambda n: n.y)
    max_x = max(list(graph.Nodes.values()), key=lambda n: n.x)
    max_y = max(list(graph.Nodes.values()), key=lambda n: n.y)

    game_info = ""
    while client.is_running() == 'true':
        game_builder.load_all()
        graph = game_builder.get_graph()
        game_UI.set_graph(graph)
        game_builder.create_proportion_mapping()
        game_UI.play()
        game_builder.move_agent()
        game_info = client.get_info()
        game_builder.get_game_info()
        game_UI.draw_node()
        print(game_info)
    game_builder.Client.stop_connection()

if __name__ == '__main__':
    main()
