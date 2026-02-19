import pandas as pd
from dagster import asset
from plotnine import ggplot,aes, geom_col


@asset

def leer_datos():
    return pd.read_csv("distribucion-renta-canarias.csv")

@asset
def limpiar_datos(leer_datos:pd.DataFrame):
    df = leer_datos.copy()

    df = df.rename(columns={
    "TIME_PERIOD#es": "anio",
    "TERRITORIO#es": "territorio",
    "MEDIDAS#es": "medida",
    "OBS_VALUE": "valor"
    })
    df["anio"] = df["anio"].astype(int)
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    return df

@asset
def mostrar_datos(limpiar_datos:pd.DataFrame):
    df = limpiar_datos
    print (df)

@asset
def leer_codislas():
    return pd.read_csv("codislas.csv")

@asset
def unir_datos(limpiar_datos: pd.DataFrame, leer_codilsas: pd.DataFrame):
    
