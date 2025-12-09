flowchart TD
    A([Inicio]) --> B[Importar módulo random]
    B --> C[Mostrar "**** Generador de contraseñas *******"]
    C --> D[Mostrar "*******************"]
    D --> E[Pedir al usuario tam = cantidad de caracteres]
    E --> F[Definir cadena de caracteres permitidos]
    F --> G[Inicializar contrasena = ""]
    G --> H[Iniciar bucle for i en range(tam)]
    H --> I[Generar numero aleatorio = random.randint(0, len(caracteres) - 1)]
    I --> J[Obtener caracteres[numero]]
    J --> K[Agregar carácter a contrasena]
    K --> L{¿i < tam-1?}
    L -->|Sí| H
    L -->|No| M[Mostrar "La contraseña segura es:"]
    M --> N[Mostrar valor de contrasena]
    N --> O[Mostrar "Guárdala en un lugar seguro"]
    O --> P([Fin])
