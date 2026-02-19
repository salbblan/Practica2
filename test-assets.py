import pandas as pd
from dagster import asset, AssetExecutionContext

@asset
def poblacion_test() -> pd.DataFrame:
    data = {
        "isla": ["Tenerife", "Gran Canaria", "Lanzarote", "Fuerteventura"],
        "habitantes": [931646, 855521, 156112, 119732],
    }
    return pd.DataFrame(data)

@asset
def total_canarias(context: AssetExecutionContext, poblacion_test: pd.DataFrame) -> int:
    total = int(poblacion_test["habitantes"].sum())
    # Esto sí se ve en Dagster (Metadata del asset)
    context.add_output_metadata({"total_habitantes": total})
    return total
