import numpy as np
import time
import os

def render_ring():
    A, B = 0, 0
    # Caracteres de iluminación (del más oscuro al más claro)
    chars = ".,-~:;=!*#$@"
    
    while True:
        # Limpiar consola (Windows / Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Buffers de la pantalla
        b = [' '] * 1760
        z = [0] * 1760
        
        # Generar puntos del toroide (anillo)
        for j in np.arange(0, 6.28, 0.07):
            for i in np.arange(0, 6.28, 0.02):
                c = np.sin(i)
                d = np.cos(j)
                e = np.sin(A)
                f = np.sin(j)
                g = np.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = np.cos(i)
                m = np.cos(B)
                n = np.sin(B)
                t = c * h * g - f * e
                
                # Proyección 2D
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = x + 80 * y
                
                # Cálculo de iluminación
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                
                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = chars[N if N > 0 else 0]
        
        # Imprimir el frame
        for k in range(1760):
            print(b[k] if k % 80 else '\n', end='')
            
        A += 0.04
        B += 0.02
        time.sleep(0.03)

if __name__ == '__main__':
    render_ring()