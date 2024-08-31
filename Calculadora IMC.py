def get_non_empty_input(prompt):
    """Solicita al usuario que ingrese un valor no vacío."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("El campo no puede estar vacío. Por favor, intenta nuevamente.")

def get_numeric_input(prompt):
    """Solicita al usuario que ingrese un valor numérico válido."""
    while True:
        value = input(prompt).strip()
        # Validar si es un número
        try:
            return float(value) if '.' in value else int(value)
        except ValueError:
            print("Debes ingresar un número válido. Por favor, intenta nuevamente.")


def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC según los estándares de la OMS."""
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"
    
def main():
    print("Por favor, introduce tus datos personales.")
    # Solicitar datos del usuario
    nombre = get_non_empty_input("Nombre: ")
    apellido_paterno = get_non_empty_input("Apellido paterno: ")
    apellido_materno = get_non_empty_input("Apellido materno: ")
    edad = get_numeric_input("Edad (años): ")
    peso = get_numeric_input("Peso (kg): ")
    altura = get_numeric_input("Altura (m): ")

    # Calcular el IMC
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    # Desplegar los datos en pantalla
    print("\n--- Datos Pers onales ---")
    print(f"Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {altura} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()
