from graph.api.GraphInterface import GraphInterface
from graph.implementation.Edge import Edge
from graph.implementation.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.Nodes = dict()
        self.Edges = dict()
        self.Pokemons = dict()
        self.Agents = dict()
        self.MC = 0

    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return len(self.Edges)

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.Nodes.get(id1).in_

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.Nodes.get(id1).out_

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1, id2) in self.Edges:
            pass
        else:
            if id1 in self.Nodes and id2 in self.Nodes:
                edge = Edge(id1, id2, weight)
                self.Edges[(id1, id2)] = edge
                self.Nodes.get(id1).out_[id2] = weight
                self.Nodes.get(id2).in_[id1] = weight
                if (id1, id2) in self.Edges:
                    self.MC = self.MC + 1
                    return True
                else:
                    return False
            else:
                print("Node not found.")

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.Nodes:
            pass
        else:
            if pos == None:
                self.Nodes[node_id] = Node(node_id, None, None, None)
            else:
                self.Nodes[node_id] = Node(node_id, pos[0], pos[1], pos[2])

            if node_id in self.Nodes:
                self.MC = self.MC + 1
                return True
            else:
                return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.Nodes.keys():
            for destNode in self.Nodes.get(node_id).out_:
                remove = (node_id, destNode)
                del self.Nodes[destNode].getIn()[node_id]
                del self.Edges[remove]
            for srcNode in self.Nodes.get(node_id).in_:
                del self.Nodes[srcNode].getOut()[node_id]
            del self.Nodes[node_id]
            if node_id in self.Nodes:
                return False
            else:
                self.MC = self.MC + 1
                return True
        else:
            pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.Nodes and node_id2 in self.Nodes:
            if (node_id1, node_id2) in self.Edges:
                del self.Edges[(node_id1, node_id2)]
                del self.Nodes.get(node_id1).out_[node_id2]
                del self.Nodes.get(node_id2).in_[node_id1]
                if (node_id1, node_id2) in self.Edges:
                    return False
                else:
                    self.MC = self.MC + 1
                    return True
            else:
                pass
        else:
            pass

    def add_pokemon(self, pokemon):
        self.Pokemons[len(self.Pokemons)] = pokemon
        self.MC = self.MC + 1

    def add_agent(self, agent):
        self.Agents[agent.id] = agent
        self.MC = self.MC + 1

    def __repr__(self):
        return f"Graph: |V|={self.v_size()}, |E|={self.e_size()}"
