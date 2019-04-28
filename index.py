import requests
from bs4 import BeautifulSoup
import os

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
ascii = """
  _____                                            _                      
 / ____|                                          | |                     
| |  __  ___  _ __   __ _ _   _ ___  ___ _ __   __| | ___ _ __ __ _ _ __  
| | |_ |/ _ \| '_ \ / _` | | | / __|/ _ \ '_ \ / _` |/ _ \ '__/ _` | '_ \ 
| |__| | (_) | |_) | (_| | |_| \__ \  __/ | | | (_| |  __/ | | (_| | | | |
 \_____|\___/| .__/ \__,_|\__, |___/\___|_| |_|\__,_|\___|_|  \__,_|_| |_|
             | |           __/ |                                          
             |_|          |___/                                By SadCode.org           
"""
print (ascii)
data = input("Masukkkan no hp(62xx): ")
r = requests.post("https://api.ekawijanarka.info/gopay/v1/index.php", data={'no':data})
soup = BeautifulSoup(r.text, 'html.parser')

res = soup.find('p', attrs={'align':'center','class':'pertama'})

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
print(res.text)
