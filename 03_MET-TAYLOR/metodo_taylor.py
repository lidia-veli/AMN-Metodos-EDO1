def metodo_taylor_ord1(func, a, b, y0, N):
    """es el metodo de Euler"""

    h = (b-a)/N  # tamaño del paso

    x = [a]  # valores de x
    y = [y0]  # valores de y

    for k in range(N):
        x.append ( x[k] + h )
        y.append( y[k] + h*func(x[k], y[k]) )

    return x, y


def metodo_taylor_ord2(f, f_dx, f_dy, a, b, y0, N):
    """
    Resuelve una EDO de primer orden utilizando el método de Taylor de segundo.

    ARGS:
    - func: La función que define la EDO y'=func(x, y).
    - a: valor inicial de x y extremo inferior del intervalo.
    - b: extremo superior del intervalo de valores de x.
    - y0: valor inicial de y.
    - N: número de pasos.
    """
    
    h = (b-a)/N  # tamaño del paso

    x_values = [a]
    y_values = [y0]

    # Itera hasta alcanzar el punto final
    for k in range(N):
        x_0 = x_values[k]
        y_0 = y_values[k]

        # Calcula las derivadas hasta el orden 2
        f_deriv_1 = f(x_0, y_0)
        f_deriv_2 = f_dx(x_0, y_0) + f_dy(x_0, y_0)*f_deriv_1

        # Usa la expansión de Taylor de orden 2 para obtener la siguiente aproximación
        x_1 = x_0 + h
        y_1 = y_0 + h*f_deriv_1 + ((h**2)/2)*f_deriv_2

        # Agrega los resultados a las listas
        x_values.append(x_1)
        y_values.append(y_1)

    return x_values, y_values




def metodo_taylor_ord2_1(f, f_dx, f_dy, x0, y0, xn, h):
    """
    Resuelve una EDO de primer orden utilizando el método de Taylor de segundo.

    ARGS:
    - func: La función que define la EDO y'=func(x, y).
    - x0: valor inicial de x.
    - y0: valor inicial de y.
    - xn: extremo superior del intervalo de valores de x.
    - h: tamaño del paso.
    """
    # Inicializa las listas para almacenar los resultados
    x_values = [x0]
    y_values = [y0]

    # Itera hasta alcanzar el punto final
    while x_values[-1] < xn:
        x_0 = x_values[-1]
        y_0 = y_values[-1]

        # Calcula las derivadas hasta el orden 2
        f_deriv_1 = f(x_0, y_0)
        f_deriv_2 = f_dx(x_0, y_0) + f_dy(x_0, y_0)*f_deriv_1

        # Usa la expansión de Taylor de orden 2 para obtener la siguiente aproximación
        x_1 = x_0 + h
        y_1 = y_0 + h*f_deriv_1 + ((h**2)/2)*f_deriv_2

        # Agrega los resultados a las listas
        x_values.append(x_1)
        y_values.append(y_1)

    return x_values, y_values
