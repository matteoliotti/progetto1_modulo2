import pandas as pd
import numpy as np

# parte 1

dati={
    "data":["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05",
            "2026-01-06","2026-01-07","2026-01-08","2026-01-09","2026-01-10"],
    "prodotto":["alimentari","giocattoli","alimentari","occhiali","giocattoli",
                "alimentari","occhiali","giocattoli","alimentari","occhiali"],
    "vendite":[10,20,15,30,np.nan,18,22,28,"dodici",35],
    "prezzo":[10.0,20.0,"dieci",30.0,20.0,10.0,30.0,20.0,10.0,30.0]
}

df=pd.DataFrame(dati)

df.loc[10]=["2026-01-01","alimentari",10,10.0]          # aggiunta di duplicati
df.loc[11]=["2026-01-03","alimentari",15,"dieci"]
df.loc[12]=["2026-01-5","giocattoli",np.nan,20.0]

print("Prime righe del dataset:")
print(df.head())
print("\nStruttura del dataset:")
print(df.info())
print("\nStatistiche descrittive del dataset:")
print(df.describe())