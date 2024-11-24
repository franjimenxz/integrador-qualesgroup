import pandas as pd
from db_connection import get_db_connection

def carga_stg_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/clientes.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Clientes`
    df.rename(columns={
        'CodCliente': 'ID_Cliente',
        'RazonSocial': 'Razon_Social'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Clientes`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Clientes (ID_Cliente, Razon_Social, Telefono, Mail, Direccion, Localidad, Provincia, CP)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            row['ID_Cliente'], row['Razon_Social'], row['Telefono'], row['Mail'],
            row['Direccion'], row['Localidad'], row['Provincia'], row['CP'])
        except Exception as e:
            print(f"Error al insertar cliente {row['ID_Cliente']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_clientes()
