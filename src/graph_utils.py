import osmnx as ox
from math import radians, cos, sin, asin, sqrt

def load_graph(place, network_type='drive'):
    """
    Download graf jalan OSMnx.
    """
    print(f"Scraping jaringan jalan untuk area: {place} ...")
    return ox.graph_from_place(place, network_type=network_type)

def nearest_node(G, point):
    """
    Cari node terdekat di graf dari (lat, lon)
    """
    lon, lat = point[1], point[0]
    return ox.nearest_nodes(G, lon, lat)

def haversine(coord1, coord2):
    """
    Hitung jarak haversine dalam kilometer.
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def heuristic(u, v, G):
    """
    Fungsi heuristik A*: jarak haversine antar node graf OSMnx (km).
    """
    coord_u = (G.nodes[u]['y'], G.nodes[u]['x'])
    coord_v = (G.nodes[v]['y'], G.nodes[v]['x'])
    return haversine(coord_u, coord_v)