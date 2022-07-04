def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    # Importar el archivo de precios diarios
    # Se crea y Guarda el grafico en formato PNG

    >>> make_daily_prices_plot()

    """

    import pandas as pd
    import os
    from matplotlib.pyplot import grid, title

    os.chdir("../")

    prices_df = pd.read_csv("data_lake/business/precios-diarios.csv")

    figura = prices_df.plot(
        kind="line",
        x="Fecha",
        y="Precio",
        title="Precio Promedio Histórico Diario",
        grid=True,
        figsize=(10, 5),
    ).get_figure()

    figura.savefig("data_lake/business/reports/figures/daily_prices.png")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
