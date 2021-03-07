import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

def findingGPUWord():
    print("hello")

def main():
    url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class":"item-container"})
    findMyBran = "MSI"
    counter = 0

    # We are tying to find Geforce RTX 3080.

    for container in containers:
        brand = container.div.div.a.img["title"]
        print(brand)

        if(findMyBran == brand): 
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()
