import requests
import pandas as pd
def fetch_cars():
    url="https://myfakeapi.com/api/cars/"
    response = requests.get(url)
    data=response.json()['cars']
    df=pd.DataFrame(data)
    df['price']=df['price'].str.replace('$','').astype(float)
    return df

#Test
from api_loader import fetch_cars
df=fetch_cars()
print(df.head())