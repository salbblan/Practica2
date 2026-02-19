import pandas as pd
from plotnine import *

renta = pd.read_csv("distribucion-renta-canarias.csv")

renta = renta.rename(columns={
    "TIME_PERIOD#es": "anio",
    "TERRITORIO#es": "territorio",
    "MEDIDAS#es": "medida",
    "OBS_VALUE": "valor"
})


renta["anio"] = renta["anio"].astype(int)
renta["valor"] = pd.to_numeric(renta["valor"], errors="coerce")


renta = renta[renta["anio"] == 2022]


p =(
    ggplot(renta, aes(
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
        caption="Fuente: Instituto de Estadística de Canarias"
    )
)

import os
os.makedirs("outputs", exist_ok=True)

p.save("outputs/grafico_renta.png", dpi=150, width=12, height=6)
print("Gráfico guardado en outputs/grafico_renta_Canarias.png")

print(p)



codislas =pd.read_csv("codislas.csv", encoding="cp1252", sep=";")

#Normalizamos los datos.

renta["territorio"] = renta["territorio"].str.strip().str.lower()
codislas["isla"] = codislas["ISLA"].str.strip().str.lower()

print("Columnas renta:", list(renta.columns))
print("Columnas codislas:", list(codislas.columns))

renta_enriquecida = renta.merge(
    codislas,
    left_on="territorio",
    right_on="isla",
    how="inner"
)
print("Filas sin unir:",
      renta_enriquecida["isla"].isna().sum())


print(renta_enriquecida)

#renta["cod_mun"] = renta["cod_mun"].astype(str).str.strip()

print("Filas originales:", len(renta))
print("Filas filtradas:", len(renta_enriquecida))



p =(
    ggplot(renta_enriquecida, aes(
        x="medida",
        y="valor",
        fill="territorio"
    ))
     + geom_col(position="dodge")
    + theme_minimal()
    + labs(
        title="Distribución de renta en Canarias por municipios",
        subtitle="Año 2022",
        x="Tramo de renta",
        y="Valor",
        fill ="Isla",
        caption="Fuente: Instituto de Estadística de Canarias"
    )
)


os.makedirs("outputs", exist_ok=True)

p.save("outputs/grafico_renta_CanariasMunicipio.png", dpi=150, width=12, height=6)
print("Gráfico guardado en outputs/grafico_renta_CanariasMunicipio.png")

print(p)
