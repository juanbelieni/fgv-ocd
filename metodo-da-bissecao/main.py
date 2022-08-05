from math import log


def achar_raiz(f: callable, a: float, b: float, epsilon: float) -> float:
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    x = (a + b) / 2

    while abs(b - a) > epsilon:
        if f(a) * f(x) > 0:
            a = x
        else:
            b = x

        x = (a + b) / 2

    return x


if __name__ == "__main__":

    def f1(x: float) -> float:
        return x**3 - x - 1

    def f2(x: float) -> float:
        return log(2 * x - 4)

    raiz1 = achar_raiz(f1, 0, 2, 0.0001)
    raiz2 = achar_raiz(f2, 2.25, 4, 0.0001)

    print(f"Raiz de \"x^3 - x - 1\" em [0, 2] = {raiz1}")
    print(f"Raiz de \"log(2 * x - 4)\" em [2.25, 4] = {raiz2}")
