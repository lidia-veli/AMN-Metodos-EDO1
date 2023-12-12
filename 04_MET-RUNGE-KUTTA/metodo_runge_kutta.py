def runge_kutta_ord4(f, x0, y0, xn, h):
    '''Método de Euler para resolver EDOs 
    con una única condición inicial en un intervalo [x0, xn]
    *ARGS*
    - f: función que representa la EDO y' = f(x, y)
    - x0: condción inicial para x
    - y0: condición inicial para y
    - xn: extremo superior del intervalo
    - h: tamaño del paso'''
    
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < xn:
        x_0 = x_values[-1]
        y_0 = y_values[-1]

        # Calculamos los coeficientes del método de Runge-Kutta de orden 4
        k1 = h * f(x_0, y_0)
        k2 = h * f(x_0 + 0.5*h, y_0 + 0.5*k1)
        k3 = h * f(x_0 + 0.5*h, y_0 + 0.5*k2)
        k4 = h * f(x_0 + h, y_0 + k3)

        # Calculamos la siguiente aproximación
        y_1 = y_0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_1 = x_0 + h

        # Agregamos los resultados a las listas
        x_values.append(x_1)
        y_values.append(y_1)

    return x_values, y_values
