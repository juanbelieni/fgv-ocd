def metodo_da_secante(f: callable, x0: float, x1: float, epsilon: float) -> float:
    while True:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        if abs(x2 - x1) < epsilon:
            return x2

        x0 = x1
        x1 = x2


if __name__ == "__main__":
    f = lambda x: x ** 2 + x - 6
    x0 = 1
    x1 = 3
    epsilon = 1e-5

    raiz = metodo_da_secante(f, x0, x1, epsilon)

    print("Raiz de f(x) = x^2 + x - 6: {}".format(raiz))
