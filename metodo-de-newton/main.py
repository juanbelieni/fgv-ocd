
def metodo_de_newton(f: callable, f_: callable, x0: float, epsilon: float) -> float:
    x = x0

    while abs(f(x)) > epsilon:
        x -= f(x)/f_(x)

    return x

if __name__ == '__main__':
    f = lambda x: x**3 - x - 1
    f_ = lambda x: 3*x**2 - 1
    x0 = 20
    epsilon = 1e-5

    print("Raiz de \"x^3 - x - 1\" próxima a 1:", metodo_de_newton(f, f_, x0, epsilon))
