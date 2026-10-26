"""Operações aritméticas simples."""
"""comentarioooooo"""

def soma(a: float, b: float) -> float:
    return a + b


def subtrai(a: float, b: float) -> float:
    return a - b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b


def media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)
