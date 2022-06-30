def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    >>> compute_daily_prices()

    """
    import pandas as pd

    # Leer el archivo csv
    data = pd.read_csv("data_lake/cleansed/precios-horarios.csv")

    # Agrupar por fecha
    data = data.groupby("Fecha").mean()

    # Guardar el archivo csv
    data.to_csv("data_lake/business/precios-diarios.csv", index=True)


def test_compute_daily_prices():
    """Comprobar que compute_daily_prices() funciona correctamente."""
    import os

    assert os.path.isfile("data_lake/business/precios-diarios.csv") is True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
