# 📚 POO_PRACTICA - Ejercicios de Programación Orientada a Objetos

Este repositorio contiene una colección de trabajos prácticos, ejercicios de repaso y resoluciones de exámenes para la asignatura de **Programación Orientada a Objetos**, implementados en **Python**.

El objetivo principal es aplicar conceptos fundamentales como encapsulamiento, herencia, polimorfismo, manejo de excepciones, persistencia de datos (CSV) y uso de estructuras eficientes con **NumPy**.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías Externas:**
    * `numpy`: Utilizada para la gestión de arreglos dinámicos en los gestores (Manejadores).
    * `csv`: Para la lectura y escritura de archivos de datos.
    * `abc`: Para la implementación de Clases Abstractas.

---

## 📂 Contenido del Repositorio

El proyecto está dividido en módulos independientes, cada uno resolviendo una problemática diferente:

### 1. 🎮 Sistema de Gamers (Carpeta `GAMERE`)
Sistema de gestión para una empresa de videojuegos online ("VideOL SRL").
* **Entidades:** `Gamer`, `Conexiones`.
* **Funcionalidades:**
    * Carga de datos desde `gammers.csv` y `conexiones.csv`.
    * Uso de **NumPy** para gestionar las conexiones.
    * Cálculo de importes a facturar según el plan (Básico, Completo, Extendido) y horas excedidas.
    * Detección de conexiones simultáneas (sobrecarga de `__eq__`).
    * Ordenamiento de datos (sobrecarga de `__lt__`).

### 2. ⚽ Liguilla de Fútbol (Carpeta `LIGUILLA`)
Sistema para procesar resultados de partidos y generar tablas de posiciones.
* **Entidades:** `Equipo`, `Resultado`.
* **Funcionalidades:**
    * Carga de equipos y resultados de fechas.
    * Cálculo automático de puntos (3 por ganar, 1 por empatar) y diferencia de goles.
    * Generación de **Tabla de Posiciones** ordenada dinámicamente.
    * Consulta de resultados por equipo (Local vs Visitante).

### 3. 🚌 Gestión de Colectivos (Carpeta `COLECTIVOS`)
Administración de flota de colectivos y tramos de viaje.
* **Entidades:** `Colectivo`, `Tramo`.
* **Funcionalidades:**
    * Relación entre viajes y vehículos.
    * Cálculo de kilometraje total y consumo estimado de combustible.
    * Filtrado de tramos por distancia superior a un valor dado.

### 4. 🏥 Clínica Médica (Carpeta `EJ6`)
Administración de pacientes y sus atenciones médicas.
* **Entidades:** `Paciente`, `Atenciones`.
* **Funcionalidades:**
    * Listado de pacientes que **no** registraron atenciones.
    * Búsqueda de atenciones por fecha e importe total.
    * Ordenamiento de pacientes por Apellido y Unidad.

### 5. 📱 Planes de Telefonía y TV (Carpeta `poo`)
Ejemplo claro de **Herencia y Clases Abstractas**.
* **Entidades:** `Plan` (Abstracta) -> `Telefonico`, `Television`.
* **Funcionalidades:**
    * Polimorfismo en el cálculo de importes finales con descuentos.
    * Carga heterogénea de planes en una misma lista.
    * Consultas por cobertura geográfica y cantidad de canales.

### 6. 🚛 Logística y Movilidad (Carpeta `practica 1`)
Control de gastos para una empresa de logística ("Transportes Andinos").
* **Entidades:** `Movilidad`, `Gasto`.
* **Funcionalidades:**
    * Gestor de gastos implementado con listas Python.
    * Gestor de movilidades implementado con **NumPy**.
    * Reporte de gastos totales agrupados por fecha o patente.

---

## 🚀 Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/facundocom/POO_PRACTICA.git](https://github.com/facundocom/POO_PRACTICA.git)
    cd POO_PRACTICA
    ```

2.  **Instalar dependencias:**
    Este proyecto requiere `numpy`. Puedes instalarlo ejecutando:
    ```bash
    pip install numpy
    ```

3.  **Ejecutar un ejercicio:**
    Navega a la carpeta del ejercicio que desees probar y ejecuta el archivo `main.py`.
    *Ejemplo:*
    ```bash
    cd LIGUILLA
    python main.py
    ```

    > **Nota:** Asegúrate de que los archivos `.csv` estén en la misma carpeta desde donde ejecutas el script para evitar errores de "File not found".

---

## ✒️ Autor

* **Facundo Coria** - [Perfil de GitHub](https://github.com/facundocom)
* *Materia:* Programación Orientada a Objetos.

---
