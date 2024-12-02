from numeric_input import read_int, read_float


def test_read_int(monkeypatch):
    inputs = iter([50, 5])  # Erste Eingabe außerhalb des Bereichs, zweite Eingabe gültig
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = read_int("Geben Sie eine Zahl zwischen 1 und 10 ein: ", 1, 10)
    assert result == 5


def test_read_float(monkeypatch):
    inputs = iter(["abc", 20.5])  # Erste Eingabe ist ungültig, zweite gültig
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = read_float("Geben Sie eine Zahl zwischen 10.0 und 30.0 ein: ", 10.0, 30.0)
    assert result == 20.5
