import pyodbc
from db_connection import get_db_connection

def execute_stored_procedure(proc_name, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if params:
            print(f"Ejecutando {proc_name} con parámetros: {params}...")
            cursor.execute(f"EXEC {proc_name} @anio = ?", params)
        else:
            print(f"Ejecutando {proc_name}...")
            cursor.execute(f"EXEC {proc_name}")
        conn.commit()
        print(f"{proc_name} ejecutado correctamente.")
    except Exception as e:
        print(f"Error ejecutando {proc_name}: {e}")
    finally:
        conn.close()

def execute_all_procedures(procedures):
    conn = get_db_connection()
    cursor = conn.cursor()

    for proc_name, params in procedures:
        try:
            if params:
                print(f"Ejecutando {proc_name} con parámetros: {params}...")
                cursor.execute(f"EXEC {proc_name} @anio = ?", params)
            else:
                print(f"Ejecutando {proc_name}...")
                cursor.execute(f"EXEC {proc_name}")
            conn.commit()
            print(f"{proc_name} ejecutado correctamente.")
        except Exception as e:
            print(f"Error ejecutando {proc_name}: {e}")

    conn.close()

if __name__ == "__main__":
    # Stored procedures para las tablas `int`
    procedures_int = [
        ("sp_carga_Int_Clientes", None),
        ("sp_carga_Int_Tiendas", None),
        ("sp_carga_Int_Ventas", None),
        ("sp_carga_Int_Productos", None),
        ("sp_carga_Int_Proveedores", None),
        ("sp_carga_Int_Entregas", None),
        ("sp_carga_Int_Almacenes", None),
        ("sp_carga_Int_EstadoPedido", None)
    ]

    # Stored procedures para las tablas `dim`
    procedures_dim = [
        ("sp_carga_Dim_Clientes", None),
        ("sp_carga_Dim_Tiendas", None),
        ("sp_carga_Dim_Productos", None),
        ("sp_carga_Dim_Proveedores", None),
        ("sp_carga_Dim_Almacenes", None),
        ("sp_carga_Dim_EstadoPedido", None),
        ("Sp_Genera_Dim_Tiempo", (2024,))
    ]

    # Stored procedures para las tablas `fact`
    procedures_fact = [
        ("sp_carga_Fact_Ventas", None),
        ("sp_carga_Fact_Entregas", None)
    ]

    # Mostrar menú
    print("Seleccione una opción:")
    print("1. Ejecutar todos los stored procedures `int`")
    print("2. Ejecutar todos los stored procedures `dim`")
    print("3. Ejecutar todos los stored procedures `fact`")
    print("4. Ejecutar un stored procedure específico (`int`, `dim` o `fact`)")

    try:
        choice = int(input("\nIngrese el número de la opción: "))
        if choice == 1:
            execute_all_procedures(procedures_int)
        elif choice == 2:
            execute_all_procedures(procedures_dim)
        elif choice == 3:
            execute_all_procedures(procedures_fact)
        elif choice == 4:
            print("\nSeleccione el procedimiento a ejecutar:")
            all_procedures = procedures_int + procedures_dim + procedures_fact
            for i, (proc, params) in enumerate(all_procedures, start=1):
                print(f"{i}. {proc}")
            proc_choice = int(input("\nIngrese el número del procedimiento: "))
            if 1 <= proc_choice <= len(all_procedures):
                proc_name, params = all_procedures[proc_choice - 1]
                execute_stored_procedure(proc_name, params)
            else:
                print("Opción inválida. Por favor seleccione un número válido.")
        else:
            print("Opción inválida. Por favor seleccione un número válido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
