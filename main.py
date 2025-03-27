import pandas as pd

def generar_dataset():
    data = {
        'ID': [1, 2, 3, 4, 5],
        'Nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro'],
        'Edad': [30, 25, 40, 35, 28],
        'Departamento': ['Ventas', 'TI', 'Recursos Humanos', 'Marketing', 'TI'],
        'Salario': [2500, 3200, 2800, 3000, 3500]

    }
    df = pd.DataFrame(data)
    return df

def buscar_empleado(df, nombre):
    resultado = df[df['Nombre'].str.lower() == nombre.lower()]
    if resultado.empty():
        print(f"No se encontro ningun empleado con el nombre '{nombre}'.")
    else:
        print("\nSe encontro el empleado con el nombre: ")
        print(resultado)

def buscar_por_departamento(df, departamento):
    resultado = df[df['Departamento'].str.lower() == departamento.lower()]
    if resultado.empty():
        print(f"No se encontro ningun empleado en el departamento '{departamento}'.")
    else:
        print("\nSe encontro el empleado en el departamento: ", departamento)
        print(resultado)

def calcular_salario_promedio(df):
    promedio = df['Salario'].mean()
    print(f"\nEl salario promedio de la empresa es de: ${promedio:.2f}")

def main():
    print("Generar dataset de empleados...")
    df_empleados = generar_dataset()

    print("Dataset de empleados:")
    print(df_empleados)

    nombre_empleado = input("\nIngrese el nombre del empleado a buscar: ")
    buscar_empleado(df_empleados, nombre_empleado)

    departamento = input("\nIngrese el nombre del departamento a buscar: ")
    buscar_por_departamento(df_empleados, departamento)

    calcular_salario_promedio(df_empleados)

if __name__ == "__main__":
    main()

