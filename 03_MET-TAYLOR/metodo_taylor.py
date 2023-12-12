def metodo_taylor_ord1(func, x0, y0, xn, h):
    """es el metodo de Euler"""

    x_values = [x0]
    y_values = [y0]
    

    while x_values[-1] < xn:
        x_0 = x_values[-1]
        y_0 = y_values[-1]
        
        deriv_y = func(x_0, y_0)
        
        x_1 = x_0 + h
        y_1 = y_0 + h * deriv_y
        
        x_values.append(x_1)
        y_values.append(y_1)

    return x_values, y_values


def metodo_taylor_ord2(f, f_dx, f_dy, x0, y0, xn, h):
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
