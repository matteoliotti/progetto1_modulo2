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
df.loc[12]=["2026-01-05","giocattoli",np.nan,20.0]

print(df)
print("\nPrime righe del dataset:")
print(df.head())
print("\nStruttura del dataset:")
print(df.info(memory_usage="deep"))
print("\nStatistiche descrittive del dataset:")
print(df.describe())


# parte 2

df["data"]=pd.to_datetime(df["data"])
df["vendite"]=pd.to_numeric(df["vendite"],errors='coerce')
df["vendite"]=df["vendite"].fillna(0)
df["prezzo"]=pd.to_numeric(df["prezzo"],errors='coerce')
df["prezzo"]=df["prezzo"].fillna(df["prezzo"].mean())
df=df.drop_duplicates()

print("\nDataset ripulito:\n")
print(df)

# parte 3

vendite_totali=df.groupby("prodotto")["vendite"].sum().reset_index()
print("\nVendite totali per prodotto:")
print(vendite_totali)

prodotto_piu_venduto=vendite_totali.loc[vendite_totali["vendite"].idxmax()]
prodotto_meno_venduto=vendite_totali.loc[vendite_totali["vendite"].idxmin()]
print("\nProdotto più venduto:")
print(prodotto_piu_venduto)
print("\nProdotto meno venduto:")
print(prodotto_meno_venduto)

vendite_medie_giornaliere=df.groupby("data")["vendite"].mean().reset_index()
print("\nVendite medie giornaliere:")
print(vendite_medie_giornaliere)