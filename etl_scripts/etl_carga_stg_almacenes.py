import pandas as pd
from db_connection import get_db_connection

def carga_stg_almacenes():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/almacenes.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Almacenes`
    df.rename(columns={
        'CodAlmacen': 'ID_Almacen'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Almacenes`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Almacenes (ID_Almacen, Nombre_Almacen, Ubicacion)
                VALUES (?, ?, ?)
            """, 
            row['ID_Almacen'], row['Nombre_Almacen'], row['Ubicacion'])
        except Exception as e:
            print(f"Error al insertar almacén {row['ID_Almacen']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_almacenes()
