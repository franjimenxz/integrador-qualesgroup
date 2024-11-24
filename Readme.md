# Proyecto: Data Warehouse para DataShop

Este proyecto implementa un **Data Warehouse (DW)** para la empresa **DataShop**, utilizando herramientas como **SQL Server** y **Python** para manejar y transformar datos provenientes de diferentes fuentes.
## Modelo Lógico de Datos

### Dimensiones
- **Dim_Clientes**
- **Dim_Tiendas**
- **Dim_Productos**
- **Dim_Proveedores**
- **Dim_Almacenes**
- **Dim_EstadoPedido**
- **Dim_Tiempo**

### Hechos
- **Fact_Ventas**
- **Fact_Entregas**

## Imagen del Modelo Físico
![Modelo DW](DW_DataShop-db.png)

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujo de Trabajo](#flujo-de-trabajo)
- [Requisitos](#requisitos)
- [Implementación](#implementación)
  - [ETL](#etl)
  - [Stored Procedures](#stored-procedures)
  - [Carga de Tablas Dimensionales y de Hechos](#carga-de-tablas-dimensionales-y-de-hechos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Estructura del Data Warehouse](#estructura-del-data-warehouse)

## Descripción del Proyecto

Este proyecto permite la construcción de un **Data Warehouse** desde datos en formato **CSV**. Se divide en las siguientes etapas:

1. **Extracción**: Carga de datos desde archivos CSV.
2. **Transformación**: Limpieza y normalización de datos en tablas `stg` (staging).
3. **Carga**: Inserción de datos procesados en tablas `int` (intermedias) y finalmente en tablas `dim` (dimensiones) y `fact` (hechos).

## Estructura del Proyecto
DW_DataShop/
├── data/                     # Contiene los archivos CSV con los datos fuente
│   ├── Almacenes.csv
│   ├── clientes.csv
│   ├── Entregas.csv
│   ├── EstadoDelPedido.csv
│   ├── productos.csv
│   ├── Proveedores.csv
│   ├── tiendas.csv
│   ├── ventas.csv
│
├── etl_scripts/              # Scripts ETL para cargar datos y procedimientos almacenados
│   ├── db_connection.py      # Archivo de conexión a la base de datos
│   ├── etl_carga_stg_clientes.py
│   ├── etl_carga_stg_tiendas.py
│   ├── etl_carga_stg_ventas.py
│   ├── etl_carga_stg_productos.py
│   ├── etl_carga_stg_proveedores.py
│   ├── etl_carga_stg_estado_pedido.py
│   ├── etl_carga_stg_almacenes.py
│   ├── etl_carga_stg_entregas.py
│   ├── carga_dim_fact.py     # Script para cargar las tablas dim y fact
│   ├── etl_carga_sp.py       # Script para ejecutar todos los SP (Int, Dim y Fact)
│   ├── main_etl.py           # Script principal para orquestar todo el flujo ETL
│
├── Reporte de Ventas.xlsx    # Reporte generado (opcional)
├── DW_DataShop-db.png        # Diagrama del modelo de datos (opcional)
├── sp.txt                    # Archivo con los stored procedures en formato texto
├── README.md                 # Documentación del proyecto


## Flujo de Trabajo

1. **ETL a Tablas Staging (`stg`)**:
   - Se extraen datos desde archivos CSV utilizando Python.
   - Los datos se limpian y transforman según las necesidades del negocio.

2. **Carga a Tablas Intermedias (`int`)**:
   - Los datos limpios de las tablas `stg` se procesan y cargan a tablas intermedias utilizando stored procedures.

3. **Carga de Tablas Dimensionales (`dim`)**:
   - Las dimensiones como `Clientes`, `Productos`, etc., se generan a partir de las tablas `int`.

4. **Carga de Tablas de Hechos (`fact`)**:
   - Se construyen las tablas `Fact_Ventas` y `Fact_Entregas` a partir de las dimensiones y las tablas `int`.

5. **Generación de la Dimensión de Tiempo (`Dim_Tiempo`)**:
   - Un stored procedure genera esta tabla basada en el año especificado.

## Requisitos

- **SQL Server**
- **Python 3.11** o superior
- Librerías Python:
  - `pandas`
  - `pyodbc`

## Implementación

### ETL

Los scripts ETL se encuentran en la carpeta `etl_scripts/` y procesan los datos en el siguiente orden:

1. **Staging (`stg`)**:
   - Cada script carga un archivo CSV en su respectiva tabla `stg`.
2. **Intermedias (`int`)**:
   - Se ejecutan stored procedures para procesar y cargar los datos en las tablas `int`.

### Stored Procedures

- **Carga Dimensional**: 
  - Stored procedures como `sp_carga_Dim_Clientes` y `sp_carga_Dim_Productos` procesan datos desde `int` hacia `dim`.
- **Carga de Hechos**:
  - `sp_carga_Fact_Ventas` y `sp_carga_Fact_Entregas` combinan las dimensiones y datos intermedios para generar las tablas de hechos.

### Carga de Tablas Dimensionales y de Hechos

Cargar stg: Scripts como etl_carga_stg_clientes.py para cargar cada tabla staging.
Cargar dim y fact: carga_dim_fact.py para ejecutar los SP relacionados.
SP generales: etl_carga_sp.py para ejecutar todos los stored procedures de forma modular.
Script principal: main_etl.py para orquestar todo el flujo.

## Instrucciones de Uso

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/franjimenxz/DataShop-DW-QualesGroup.git
   cd DataShop-DW-QualesGroup
