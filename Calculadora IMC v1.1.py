def get_non_empty_input(prompt):
    """Solicita al usuario que ingrese un valor no vacío."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("El campo no puede estar vacío. Por favor, intenta nuevamente.")

def get_numeric_input(prompt, tipo=float, min_val=None, max_val=None):
    """
    Solicita al usuario que ingrese un valor numérico válido de un tipo específico.
    Puede especificar un valor mínimo y máximo.
    """
    while True:
        value = input(prompt).strip()
        try:
            number = tipo(value)
            if min_val is not None and number < min_val:
                print(f"El valor debe ser mayor o igual a {min_val}. Por favor, intenta nuevamente.")
                continue
            if max_val is not None and number > max_val:
                print(f"El valor debe ser menor o igual a {max_val}. Por favor, intenta nuevamente.")
                continue
            return number
        except ValueError:
            print("Debes ingresar un número válido. Por favor, intenta nuevamente.")

def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC) basado en el peso (kg) y la altura (m)."""
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

def solicitar_datos_usuario():
    """Solicita los datos personales del usuario y retorna un diccionario con los valores ingresados."""
    print("Por favor, introduce tus datos personales.")
    datos = {
        "nombre": get_non_empty_input("Nombre: "),
        "apellido_paterno": get_non_empty_input("Apellido paterno: "),
        "apellido_materno": get_non_empty_input("Apellido materno: "),
        "edad": get_numeric_input("Edad (años): ", int, 0),
        "peso": get_numeric_input("Peso (kg): ", float, 0),
        "altura": get_numeric_input("Altura (m): ", float, 0.5, 2.5)
    }
    return datos

def main():
    datos = solicitar_datos_usuario()

    # Calcular el IMC
    imc = calcular_imc(datos["peso"], datos["altura"])
    clasificacion = clasificar_imc(imc)

    # Desplegar los datos en pantalla
    print("\n--- Datos Personales ---")
    print(f"Nombre Completo: {datos['nombre']} {datos['apellido_paterno']} {datos['apellido_materno']}")
    print(f"Edad: {datos['edad']} años")
    print(f"Peso: {datos['peso']} kg")
    print(f"Estatura: {datos['altura']} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()
