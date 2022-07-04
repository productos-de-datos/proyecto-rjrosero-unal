def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    # Se instalan los paquetes necesarios para el procesamiento de datos
    # Se hace desde el archivo para no modificar el setup del Autograding en el repositorio de GitHub de la práctica
    # Lista de archivos XLS en la capa landing
    # se recorren los archivos XLS en la capa landing

    # Se recorren los archivos CSV en la capa raw y formatean el campo fecha a formato YYYY-MM-DD

    >>> transform_data()
    """
    import pandas as pd
    import os
    import subprocess
    import sys
    from datetime import datetime
    from os import remove

    subprocess.call(["pip", "install", "openpyxl"])
    subprocess.call(["pip", "install", "xlrd"])

    archivosLanding = [
        "data_lake/landing/" + f
        for f in os.listdir("data_lake/landing")
        if f.endswith(".xls") or f.endswith(".xlsx")
    ]

    for archivo in archivosLanding:

        df = pd.read_excel(archivo)

        if df.columns[0] != "Fecha":

            filaInicianDatos = df[df.iloc[:, 0] == "Fecha"].index[0] + 1

            df = pd.read_excel(archivo, skiprows=filaInicianDatos)

            nombreArchivo = archivo.split("/")[-1]

            nombreArchivoCSV = nombreArchivo.split(".")[0] + ".csv"

            df.to_csv("data_lake/raw/" + nombreArchivoCSV, index=False)
        else:

            nombreArchivo = archivo.split("/")[-1]

            nombreArchivoCSV = nombreArchivo.split(".")[0] + ".csv"

            df.to_csv("data_lake/raw/" + nombreArchivoCSV, index=False)

    archivosRaw = [
        "data_lake/raw/" + f for f in os.listdir("data_lake/raw") if f.endswith(".csv")
    ]

    for archivo in archivosRaw:
        try:

            data = pd.read_csv(archivo)

            data.dropna(subset=["Fecha"], inplace=True)

            data["Fecha"] = pd.to_datetime(data["Fecha"])

            data["Fecha"] = data["Fecha"].apply(lambda x: x.strftime("%Y-%m-%d"))

            nombreArchivo = archivo.split("/")[-1]

            numeroColumnas = len(data.columns)

            if numeroColumnas > 25:
                columnasABorrar = list(range(25, numeroColumnas))
                data = data.drop(data.columns[columnasABorrar], axis=1)

            data.columns = [
                "Fecha",
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
            ]

            remove(archivo)

            data.to_csv(
                "data_lake/raw/" + nombreArchivo,
                sep=",",
                decimal=".",
                encoding="utf-8",
                index=False,
            )

        except:
            print("Error al transformar el archivo " + archivo)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
