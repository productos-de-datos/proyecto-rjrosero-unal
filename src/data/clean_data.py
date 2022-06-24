def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.

    >>> clean_data()

    """
    import pandas as pd
    import os
    import numpy as np

    # Lista de archivos cvs en la capa raw
    archivosRaw = [
        "data_lake/raw/" + f for f in os.listdir("data_lake/raw") if f.endswith(".csv")
    ]

    contenidoCSV = []

    for archivo in archivosRaw:
        data = pd.read_csv(archivo)
        data = data.fillna(method="bfill", axis=1)

        data = pd.melt(
            data,
            id_vars=["Fecha"],
            value_vars=[
                "H00",
                "H01",
                "H02",
                "H03",
                "H04",
                "H05",
                "H06",
                "H07",
                "H08",
                "H09",
                "H10",
                "H11",
                "H12",
                "H13",
                "H14",
                "H15",
                "H16",
                "H17",
                "H18",
                "H19",
                "H20",
                "H21",
                "H22",
                "H23",
            ],
        )
        data.columns = ["Fecha", "Hora", "Precio"]
        data = data.sort_values(by=["Fecha", "Hora"])

        contenidoCSV.append(data)

    contenidoCSVMerged = pd.concat(contenidoCSV, ignore_index=True)
    contenidoCSVMerged.to_csv("data_lake/cleansed/precios-horarios.csv", index=False)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
