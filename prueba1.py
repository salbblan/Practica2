import pandas as pd
from plotnine import *

df = pd.read_csv("distribucion-renta-canarias.csv")

df = df.rename(columns={
    "TIME_PERIOD#es": "anio",
    "TERRITORIO#es": "territorio",
    "MEDIDAS#es": "medida",
    "OBS_VALUE": "valor"
})


df["anio"] = df["anio"].astype(int)
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

df = df[df["anio"] == 2022]

p =(
    ggplot(df, aes(
        x="medida",
        y="valor"
    ))
     + geom_col()
    + theme_minimal()
    + labs(
        title="Distribución de renta en Canarias",
        subtitle="Año 2022",
        x="Tramo de renta",
        y="Valor",
        caption="Fuente: Instituto de Estadistica de Canarias"
    )
)

import os
os.makedirs("outputs", exist_ok=True)

p.save("outputs/grafico_renta.png", dpi=150, width=12, height=6)
print("Gráfico guardado en outputs/grafico_renta.png")

print(p)