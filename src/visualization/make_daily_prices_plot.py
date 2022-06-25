from matplotlib.pyplot import grid, title


def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    >>> make_daily_prices_plot()

    """

    import pandas as pd
    import os

    # Importar el archivo de precios diarios
    os.chdir("/home/runner/work/proyecto-rjrosero-unal/proyecto-rjrosero-unal/src/data")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(os.getcwd())
    print(os.listdir())
    print(dir_path)
    """
    prices_df = pd.read_csv("data_lake\\business\\precios-diarios.csv")

    # Crear un grafico de lines que representa los precios promedios diarios
    # prices_df.plot(kind="line", x="fecha", y="precio")

    # Guardar el grafico en formato PNG
    figura = prices_df.plot(
        kind="line",
        x="Fecha",
        y="Precio",
        title="Precio Promedio Histórico Diario",
        grid=True,
        figsize=(10, 5),
    ).get_figure()

    figura.savefig("data_lake\\business\\reports\\figures\\daily_prices.png")
"""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
