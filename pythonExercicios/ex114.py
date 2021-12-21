import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[31mO site Pudim está inacessível!\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim!\033[m')
