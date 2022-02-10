import folium

my_loc = folium.Map(location=[37.503436601037414, 127.049771714636], zoom_start=18)
folium.Marker([37.503436601037414, 127.049771714636], popup=folium.Popup('멀티캠퍼스 선릉', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')