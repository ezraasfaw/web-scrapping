import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# region Get the web page.
url1 = r'https://www.gasbuddy.com/gasprices/quebec/montreal'

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

web_request1 = requests.get(url1, headers=hdr)


if web_request1.status_code or web_request2.status_code or web_request3.status_code or web_request4 == 200:
    print('Accessed web page!')
else:
    print('Web page access forbidden!')

HTML1 = web_request1.text

# endregion

# region Reading the web page: parsing the HTML.
webPage1 = BeautifulSoup(HTML1, 'html.parser')


pageTitle1 = webPage1.find('h1').text

# endregion

# region Get pricing data.
priceTags1 = webPage1.findAll('span', {'class': 'text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL'})


priceList1 = []


for p in priceTags1:
    priceText1 = p.text.replace('Â', '').replace('¢', '')
    priceList1.append(float(priceText1))

# endregion

# region Store the data into an Excel sheet.
df = pd.DataFrame(priceList1, columns=['Price']) #Convert the LIST of prices to a DataFrame.

df.to_excel('GasPrices-montreal.xlsx', index=False)

# endregion

# region Plot the pricing data.
#plt.plot(priceList, 'rx')
#plt.title(pageTitle)
#plt.show()
# endregion
