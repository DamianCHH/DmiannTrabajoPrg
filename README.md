# Diagrama de Flujo del Programa

flowchart TD

A([Inicio]) --> B[Mostrar mensaje: Generador de contraseñas]

B --> C[Inicializar tam = 0]

C --> D{tam <= 0?}
D -->|Sí| E[Pedir al usuario el tamaño de la contraseña]
E --> F{¿Ingresó número válido?}
F -->|Sí| G[Asignar valor a tam]
F -->|No| H[Mostrar: Debes ingresar un número válido] --> C
D -->|No| I[Continuar]

I --> J[Pedir cantidad de contraseñas]
J --> K{¿Ingresó número válido?}
K -->|Sí| L{¿cantidad < 1?}
L -->|Sí| M[Asignar cantidad = 1]
L -->|No| N[Continuar]
K -->|No| O[Asignar cantidad = 1]

M --> P
N --> P
O --> P

P[Definir caracteres permitidos] --> Q[Mostrar: Generando contraseñas]

Q --> R[For j en cantidad]
R --> S[Inicializar contraseña vacía]

S --> T[For i en tam]
T --> U[Elegir un carácter aleatorio]
U --> V[Agregar carácter a contraseña]
V --> T

T -->|Fin del ciclo| W[Mostrar contraseña generada]

W --> R
R -->|Fin del ciclo| X[Mostrar mensaje final: Guardarlas en lugar seguro]

X --> Y([Fin])


