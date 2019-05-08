import folium

##### Other tiles:
# "OpenStreetMap”
# “Mapbox Bright” (Limited levels of zoom for free tiles)
# “Mapbox Control Room” (Limited levels of zoom for free tiles)
# “Stamen” (Terrain, Toner, and Watercolor)
# “Cloudmade” (Must pass API key)
# “Mapbox” (Must pass API key)
# “CartoDB” (positron and dark_matter)

m =folium.Map(location=[0,0], width='100%',height='100%',left='0%', top='0%', position='relative', tiles='Mapbox Control Room', max_zoom=18, min_zoom=0, zoom_start=2, world_copy_jump=False, detect_retina=True, prefer_canvas=False, png_enabled=False, zoom_control=True)

m.save('folium_map.html')
