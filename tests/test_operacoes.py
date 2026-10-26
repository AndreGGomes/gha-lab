import pytest

from calc import divide, media, soma, subtrai


def test_soma():
    assert soma(2, 3) == 5


def test_subtrai():
    assert subtrai(10, 4) == 6


def test_divide():
    assert divide(9, 3) == 3


def test_divide_por_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_media():
    assert media([2, 4, 6]) == 4


def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])
