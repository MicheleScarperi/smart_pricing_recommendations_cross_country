from bs4 import Beautifulsoup as bfs  
from urllib.request import urlopen

url = "https://www.idealo.de/preisvergleich/OffersOfProduct/6461748_-galaxy-s10-plus-samsung.html"
content = urlopen(url).read()
soup = bfs(content)

print (soup.prettify())