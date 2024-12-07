import io
import pandas as pd

df = pd.read_csv('https://api.blockchain.info/charts/market-price?format=csv', header=None, names=['date', 'value'])

mindf = df.loc[df['value'] == df['value'].min(), ['date', 'value']]
maxdf = df.loc[df['value'] == df['value'].max(), ['date', 'value']]

df2 = df.__deepcopy__()

df2.set_index('date', inplace=True)
df2.agg(['idxmin', 'idxmax'])

df3 = pd.DataFrame( {
    'consumption': [10.51, 103.11, 55.48],
    'co2_emissions': [37.2, 19.66, 1712] },
    index=['Pork', 'Wheat Products', 'Beef']
)

url = f"http://finance.yahoo.com/quote/%5EGSPC/history/?p=%5EGSPC"
spdf = pd.read_html(io.StringIO(url))

df = pd.read_html('https://en.wikipedia.org/wiki/National_Basketball_Association')

