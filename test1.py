#API 79X24GDSGXN338JS

#https://www.alphavantage.co/documentation/

#https://github.com/RomelTorres/alpha_vantage

import requests

from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

tipo_funcion ='CRYPTO_INTRADAY'
symbol = ['ETH','BTC', 'XRP', 'BAT']
market = 'USD'
interval = '5min'
apikey = '79X24GDSGXN338JS'


# url = f'https://www.alphavantage.co/query?function={tipo_funcion}&symbol={symbol}&market={market}&interval={interval}&apikey={apikey}'
# get_result = requests.get(url)
# data = get_result.json()
# print(data)


for m in symbol:
    try:
        cc = CryptoCurrencies(key=apikey, output_format='pandas')
        data, meta_data = cc.get_digital_currency_daily(symbol=m, market=market)
        data['4b. close (USD)'].plot()
        plt.tight_layout()
        plt.title(f'Prueba de Pao {m}')
        plt.grid()
        plt.show()

    except:
        print(f'La moneda {m} no existe')
