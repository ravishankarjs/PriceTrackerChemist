import requests
from bs4 import BeautifulSoup

URL = "https://www.chemistwarehouse.com.au/buy/109716/panadol-rapid-500mg-20-tablets"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    price_element = soup.find("span", class_="Price")  # Adjust selector if needed
    if price_element:
        price = price_element.text.strip().replace("$", "")
        return float(price)
    return None

price = get_price()
if price:
    print(f"Current Price: ${price}")
    with open("price_history.txt", "a") as file:
        file.write(f"Price: ${price}\n")
else:
    print("Failed to retrieve price.")