import pandas as pd
from db_connection import get_db_connection

def carga_stg_productos():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/productos.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Productos`
    df.rename(columns={
        'CodigoProducto': 'ID_Producto',
        'PrecioCosto': 'Precio_Costo',
        'PrecioVentaSugerido': 'Precio_Venta_Sugerido'
    }, inplace=True)

    # Verificar que las columnas están correctamente ajustadas
    print("Columnas ajustadas:", df.columns)

    # Insertar datos en la tabla `stg.Productos`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Productos (ID_Producto, Descripcion, Categoria, Marca, Precio_Costo, Precio_Venta_Sugerido)
                VALUES (?, ?, ?, ?, ?, ?)
            """, 
            row['ID_Producto'], row['Descripcion'], row['Categoria'], 
            row['Marca'], row['Precio_Costo'], row['Precio_Venta_Sugerido'])
        except Exception as e:
            print(f"Error al insertar producto {row['ID_Producto']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_productos()
