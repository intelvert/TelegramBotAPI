from bs4 import BeautifulSoup as bs
import requests

url="https://www.olx.pl/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_float_price:to%5D=2200&search%5Bfilter_enum_furniture%5D%5B0%5D=yes&search%5Bfilter_enum_rooms%5D%5B0%5D=one"

def parse(url):
    names=[]
    prices=[]
    result=[]
    s=requests.get(url)
    soup=bs(s.content, 'html.parser')

    tmp=soup.findAll('div', class_="css-u2ayx9")
    for item in tmp:
        names.append(item.find('h6').text)
        prices.append(item.find('p').text)

    for name, price in zip(names, prices):
        result.append('\n'+str(name)+'\n'+"price: "+str(price))
    return result

if __name__=="__main__":
    for item in parse(url):
        print(item)