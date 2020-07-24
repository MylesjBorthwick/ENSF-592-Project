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


    def add_marker(self, x, y, title):
        tooltip = 'Click for more details'
        folium.Marker([x, y], popup= title,icon=folium.Icon(color='red'), tooltip=tooltip).add_to(self.html_map)


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
            if(y> 0 ):
                y = -1*y
            list.append([x,y])

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
            #
        folium.PolyLine(list,  popup= title, color=colour, weight=2.5, opacity=1).add_to(self.html_map)


    
    def save_map(self):
        self.html_map.save('map.html')
        new = 2 # open in a new tab, if possible
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        url = 'file://'+dir_path +'/map.html'
        # open an HTML file on my own (Windows) computer
        #url = "file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html" #need to add path
        #url = "file://C:/Users/Myles/Documents/Masters/ENSF-592/Traffic Project/Traffic Project 592/ENSF-592-Project/map.html"
        webbrowser.open(url,new=new) #easier to use, but no capture functinality... 

            




    
    


#m.save('map.html')

#in jupyter it will just display these maps and that works...
#for GUI there is no direct method to display this type of map file for tkinter- could turn into html file (needed anyways) and display that (current plan )

#https://python-visualization.github.io/folium/quickstart.html 

#https://stackoverflow.com/questions/46605372/create-a-simple-app-in-tkinter-for-displaying-map

#https://github.com/python-visualization/folium/issues/35 
#https://stackoverflow.com/questions/5633828/convert-html-string-to-an-image-in-python/48537053#48537053 

#TODO: output a map html file with all of the markings. Also need to place the markings on the map. Need to display map within GUI


def browser(self):
    import sys
    import urllib.request
    import os
    import subprocess



    import os
    import time
    from selenium import webdriver

    from time import sleep
    #driver = webdriver.Firefox(executable_path=r'C:\Users\Ken\Anaconda3\geckodriver.exe')
    driver = webdriver.Firefox()
    driver.get('file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html')
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()
    print("end...")



"""
delay=5
fn='testmap.html'
tmpurl='file://Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html'.format(path=os.getcwd(),mapfile=fn)
#m.save(fn)

browser = webdriver.Firefox()
browser.get(tmpurl)
#Give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot('map.png')
browser.quit()
"""


"""
import webbrowser
new = 2 # open in a new tab, if possible
# open an HTML file on my own (Windows) computer
delay=5
url = "file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html"
webbrowser.open(url,new=new) #easier to use, but no capture functinality... 
time.sleep(delay)
"""


#C:\Users\Ken\Desktop\ENSF592\Project\ENSF-592-Project

def best_shot(self):
    outdir = "C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/" # this directory has to exist..
    #map.save("map.html")
    url = "file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html".format(os.getcwd())
    outfn = os.path.join(outdir,"outfig.png")

    url2 = "file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/screenshot.png"
    subprocess.check_call(["cutycapt","--url={}".format(url), "--out={}".format(url2)]) #keeps not finding the file... 

#subprocess.check_call(["cutycapt", url, outfn])

#subprocess.check_call(["cutycapt","--url=file://Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html".format(url), "--out=file://Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/outfig.png".format(outfn)])
"""
from PySide2.QtWidgets import QApplication, QLabel

qt_app = QApplication(sys.argv)
 
# Create a widget
widget = QWidget()
 
# Show it as a standalone widget
widget.show()
 
# Run the application's event loop
qt_app.exec_()

app = QApplication([])
win = QWebView()

win.show()
app.exec_()

"""
# Allow access to command-line arguments
"""
def go():
	text.delete(1.0, END)
	with urllib.request.urlopen(entry.get()) as response:
		received_html = response.read()
	text.insert(1.0, received_html)
   


browser_window = Tk()
browser_window.title('knowpapa browser')
label = Label(browser_window, text= 'Enter URL:')
entry = Entry(browser_window)
entry.insert(END, "http://knowpapa.com")
button = Button(browser_window, text='Go', command = go)
text = Text(browser_window)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
browser_window.mainloop()


from tkinterhtml import HtmlFrame

import tkinter as tk

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
 
frame.set_content(urllib.request.open('file://C:/Users/Ken/Desktop/ENSF592/Project/ENSF-592-Project/map.html').read().decode())

frame.pack()

"""

