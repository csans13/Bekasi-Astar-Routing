from config import ORIGIN_POINT, DESTINATION_POINT, GRAPH_PLACE
from graph_utils import load_graph, nearest_node
from astar_solver import solve_astar, route_coordinates
from visualisasi import visualize_route

def main():
    # 1. Load graf jalan
    G = load_graph(GRAPH_PLACE)

    # 2. Mapping titik asal-tujuan ke node graf
    origin_node = nearest_node(G, ORIGIN_POINT)
    destination_node = nearest_node(G, DESTINATION_POINT)
    print(f"Node asal: {origin_node}, node tujuan: {destination_node}")

    # 3. Jalankan algoritma A*
    route = solve_astar(G, origin_node, destination_node)
    print(f"Rute ditemukan: {route}")

    # 4. Ekstrak koordinat untuk visualisasi & print rute
    route_coords = route_coordinates(G, route)
    print(f"Jumlah segmen: {len(route_coords)-1}")
    print("Koordinat asal-tujuan utama:")
    print("Asal:", route_coords[0])
    print("Tujuan:", route_coords[-1])

    # 5. Visualisasi
    visualize_route(route_coords)

if __name__ == '__main__':
    main()