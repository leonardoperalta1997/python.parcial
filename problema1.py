print("Bienvenido")

x = float(input("Ingresa el valor de X: "))
y = float(input("Ingresa el valor de Y: "))

if x > 0 and y > 0:
    print(f"El punto ({x},{y}) se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print(f"El punto ({x},{y}) se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print(f"El punto ({x},{y}) se encuentra en el tercer cuadrante.")
elif x > 0 and y < 0:
    print(f"El punto ({x},{y}) se encuentra en el cuarto cuadrante.")
else:
    print(f"El punto ({x},{y}) se encuentra en el origen.")
