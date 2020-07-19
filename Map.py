import folium

m = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12) #change to calgary
#in jupyter it will just display these maps and that works...
#for GUI there is no direct method to display this type of map file for tkinter- could turn into html file (needed anyways) and display that (current plan )

#https://python-visualization.github.io/folium/quickstart.html 

#https://stackoverflow.com/questions/46605372/create-a-simple-app-in-tkinter-for-displaying-map

#TODO: output a map html file with all of the markings. Also need to place the markings on the map. Need to display map within GUI
