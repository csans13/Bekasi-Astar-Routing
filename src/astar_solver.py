import networkx as nx
from graph_utils import heuristic

def solve_astar(G, origin_node, destination_node):
    """
    Jalankan A* dan ambil rute optimal (berupa list node OSM).
    """
    print("Mencari rute optimal A* ...")
    route = nx.astar_path(G, origin_node, destination_node,
                          heuristic=lambda u,v: heuristic(u, v, G),
                          weight='length')
    return route

def route_coordinates(G, route):
    """
    Ubah node rute jadi list koordinat (lat, lon).
    """
    return [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]