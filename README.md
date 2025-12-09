# Diagrama de Flujo del Programa

```mermaid
flowchart TD
    A([Inicio]) --> B[Importar modulo random]
    B --> C[Mostrar mensaje de titulo]
    C --> D[Pedir al usuario tam = numero de caracteres]
    D --> E[Definir cadena de caracteres permitidos]
    E --> F[Inicializar contrasena como cadena vacia]
    F --> G[Iniciar bucle for i en range(tam)]
    G --> H[Generar numero aleatorio entre 0 y longitud de caracteres - 1]
    H --> I[Obtener caracter usando caracteres[numero]]
    I --> J[Agregar caracter a la cadena contrasena]
    J --> K{Quedan iteraciones en el bucle?}
    K -->|Si| G
    K -->|No| L[Mostrar mensaje: La contraseña segura es]
    L --> M[Mostrar valor de contrasena]
    M --> N[Mostrar mensaje: Guardala en un lugar seguro]
    N --> O([Fin])
