import folium
import webbrowser
from folium.plugins import MarkerCluster
from newsapi import NewsApiClient
import pandas as pd
import requests


class Map:
    
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    def showMap(self):
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
        my_map.save("map.html")
        webbrowser.open("map.html")
    def retriveNews(self):
        url = ('https://newsapi.org/v2/top-headlines?sources?'
       'apiKey=xxx')
        response = requests.get(url)
        data = response.json()
        for i in data['articles']:
            print(f"{i['title']} and  {i['country']}")
            print()
        

def main():
    coords = [39.2571, -76.861]
    map = Map(center = coords, zoom_start = 13)
    #map.showMap()
    map.retriveNews()
 

if __name__ == "__main__":
    main()