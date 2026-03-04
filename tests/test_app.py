from src.my_transformer.app import main


def test_main_returns_zero() -> None:
    assert main() == 0
