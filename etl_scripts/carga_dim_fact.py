import pyodbc
from db_connection import get_db_connection

def execute_stored_procedure(proc_name, params=None):
    """
    Ejecuta un stored procedure con parámetros opcionales.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if params:
            print(f"Ejecutando {proc_name} con parámetros: {params}")
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

if __name__ == "__main__":
    # Stored Procedures para tablas dim
    dim_procedures = [
        ("sp_carga_Dim_Clientes", None),
        ("sp_carga_Dim_Tiendas", None),
        ("sp_carga_Dim_Productos", None),
        ("sp_carga_Dim_Proveedores", None),
        ("sp_carga_Dim_Almacenes", None),
        ("sp_carga_Dim_EstadoPedido", None),
        ("Sp_Genera_Dim_Tiempo", (2024,))  
    ]

    # Stored Procedures para tablas fact
    fact_procedures = [
        ("sp_carga_Fact_Ventas", None),
        ("sp_carga_Fact_Entregas", None)
    ]

    print("Cargando tablas `dim`...")
    for proc, params in dim_procedures:
        execute_stored_procedure(proc, params)

    print("\nCargando tablas `fact`...")
    for proc, params in fact_procedures:
        execute_stored_procedure(proc, params)
