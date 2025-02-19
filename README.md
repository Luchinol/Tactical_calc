# Proyecto: Calculadora de Maniobras

Este proyecto es una aplicación de análisis y evaluación basada en métodos cuantitativos que se utiliza para optimizar la toma de decisiones en maniobras de unidades militares. La aplicación sigue los principios del patrón MVC (Modelo-Vista-Controlador), lo que permite una separación clara entre la lógica de negocio, el procesamiento de los datos y la interfaz de usuario.

## Estructura del Proyecto

proyecto/  
│  
├── calculadora/  
│   ├── __init__.py  
│   ├── ahp.py                 # Vista y manejo de la ventana AHP  
│   ├── gui.py                 # Vista principal: calculadora y launcher  
│   ├── tropas.py              # Contiene funciones y datos de tropas registradas  
│   │  
│   ├── controllers/           # Controladores para intermediar entre vistas y modelos  
│   │   ├── __init__.py  
│   │   ├── ahp_controller.py       # Controlador para el proceso AHP  
│   │   └── calculator_controller.py  # Controlador para cálculos en la calculadora  
│   │  
│   └── models/                # Modelos que encapsulan la lógica de negocio  
│       ├── __init__.py  
│       └── ahp_model.py       # Modelo que implementa el cálculo de la matriz AHP y sus pesos  
│  
└── README.txt                 # Este archivo

## Descripción de Funcionalidades

* **AHP Module:**
  - Implementa el método de Análisis Jerárquico de Procesos (AHP).
  - La lógica del cálculo se encuentra en el modelo `ahp_model.py` mientras que la vista `ahp.py` controla la interacción con el usuario.

* **Calculadora y Launcher:**
  - La interfaz principal se representa en `gui.py`, la cual permite la visualización de tropas propias y adversarias.
  - Se utilizan controladores para separar la lógica de negocio, como el cálculo de totales y la gestión de datos ingresados, ubicados en `calculator_controller.py`.

* **Tropas:**
  - El archivo `tropas.py` contiene funciones que proveen los datos y estructuras de las fuerzas propias y adversarias.

## Recomendaciones para Profesionalizar el Servicio

1. **Pruebas Unitarias e Integración:** Utilizar frameworks como Pytest o unittest para asegurar el correcto funcionamiento de cada componente y la integración entre ellos.

2. **Logging Avanzado:** Implementar un sistema de logging con la biblioteca `logging` de Python para capturar y almacenar eventos críticos, facilitando el diagnóstico de errores.

3. **CI/CD:** Integrar pipelines con herramientas como GitHub Actions o Jenkins para automatizar pruebas y despliegues.

4. **Documentación:** Utilizar herramientas como Sphinx para generar documentación a partir de docstrings y mantener actualizado el README.

5. **Configuración Externa:** Externalizar la configuración en archivos YAML o variables de entorno para facilitar la adaptación a diferentes entornos.

6. **Optimización y Escalabilidad:** Revisar algoritmos y considerar la paralelización de operaciones para mejorar el rendimiento en grandes volúmenes de datos.

## Cómo Ejecutar el Proyecto

1. Clona el repositorio en tu máquina local.

2. Asegúrate de tener instaladas todas las dependencias requeridas (por ejemplo, Tkinter, etc.).

3. Ejecuta el archivo principal lanzando la aplicación con:

   bash  
   python calculadora/gui.py

4. Interactúa con la aplicación utilizando las interfaces proporcionadas para evaluar la maniobra de combate y analizar las fuerzas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue las pautas de desarrollo y asegúrate de que tu código siga la arquitectura MVC para mantener la modularidad y escalabilidad del proyecto.

## Licencia

Este proyecto está bajo [Licencia MIT](LICENSE) (o la licencia que corresponda).