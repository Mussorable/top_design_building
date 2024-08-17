import folium
from xdg.Config import icon_size


def generate_map(coordinates=None, zoom_start=14):
    if coordinates is None:
        coordinates = [51.215950, 18.573541]

    m = folium.Map(
        location=coordinates,
        zoom_start=zoom_start,
        scrollWheelZoom=False,
        dragging=False,
    )
    folium.Marker(
        location=coordinates,
        icon=folium.Icon(color='blue'),
        popup='<b>Top Design</b>'
              '<br>'
              'Address: osiedle Kopernika 1, 98-300 Wieluń',
    ).add_to(m)

    return m._repr_html_()
