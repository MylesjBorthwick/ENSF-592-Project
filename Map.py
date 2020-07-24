import folium
import string
import webbrowser
import os 

"""This class contains the functionality to map coordinates using folium into an html file, and load that file. It is called from the GUI window. 
Created by Ken Loughery and Myles Borthwick"""



class Map:

    
    def __init__(self):
        self.html_map = folium.Map(
        location=[51.03,-114.04],
        zoom_start=11) #calgary

    #add a marker with a title from two x and y coordinates 
    def add_marker(self, x, y, title):
        tooltip = 'Click for more details'
        folium.Marker([x, y], popup= title,icon=folium.Icon(color='red'), tooltip=tooltip).add_to(self.html_map)


    #create a line segment from a string of coordinates
    def add_line_coordinates(self, coordinates_string, title, volume):
        coordinates_string = coordinates_string.replace('(', ' ')    
        coordinates_string = coordinates_string.replace('MULTILINESTRING', ' ') 
        coordinates_string = coordinates_string.replace(')', ' ') 
        strippables = string.punctuation + string.whitespace
        coordinates_string = coordinates_string.strip(strippables)
        coordinates = coordinates_string.split(',')
        list = []
        for cord in coordinates:
            cord = cord.strip()
            ordinates = cord.split()
            x = float(ordinates[1].strip())
            y = float(ordinates[0].strip())
            if(y> 0 ): #some coordinates are not negative, and so end up in Russia, quick fix to this
                y = -1*y
            list.append([x,y])

        #colour code the map based on volume
        colour = 'blue'
        if volume > 150000:
            colour = 'red'
        elif volume > 100000:
            colour = 'darkred'
        elif volume > 50000:
            colour = 'lightred'
        elif volume > 25000:
            colour = 'orange'            
        elif volume > 10000:
            colour = 'pink'
        elif volume > 7000:
            colour = 'green'
        else: 
            colour = 'blue'
            #add coordinates to line in the html file
        folium.PolyLine(list,  popup= title, color=colour, weight=2.5, opacity=1).add_to(self.html_map)


    
    def save_map(self):
        self.html_map.save('map.html')
        new = 2 # open in a new tab, if possible

        # open an HTML file on my own (Windows) computer
        dir_path = os.path.dirname(os.path.realpath(__file__))
        url = 'file://'+dir_path +'/map.html'
        webbrowser.open(url,new=new) #easier to use, but no capture functinality... 

            




#https://python-visualization.github.io/folium/quickstart.html 

#https://stackoverflow.com/questions/46605372/create-a-simple-app-in-tkinter-for-displaying-map

#https://github.com/python-visualization/folium/issues/35 
#https://stackoverflow.com/questions/5633828/convert-html-string-to-an-image-in-python/48537053#48537053 
