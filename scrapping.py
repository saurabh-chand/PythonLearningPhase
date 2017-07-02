import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("http://cdn.images.express.co.uk/img/dynamic/67/590x/Zlatan-Ibrahimovic-823452.jpg")
