from graph.implementation.DiGraph import DiGraph
from graph.implementation.Edge import Edge
from graph.implementation.Node import Node


class Agent:
    def __init__(self, id, value, src, dest, speed, pos):
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos
        self.pokemon_list = []
        self.path_list = []
        self.curr_edge = None
        self.curr_node = None
        self.next_node = None
        self.curr_pokemon = None
        self.curr_agent = None

    def get_id(self):
        return self.id

    def set_id(self, i):
        self.id = i

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def get_src(self):
        return self.src

    def set_src(self, s):
        self.src = s

    def get_dest(self):
        return self.dest

    def set_dest(self, d):
        self.dest = d

    def get_speed(self):
        return self.speed

    def set_speed(self, s):
        self.speed = s

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p

    def get_pokemon_list(self) -> list:
        return self.pokemon_list

    def add_to_pokemon_list(self, pokemon):
        self.pokemon_list.append(pokemon)

    def get_path(self) -> list:
        return self.path_list

    def set_path(self, tsp):
        self.path_list = tsp

    def get_curr_edge(self) -> Edge:
        return self.curr_edge

    def get_curr_node(self) -> Node:
        return self.curr_node

    def set_curr_node(self, graph: DiGraph, src: int):
        self.curr_node = graph.Nodes.get(src)

    def get_next_node(self) -> Node:
        return self.next_node

    def set_next_node(self, graph: DiGraph, dest: int) -> bool:
        self.curr_edge = graph.all_out_edges_of_node(self.curr_node)[dest]
        if self.curr_edge is not None:
            return True
        return False

    def get_curr_pokemon(self) -> int:
        return self.curr_pokemon

    def set_curr_pokemon(self, pokemon_id: int):
        self.curr_pokemon = pokemon_id

    def __repr__(self):
        return "Agent{", "id=", self.id, ",value=", self.value, ",src=", self.src, ",dest=", self.dest, ",speed=", self.speed, ",pos=", self.pos, '}'
