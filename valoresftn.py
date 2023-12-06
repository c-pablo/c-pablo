# -*- coding: utf-8 -*-
"""ValoresFTN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15YF_562O2e1q4zYEcIlW9XslUVSR68hu
"""

pip install scrapy

from scrapy import Selector
import requests

url ='https://finance.yahoo.com/quote/FTNT/'
html = requests.get( url ).content
sel = Selector( text=html )
titulares = sel.xpath('//fin-streamer')
for i in range(len(titulares)):
  if "regularMarketPrice" in titulares[i].attrib["data-field"] and "FTNT" in titulares[i].attrib["data-symbol"]:
    print("El precio de Fortinet es",":",titulares[i].attrib["value"],i)
#titulares[0].extract()

titulares[1].attrib["class"]

titulares2 = titulares[18].xpath('/span')
titulares[18]
#@data-field="regularMarketPrice"] and [@data-symbol="FTNT"]