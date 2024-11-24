import pandas as pd
from db_connection import get_db_connection

def carga_stg_entregas():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/entregas.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Entregas`
    df.rename(columns={
        'CodEntrega': 'ID_Entrega',
        'CodVenta': 'ID_Venta',
        'CodProveedor': 'ID_Proveedor',
        'CodAlmacen': 'ID_Almacen',
        'CodEstado': 'ID_Estado',
        'Fecha_Envio': 'Fecha_Envio',
        'Fecha_Entrega': 'Fecha_Entrega'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Entregas`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Entregas (ID_Entrega, ID_Venta, ID_Proveedor, ID_Almacen, ID_Estado, Fecha_Envio, Fecha_Entrega)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, 
            row['ID_Entrega'], row['ID_Venta'], row['ID_Proveedor'], 
            row['ID_Almacen'], row['ID_Estado'], row['Fecha_Envio'], row['Fecha_Entrega'])
        except Exception as e:
            print(f"Error al insertar entrega {row['ID_Entrega']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_entregas()
