from fastapi import FastAPI

app = FastAPI()

@app.get('/puro')
async def puro():
    return{'puro','chocolate con 100% de cacao'}

@app.get('/top10')
async def top10():
    return{'top10','top 10 en rating de chocolates'}

@app.get('/full')
async def full():
    return{'full','lista completa con todos los chocolates'}

@app.get('/ref')
async def ref():
    return{'ref','chocolates con el valor de ref menor al promedio, solo las columnas company,ref,res'}    