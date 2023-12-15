def euler(func, a, b, y0, N):
    '''Método de Euler para resolver EDOs 
    con una única condición inicial en un intervalo [x0, xn]
    
    *ARGS*
    - a: condción inicial para x y extremo inferior del intervalo
    - b: extremo superior del intervalo
    - y0: condición inicial para y
    - N: número de pasos
    '''

    h = (b-a)/N  # tamaño del paso

    x_values = [a]
    y_values = [y0]

    for k in range(N):
        x = x_values[k]
        y = y_values[k]
        
        x_values.append ( x+h )
        y_values.append( y + h*func(x, y) )

    return x_values, y_values


def euler_1(func, a, b, y0, N):
    '''Método de Euler para resolver EDOs 
    con una única condición inicial en un intervalo [x0, xn]
    
    *ARGS*
    - a: condción inicial para x y extremo inferior del intervalo
    - b: extremo superior del intervalo
    - y0: condición inicial para y
    - N: número de pasos
    '''

    h = (b-a)/N  # tamaño del paso

    x = [a]  # valores de x
    y = [y0]  # valores de y

    for k in range(N):   
        x.append ( x[k] + h )
        y.append( y[k] + h*func(x[k], y[k]) )

    return x, y


def euler_2(func, x0, y0, xn, h):
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
