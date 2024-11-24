import pandas as pd
from db_connection import get_db_connection

def carga_stg_estado_pedido():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/EstadoDelPedido.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.EstadoPedido`
    df.rename(columns={
        'CodEstado': 'ID_Estado'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.EstadoPedido`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.EstadoPedido (ID_Estado, Descripcion_Estado)
                VALUES (?, ?)
            """, 
            row['ID_Estado'], row['Descripcion_Estado'])
        except Exception as e:
            print(f"Error al insertar estado {row['ID_Estado']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_estado_pedido()
