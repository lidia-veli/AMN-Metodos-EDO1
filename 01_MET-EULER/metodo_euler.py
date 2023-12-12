def euler(func, x0, y0, xn, h):
    '''Método de Euler para resolver EDOs 
    con una única condición inicial en un intervalo [x0, xn]
    *ARGS*
    - x0: condción inicial para x
    - y0: condición inicial para y
    - xn: extremo superior del intervalo
    - h: tamaño del paso'''

    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < xn:
        x = x_values[-1]
        y = y_values[-1]
        
        x_values.append ( x+h )
        y_values.append( y + h*func(x, y) )

    return x_values, y_values
