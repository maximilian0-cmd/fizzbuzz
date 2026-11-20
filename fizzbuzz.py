def fizzbuzz(num):
    """
    Devuelve el resultado del juego FizzBuzz para un número entero.

    Reglas:
        - Si el número es múltiplo de 3 y de 5, devuelve "fizzbuzz".
        - Si es múltiplo solo de 3, devuelve "fizz".
        - Si es múltiplo solo de 5, devuelve "buzz".
        - En cualquier otro caso, devuelve el número sin modificar.

    Args:
        num (int): Número entero a evaluar.

    Returns:
        str | int: "fizzbuzz", "fizz" o "buzz" según corresponda;
        si no es múltiplo de 3 ni de 5, devuelve el mismo número recibido.

    Examples:
        >>> fizzbuzz(15)
        'fizzbuzz'
        >>> fizzbuzz(9)
        'fizz'
        >>> fizzbuzz(10)
        'buzz'
        >>> fizzbuzz(7)
        7
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num == 0:
        return "fizzbuzz"
    return num