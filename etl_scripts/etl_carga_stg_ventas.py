import pandas as pd
from db_connection import get_db_connection

def carga_stg_ventas():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cargar datos desde el archivo CSV con manejo de espacios
    df = pd.read_csv('./data/ventas.csv', skipinitialspace=True)

    # Renombrar las columnas para coincidir con la tabla `stg.Ventas`
    df.rename(columns={
        'CodVenta': 'ID_Venta',
        'FechaVenta': 'Fecha_Venta',
        'CodigoProducto': 'ID_Producto',
        'CodigoCliente': 'ID_Cliente',
        'CodigoTienda': 'ID_Tienda',
        'PrecioVenta': 'Precio_Venta'
    }, inplace=True)

    # Verificar las columnas después del renombrado
    print("Columnas ajustadas:", df.columns)

    # Eliminar espacios en blanco de las celdas
    df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

    # Validar y limpiar los datos
    try:
        df['ID_Venta'] = df['ID_Venta'].astype(int)
        df['ID_Producto'] = df['ID_Producto'].astype(int)
        df['Cantidad'] = df['Cantidad'].astype(int)
        df['Precio_Venta'] = pd.to_numeric(df['Precio_Venta'], errors='coerce').round(2)
        df['ID_Cliente'] = df['ID_Cliente'].astype(int)
        df['ID_Tienda'] = df['ID_Tienda'].astype(int)
        df['Fecha_Venta'] = pd.to_datetime(df['Fecha_Venta'], errors='coerce')
    except KeyError as e:
        print(f"Error: columna faltante en los datos - {e}")
        return
    except Exception as e:
        print(f"Error al convertir datos: {e}")
        return

    # Filtrar filas con datos inválidos
    df = df.dropna()

    # Insertar datos en la tabla `stg.Ventas`
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO stg.Ventas (ID_Venta, Fecha_Venta, ID_Producto, Producto, Cantidad, Precio_Venta, 
                                        ID_Cliente, Cliente, ID_Tienda, Tienda)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            row['ID_Venta'], row['Fecha_Venta'], row['ID_Producto'], row['Producto'], 
            row['Cantidad'], row['Precio_Venta'], row['ID_Cliente'], row['Cliente'], 
            row['ID_Tienda'], row['Tienda'])
        except Exception as e:
            print(f"Error al insertar venta {row['ID_Venta']}: {e}")
            continue

    conn.commit()
    conn.close()

if __name__ == '__main__':
    carga_stg_ventas()
