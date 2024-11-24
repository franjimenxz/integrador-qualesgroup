import pandas as pd
from db_connection import get_db_connection

def carga_stg_tiendas():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/tiendas.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Tiendas`
    df.rename(columns={
        'CodigoTienda': 'ID_Tienda',
        'Descripcion': 'Descripcion',
        'Direccion': 'Direccion',
        'Localidad': 'Localidad',
        'Provincia': 'Provincia',
        'CP': 'CP',
        'TipoTienda': 'Tipo_Tienda'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Tiendas`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Tiendas (ID_Tienda, Descripcion, Direccion, Localidad, Provincia, CP, Tipo_Tienda)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, 
            row['ID_Tienda'], row['Descripcion'], row['Direccion'], 
            row['Localidad'], row['Provincia'], row['CP'], row['Tipo_Tienda'])
        except Exception as e:
            print(f"Error al insertar tienda {row['ID_Tienda']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_tiendas()
