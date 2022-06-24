def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    >>> transform_data()
    """
    import pandas as pd
    import os
    import subprocess
    import sys
    from datetime import datetime
    from os import remove

    # Se instalan los paquetes necesarios para el procesamiento de datos
    # Se hace desde el archivo para no modificar el setup del Autograding en el repositorio de GitHub de la práctica
    subprocess.call(["pip", "install", "openpyxl"])
    subprocess.call(["pip", "install", "xlrd"])

    # Lista de archivos XLS en la capa landing
    archivosLanding = [
        "data_lake/landing/" + f
        for f in os.listdir("data_lake/landing")
        if f.endswith(".xls") or f.endswith(".xlsx")
    ]

    # se recorren los archivos XLS en la capa landing
    for archivo in archivosLanding:
        # Se lee el archivo XLS
        df = pd.read_excel(archivo)

        if df.columns[0] != "Fecha":
            # Se obtiene la fila de la cabecera
            filaInicianDatos = df[df.iloc[:, 0] == "Fecha"].index[0] + 1

            # Se vuelve a leer el archivo XLS saltando las filas de los titulos
            df = pd.read_excel(archivo, skiprows=filaInicianDatos)

            # Se obtiene el nombre del archivo XLS
            nombreArchivo = archivo.split("/")[-1]

            # Se obtiene el nombre del archivo CSV
            nombreArchivoCSV = nombreArchivo.split(".")[0] + ".csv"

            # Se guarda el archivo CSV
            df.to_csv("data_lake/raw/" + nombreArchivoCSV, index=False)
        else:
            # Se obtiene el nombre del archivo XLS
            nombreArchivo = archivo.split("/")[-1]

            # Se obtiene el nombre del archivo CSV
            nombreArchivoCSV = nombreArchivo.split(".")[0] + ".csv"

            # Se guarda el archivo CSV
            df.to_csv("data_lake/raw/" + nombreArchivoCSV, index=False)

    archivosRaw = [
        "data_lake/raw/" + f for f in os.listdir("data_lake/raw") if f.endswith(".csv")
    ]

    # Se recorren los archivos CSV en la capa raw y formatean el campo fecha a formato YYYY-MM-DD
    for archivo in archivosRaw:
        try:
            # Se lee el archivo CSV
            data = pd.read_csv(archivo)

            data.dropna(subset=["Fecha"], inplace=True)

            # Se convierte la columna a fecha
            data["Fecha"] = pd.to_datetime(data["Fecha"])

            # Se formatea la columna de fecha a formato YYYY-MM-DD
            data["Fecha"] = data["Fecha"].apply(lambda x: x.strftime("%Y-%m-%d"))

            # Se obtiene el nombre del archivo CSV
            nombreArchivo = archivo.split("/")[-1]

            # Se eliminan las columnas que no se necesitan en el archivo CSV final
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

            # Se elimina el archivo CSV
            remove(archivo)

            # Se guarda el archivo CSV nuevamente con la columna de fecha en formato YYYY-MM-DD
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
