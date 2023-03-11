from fastapi import FastAPI

app = FastAPI()

import pandas as pd

df = pd.read_csv('chocobar.csv', sep=',')

df1 = df.query('cacao =="100%"')
dic1 = df1.to_dict()

df2 = df.sort_values(by='porcentaje', ascending=False)
dic2 = df2.to_dict()

df3 = df
dic3 = df3.to_dict()

mean_ref = df['ref'].mean()
df4 = df.query('ref < ' + str(mean_ref))
df4 = df4[['company','ref','res']]
dic4 = df4.to_dict()


@app.get('/')
async def index():
    return{'estado','funcionando'}

@app.get('/puro')
async def puro():
    return{'estado1','funcionando'} 
# dic1


@app.get('/top10')
async def top10():
    return{'estado2','funcionando'} 
# dic2

@app.get('/full')
async def full():
    return{'estado3','funcionando'} 
#dic3

@app.get('/ref')
async def ref():
    return{'estado4','funcionando'} 
# dic4
