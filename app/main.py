from fastapi import FastAPI

app = FastAPI()

import polars as pl

df = pl.read_csv('chocobar.csv', sep=',', infer_schema_length=10000)

df1 = df.filter(pl.col('cacao')=='100%')
dic1 = df1.to_dict()

sorted_df = df.sort(by='cacao', descending=True)
df2 = sorted_df.head(10)
dic2 = df2.to_dict()

df3 = df
dic3 = df3.to_dict()

mean_ref = df['ref'].mean()
df4 = df.filter(pl.col('ref')<mean_ref)
df4 = df4.select(pl.col(['company','ref','res']))
dic4 = df4.to_dict()


@app.get('/')
async def index():
    return{'estado','funcionando'}

@app.get('/puro')
async def puro():
    return dic1

@app.get('/top10')
async def top10():
    return dic2

@app.get('/full')
async def full():
    return dic3

@app.get('/ref')
async def ref():
    return dic4
