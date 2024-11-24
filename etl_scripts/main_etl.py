from etl_carga_stg_clientes import carga_stg_clientes
from etl_carga_stg_tiendas import carga_stg_tiendas
from etl_carga_stg_ventas import carga_stg_ventas
from etl_carga_stg_productos import carga_stg_productos
from etl_carga_stg_proveedores import carga_stg_proveedores
from etl_carga_stg_almacenes import carga_stg_almacenes
from etl_carga_stg_entregas import carga_stg_entregas
from etl_carga_stg_estado_pedido import carga_stg_estado_pedido

def main_etl():
    try:
        print("Iniciando carga de datos en las tablas `stg`...")

        print("Cargando datos en `stg.Clientes`...")
        carga_stg_clientes()
        print("Carga de `stg.Clientes` completada.\n")

        print("Cargando datos en `stg.Tiendas`...")
        carga_stg_tiendas()
        print("Carga de `stg.Tiendas` completada.\n")

        print("Cargando datos en `stg.Ventas`...")
        carga_stg_ventas()
        print("Carga de `stg.Ventas` completada.\n")

        print("Cargando datos en `stg.Productos`...")
        carga_stg_productos()
        print("Carga de `stg.Productos` completada.\n")

        print("Cargando datos en `stg.Proveedores`...")
        carga_stg_proveedores()
        print("Carga de `stg.Proveedores` completada.\n")

        print("Cargando datos en `stg.Almacenes`...")
        carga_stg_almacenes()
        print("Carga de `stg.Almacenes` completada.\n")

        print("Cargando datos en `stg.Entregas`...")
        carga_stg_entregas()
        print("Carga de `stg.Entregas` completada.\n")

        print("Cargando datos en `stg.EstadoPedido`...")
        carga_stg_estado_pedido()
        print("Carga de `stg.EstadoPedido` completada.\n")

        print("Carga de todos los datos en las tablas `stg` completada.")
    except Exception as e:
        print(f"Error durante la carga de datos: {e}")

if __name__ == "__main__":
    main_etl()
