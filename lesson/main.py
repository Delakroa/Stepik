from typing import Any, Union


def funct(number: int, value: list) -> int:
    """Стандартная типизация"""
    return number


def funct1(arrage: Any) -> Any:
    """В таком случае arrage принимает любой тип данных и строку, список и тд"""
    return arrage


def funct2(value: Union[str, int]) -> Union[str, int]:
    """В том случае когда нужен определенный тип данных (вернуть или принять)"""
    return value


if __name__ == '__main__':
    print(funct(1, ['hey']))
