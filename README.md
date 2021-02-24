# PruebaCRUD

Crear un proyecto, Backend y Frontend, donde estos se comuniquen via API Rest
usando el Framework o la tecnología que les facilite el desarrollo (Si usas Symfony es
valorado, más no una limitante)
La idea del proyecto es realizar dos CRUD (create, read, update, delete):
1. Productos
2. Categoría de productos.
Base de datos:
una limitante)
(si usas un servicio online de almacenamiento de datos, sera valorado, más no
• Productos:
◦ id (entero)
◦ código (string)
◦ nombre (string)
◦ descripción (string)
◦ marca (string)
◦ categoría (relación con la categoría de productos)
◦ precio (float).
• Categorías de productos:
◦ id (entero)
◦ código (string)
◦ nombre (string)
◦ descripción (string)
◦ activo (booleano).
El CRUD debe de mantener estas Validaciones
• Productos:
◦ Todos los campos son obligatorios.
◦ El nombre y el código no pueden repetirse.
◦ El código no puede contener caracteres especiales ni espacios.
◦ El código debe tener mínimo 4 caracteres y máximo 10.
◦ El nombre debe contener mínimo 4 caracteres.
◦ El precio debe ser un número válido.
•
Categorías de productos:
◦ Todos los campos son obligatorios.
◦ El nombre y el código no pueden repetirse.
◦ El código no puede contener caracteres especiales ni espacios.
◦ El nombre debe contener mínimo 2 caracteres.
La proyecto debe Permitir:
• Listar productos. (Paginar los productos es un Plus o Adicional) .
• Filtrar productos. (Opcional, es un plus) .
• Ordenar por columna (Opcional, es un plus) .
• Crear Productos.
• Editar Productos.
• Eliminar Productos (El usuario debe confirmar esta acción, es decir, se le debe
preguntar al usuario si está seguro de que desea eliminar el producto) .
• Listar Categorías de productos.
• Crear Categoría de Producto.
• Editar Categoría de Producto.•
La aplicación pueda mostrar un resumen general de todos los productos ( es
valorado, más no una limitante )
