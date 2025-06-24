import folium
import os
from config import ASAL_NAMA, TUJUAN_NAMA

def visualize_route(route_coords, filename=ASAL_NAMA+" ke "+TUJUAN_NAMA+".html"):
    """
    Plot rute pada peta Folium, simpan sebagai HTML.
    """
    center_lat = sum([lat for lat, lon in route_coords]) / len(route_coords)
    center_lon = sum([lon for lat, lon in route_coords]) / len(route_coords)
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

    # Garis rute
    folium.PolyLine(route_coords, color='blue', weight=5, opacity=0.7).add_to(m)

    # Marker asal dan tujuan
    folium.Marker(route_coords[0], popup='Asal', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(route_coords[-1], popup='Tujuan', icon=folium.Icon(color='red')).add_to(m)

    os.makedirs("test", exist_ok=True)
    m.save(os.path.join("test", filename))
    print(f"Peta rute A* tersimpan di '{filename}'")