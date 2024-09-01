# Calculadora-de-IMC v 1.1

1. Función get_non_empty_input

def get_non_empty_input(prompt):
    
    """Solicita al usuario que ingrese un valor no vacío."""
    
    while True:
        
        value = input(prompt).strip()
       
        if value:
            
            return value
        
        print("El campo no puede estar vacío. Por favor, intenta nuevamente.")

Propósito: Esta función solicita que ingrese un texto que no puede estar vacío.
Flujo de trabajo:

Usa un bucle while True para repetirse hasta que se obtenga un valor válido.

input(prompt) solicita al usuario una entrada con el mensaje proporcionado (prompt).

strip() elimina los espacios en blanco al principio y al final de la entrada.
Si el valor no está vacío, se retorna. Si está vacío, arroja un mensaje de error y la función vuelve a solicitar la entrada.

2. Función get_numeric_input

def get_numeric_input(prompt, tipo=float, min_val=None, max_val=None):
    
    """Solicita al usuario que ingrese un valor numérico válido de un tipo específico.
    Puede especificar un valor mínimo y máximo."""
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

Propósito: Solicita al usuario un número, verificando que sea válido (un entero o un decimal) y opcionalmente dentro de un rango definido.

Parámetros:

prompt: Mensaje que se muestra al usuario.

tipo: El tipo de dato numérico (int o float) que se espera del usuario. Por defecto es float.

min_val y max_val: Límites opcionales para el valor ingresado.

Flujo de trabajo:

El bucle while True se repite hasta que se obtenga un valor válido.

input(prompt).strip() pide al usuario una entrada.

Intenta convertir la entrada a un número usando tipo(value).

Si la conversión falla, se lanza un ValueError y se muestra un mensaje de error.

Si se proporcionan min_val o max_val, se verifican los límites; si no se cumplen, se muestra un mensaje de error y se vuelve a solicitar la entrada.

3. Función calcular_imc

def calcular_imc(peso, altura):
    
    """Calcula el índice de masa corporal (IMC) basado en el peso (kg) y la altura (m)."""
    
    return peso / (altura ** 2)

Propósito: Calcula el índice de masa corporal (IMC) usando la fórmula:

IMC = peso (kg)/(altura (m))**2


Parámetros:

peso: El peso de la persona en kilogramos.

altura: La altura de la persona en metros.

Flujo de trabajo:

Calcula el IMC dividiendo el peso entre el cuadrado de la altura.

Retorna el resultado.

4. Función clasificar_imc

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

Propósito: Clasifica el valor de IMC en una categoría según los estándares de la Organización Mundial de la Salud (OMS).

Parámetro:

imc: El índice de masa corporal calculado.

Flujo de trabajo:

Utiliza una serie de condiciones if-elif-else para clasificar el IMC en categorías: "Bajo peso", "Peso normal", "Sobrepeso", "Obesidad grado I", "Obesidad grado II" y "Obesidad grado III".

Retorna la clasificación correspondiente.

5. Función solicitar_datos_usuario


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

Propósito: Solicitar al usuario todos sus datos personales necesarios para el cálculo del IMC.

Flujo de trabajo:

Muestra un mensaje inicial para pedir datos personales.

Usa las funciones get_non_empty_input y get_numeric_input para recopilar y validar los datos del usuario.

Almacena los datos en un diccionario datos y lo retorna.

6. Función main

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

Propósito: Función principal del programa que controla el flujo general de ejecución.
de trabajo:

Llama a solicitar_datos_usuario para recopilar datos del usuario.

Calcula el IMC usando calcular_imc.

Clasifica el IMC usando clasificar_imc.

Muestra todos los datos y resultados en pantalla.

7. Ejecución del Programa


if __name__ == "__main__":
    
    main()

Propósito: Verifica si el script se está ejecutando directamente (y no importado como un módulo) y, de ser así, llama a la función main() para iniciar el programa.
