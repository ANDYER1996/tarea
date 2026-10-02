SISTEMA DE GESTION MEDICA - ECLIPSE

VERSION CORREGIDA
- Caratula de bienvenida visible al iniciar.
- Inicio > Caratula principal vuelve a mostrar la caratula.
- Formularios se abren sobre un JDesktopPane independiente.
- Navegacion corregida para crear cada formulario correctamente.
- Entidades conservadas y compatibles con el proyecto original.

Estructura:
src/entidad -> clases entidad
src/datos -> datos en memoria
src/gui -> ventanas Swing

Para usar en Eclipse:
1. Descomprime el ZIP.
2. File > Import > Existing Projects into Workspace.
3. Selecciona la carpeta SistemaGestionMedica_Caratula.
4. Run As > Java Application sobre gui.FrmPrincipal.

Requiere Java 17 o compatible.
Los datos se almacenan en memoria y se reinician al cerrar el programa.
