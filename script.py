/*import pandas as pd

data = {
  'Nome' : ['Aline', 'Bob', 'Charlie'],
  'Idade': [25, 30, 35],
  'Cidade': ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(data)

print(" ---- DataFrame Pandas --- ")
print(df)
print(" ------------------------- ")
*/
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

