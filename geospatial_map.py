import folium

locations = [
    ("Hyderabad", 17.3850, 78.4867, 850000, 420),
    ("Warangal", 17.9784, 79.5941, 320000, 210),
    ("Karimnagar", 18.4386, 79.1288, 280000, 190),
    ("Nizamabad", 18.6725, 78.0941, 220000, 160),
    ("Khammam", 17.2473, 80.1514, 260000, 175),
    ("Vijayawada", 16.5062, 80.6480, 480000, 280),
    ("Visakhapatnam", 17.6868, 83.2185, 620000, 350),
    ("Tirupati", 13.6288, 79.4192, 300000, 200),
    ("Bengaluru", 12.9716, 77.5946, 900000, 500),
    ("Mysuru", 12.2958, 76.6394, 350000, 230),
    ("Mumbai", 19.0760, 72.8777, 950000, 520),
    ("Pune", 18.5204, 73.8567, 720000, 410)
]

m = folium.Map(
    location=[17.5, 78.5],
    zoom_start=6,
    tiles="CartoDB positron"
)

for city, lat, lon, revenue, users in locations:
    folium.CircleMarker(
        location=[lat, lon],
        radius=8,
        popup=f"{city}<br>Revenue: ₹{revenue:,}<br>Users: {users}",
        fill=True
    ).add_to(m)

m.save("geospatial_map.html")

print("Map created successfully!")