def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional

    >>> compute_monthly_prices()

    """
    import pandas as pd

    # Leer el archivo csv
    data = pd.read_csv("data_lake/cleansed/precios-horarios.csv")

    data["Fecha"] = pd.to_datetime(data["Fecha"])

    # Agrupar por año y mes.
    data = data.groupby(pd.Grouper(key="Fecha", axis=1, freq="M")).mean()

    # Guardar el archivo csv
    data.to_csv("data_lake/business/precios-mensuales.csv", index=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
