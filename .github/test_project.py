from src.features.make_features import make_features
from src.data.compute_daily_prices import compute_daily_prices


def test_make_features():
    """Comprobar que make_features() funciona correctamente."""
    import os

    make_features()
    assert os.path.isfile("data_lake/business/features/precios-diarios.csv") is True


def test_compute_daily_prices():
    """Comprobar que compute_daily_prices() funciona correctamente."""
    import os

    compute_daily_prices()
    assert os.path.isfile("data_lake/business/precios-diarios.csv") is True
