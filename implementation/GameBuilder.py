import json
import math
import os
from graph.implementation.Node import Node
from implementation.Agent import Agent
from api.client import Client
from graph.implementation.GraphAlgo import GraphAlgo


class GameBuilder:

    def __init__(self):
        self.Client = Client()
        self.GraphAlgo = GraphAlgo()

    def create_proportion_mapping(self):
        """
        Used when scaling the nodes.
        Find min and max values of node positions.
        """
        graph_proportions = {}
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        for node in self.GraphAlgo.graph.Nodes.values():
            node_x, node_y = node.getx(), node.gety()
            min_x = min(min_x, node_x)
            min_y = min(min_y, node_y)
            max_x = max(max_x, node_x)
            max_y = max(max_y, node_y)
        graph_proportions["x_proportions"] = (min_x, max_x)
        graph_proportions["y_proportions"] = (min_y, max_y)
        return (max_x, max_y)

    # def call_agent(self):
    # GraphAlgo.load_agents(Client.get_agents())
    def load_all(self):
        self.GraphAlgo.load_graph(self.Client.get_graph())
        self.GraphAlgo.load_agents(self.Client.get_agents())
        self.GraphAlgo.load_pokemons(self.Client.get_pokemons())

    def move_agent(self):
        self.Client.move()
        self.GraphAlgo.load_from_json(self.Client.get_graph())
        self.GraphAlgo.load_agents(self.Client.get_agents())
        self.GraphAlgo.load_pokemons(self.Client.get_pokemons())
        self.match_pokemon_to_agent()
        self.next_dest()

    def next_dest(self):
        for agent in self.GraphAlgo.get_agent().values():
            dest = agent.get_path().pop(0)
            self.Client.choose_next_edge(("{\"agent_id\":" + agent.id + ", \"next_node_id\": " + dest + "}"))

    def get_game_info(self):
        try:
            game_info = json.loads(self.Client.get_info())
            game_info = game_info.get("GameServer", None)
            if game_info is None:
                raise ValueError("Bad JSON")
            self.GraphAlgo.load_from_json(os.path.join("../", game_info.get("graph")))
        except Exception as e:
            print(f"Couldn't load game info: {e}")

    def init_connection(self):
        self.Client.start_connection(os.getenv("HOST"), int(os.getenv("PORT")))

    def start_game(self):
        self.Client.start()

    def get_graph(self):
        try:
            return self.GraphAlgo.get_graph()
        except Exception as e:
            print(f"error.. no graph was loaded from json {e}")

    def get_agents(self):
        return self.GraphAlgo.get_agent()

    def get_pokemon(self):
        return self.GraphAlgo.get_pokemon()

    def is_running(self):
        return self.Client.is_running()

    """
    --------------------------------------------------------+
    algo:                                                   |
    --------------------------------------------------------+
    """

    def match_pokemon_to_agent(self):
        for pokemon in self.get_pokemon().values():
            min_time = float("inf")
            closest_agent = None
            for agent in self.get_agents().values():
                time = self.time_to_reach_pokemon(agent, pokemon)
                if time < min_time:
                    min_time = time
                    closest_agent = agent
            closest_agent.add_to_pokemon_list(pokemon)

    def time_to_reach_pokemon(self, agent, pokemon):
        pok_list = agent.get_pokemon_list()
        src = agent.get_src()
        dest = agent.get_dest()
        time = 0
        merge_tsp = []
        for pokemon in pok_list:
            edge = self.GraphAlgo.find_edge_for_pokemon(pokemon)
            tsp = self.GraphAlgo.TSP([src, dest, edge.getSrc(), edge.getDest()])
            merge_tsp += tsp
            src = edge.getSrc()
            dest = edge.getDest()
            for i in tsp.__len__() - 1:
                time = time + self.calculate_time_from_node_to_node(tsp[i], tsp[i + 1], agent)
        edge_src = self.GraphAlgo.find_edge_for_pokemon(pok_list[len(pok_list) - 1])
        edge_dest = self.GraphAlgo.find_edge_for_pokemon(pokemon)
        tsp = self.GraphAlgo.TSP([edge_src.getSrc(), edge_src.getDest(), edge_dest.getSrc(), edge_dest.getDest()])
        merge_tsp += tsp
        for i in tsp.__len__() - 1:
            time = time + self.calculate_time_from_node_to_node(tsp[i], tsp[i + 1], agent)
        agent.set_path(merge_tsp)
        return time

    def calculate_time_from_node_to_node(self, src: Node, dest: Node, agent: Agent):
        # distance/speed = time  --> distance = ((x1-x2)^2 + (y1-y2)^2) ^ 0.5
        distance = math.sqrt(math.pow((src.getx() - dest.getx()), 2) + math.pow((src.gety() - dest.gety()), 2))
        speed = agent.speed
        time = distance / speed
        return time
