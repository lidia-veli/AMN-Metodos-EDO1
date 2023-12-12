
def euler_predict_correct(func, x0, y0, xn, h):
    '''Método Predictor Corrector para resolver EDOs
    con una única condición inicial en un intervalo [x0, xn]
    *ARGS*
    - x0: condción inicial para x
    - y0: condición inicial para y
    - xn: extremo superior del intervalo
    - h: tamaño del paso
    '''

    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < xn:
        x_0 = x_values[-1]
        y_0 = y_values[-1]
        z = y_0 + h*func(x_0, y_0)

        # valor corregido de x
        x_1 = x_0 + h  
        x_values.append (x_1)
        # valor corregido de y
        y_1 = y_0 + (h/2) * (func(x_0,y_0)+func(x_1, z))
        y_values.append(y_1)

    return x_values, y_values
