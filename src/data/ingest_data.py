"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""

from ast import Try
from distutils.log import Log
import logging
from urllib import request


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    # Generación años a descargar desde 1995
    # Total de años a generar

    # Creacion de secuencia a partir de 1995
    # Descarga de archivos desde la página y guardarlos en la carpeta de landing
    # Se recorren los años generados armando la ruta del archivo físico y se procede a descargarlo
    # Se tiene sección de Try Catch en el caso no se puede descargar los archivos XLSX intente con XLS

    # se borra archivo si no se puede descargar por alguna razón y se intenta con XLS y se guarda en la misma carpeta de landing

    >>> ingest_data()

    """

    import urllib.request
    import datetime
    import logging
    from os import remove

    fecha = datetime.datetime.now()

    total_anios = fecha.year - 1995

    anios = list(range(1995, 1995 + total_anios, 1))

    for anio in anios:
        f = open(f"data_lake/landing/{anio}.xlsx", "wb")
        try:
            f.write(
                request.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xlsx"
                ).read()
            )
            f.close()
        except Exception:
            f.close()

            remove(f"data_lake/landing/{anio}.xlsx")

            f = open(f"data_lake/landing/{anio}.xls", "wb")
            f.write(
                request.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xls"
                ).read()
            )
            f.close()
        except:
            logging.exception("Error con el archivo: " & anio)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
