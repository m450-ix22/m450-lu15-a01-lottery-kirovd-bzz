import pytest
from lottery import create_ticket
from person import Person


def test_create_ticket_success(monkeypatch):
    person = Person(givenname="Max", password="1234", balance=10.0)

    inputs = iter([5, 12, 23, 34, 7, 15, 3])  # Zahlen und Jokerzahl
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    create_ticket(person)

    assert person.balance == 8.0  # 2 CHF wurden abgezogen


def test_create_ticket_insufficient_balance(monkeypatch, capsys):
    person = Person(givenname="Max", password="1234", balance=1.0)

    inputs = iter([5, 12, 23, 34, 7, 15, 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    create_ticket(person)

    captured = capsys.readouterr()
    assert 'Zuwenig Guthaben' in captured.out

