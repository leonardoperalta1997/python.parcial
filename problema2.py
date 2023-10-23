print("Bienvenido")

def get_temperature():
    while True:
        try:
            temperature = float(input("Ingresa la temperatura en grados centígrados: "))
            return temperature
        except ValueError:
            print("Por favor, ingresa un número válido.")

def get_message(temperature):
    if temperature < 0:
        return "La temperatura es muy baja. ¡Estás en el clima ártico!"
    elif temperature < 10:
        return "La temperatura es muy fría."
    elif temperature < 20:
        return "La temperatura es fría."
    elif temperature < 30:
        return "La temperatura es normal."
    elif temperature < 40:
        return "La temperatura es caliente."
    else:
        return "La temperatura es muy caliente."

temperature = get_temperature()
message = get_message(temperature)
print(message)
