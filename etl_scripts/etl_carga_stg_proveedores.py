import pandas as pd
from db_connection import get_db_connection

def carga_stg_proveedores():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/proveedores.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Proveedores`
    df.rename(columns={
        'CodProveedor': 'ID_Proveedor'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Proveedores`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Proveedores (ID_Proveedor, Nombre_Proveedor, Costo_Estimado)
                VALUES (?, ?, ?)
            """, 
            row['ID_Proveedor'], row['Nombre_Proveedor'], row['Costo_Estimado'])
        except Exception as e:
            print(f"Error al insertar proveedor {row['ID_Proveedor']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_proveedores()
