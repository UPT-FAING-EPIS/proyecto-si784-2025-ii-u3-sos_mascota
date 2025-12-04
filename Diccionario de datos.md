

` `**![C:\Users\EPIS\Documents\upt.png](media/Aspose.Words.b92227d5-37f1-42be-9f4f-06baad36bdae.001.png)**






**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**



**Desarrollo de Aplicativo Móvil “SOS Mascota”**

Curso: Calidad y Pruebas de Software


Docente: Mag. Patrick Cuadros Quiroga



Integrantes:

1. Christian Dennis Hinojosa Mucho		(2019065161)
1. Royser Alonsso Villanueva Mamani		(2021071090)
1. Gilmer Donaldo Mamani Condori		(2012042779)

**   


**Tacna – Perú**

***2025***

# <a name="_heading=h.v9wtniso4pp9"></a>**DICCIONARIO DE DATOS**


## <a name="_heading=h.fpfmf4c65168"></a>**Colecciones Principales**
### <a name="_heading=h.jwec2h7ljzim"></a>**1. usuarios**
Almacena perfiles de usuario y estado de autenticación. Cada ID de documento corresponde al UID de Firebase Auth.
|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|uid|string|ID de usuario de Firebase Auth (ID del documento)|
|nombre|string|Nombre completo del usuario|
|correo|string|Dirección de correo electrónico|
|telefono|string|Número de teléfono de contacto|
|ubicacion|string|Ubicación general del usuario|
|fotoPerfil|string|URL de Firebase Storage para foto de perfil|
|guardados|array|Lista de IDs de reportes guardados|
|notificacionesPush|boolean|Preferencia de notificaciones push|
|estadoVerificado|boolean|Si el DNI del usuario ha sido verificado|







**2. reportes\_mascotas**

Almacena reportes de mascotas perdidas creadas por usuarios. Es la entidad principal del flujo de búsqueda de mascotas.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|usuarioId|string|Clave foránea a colección usuarios|
|nombre|string|Nombre de la mascota|
|tipo|string|Tipo de mascota (ej: "Perro", "Gato")|
|raza|string|Raza de la mascota|
|estado|string|Estado: "PERDIDO" o "ENCONTRADO"|
|fotos|array|Lista de URLs de Firebase Storage|
|direccion|string|Dirección donde se perdió la mascota|
|distrito|string|Distrito/barrio|
|latitud|double|Coordenada GPS de latitud|
|longitud|double|Coordenada GPS de longitud|
|fechaPerdida|string|Fecha en que se perdió (cadena formateada)|
|horaPerdida|string|Hora en que se perdió|
|descripcion|string|Descripción detallada de la mascota|
|recompensa|string|Información de recompensa|
|fechaRegistro|timestamp|Timestamp del servidor Firestore|
###
### <a name="_heading=h.pns3ttmz9c1i"></a><a name="_heading=h.86b4n2w46rrx"></a>**3. avistamientos**
Almacena reportes de avistamientos de mascotas. Cuando el algoritmo de IA identifica similitud ≥ 80%, un avistamiento se vincula a un reporte.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|usuarioId|string|Clave foránea a usuarios|
|foto|string|URL de foto única (no array)|
|descripcion|string|Descripción del avistamiento|
|direccion|string|Dirección del avistamiento|
|distrito|string|Distrito/barrio|
|latitud|double|Coordenada GPS de latitud|
|longitud|double|Coordenada GPS de longitud|
|fechaAvistamiento|string|Fecha del avistamiento|
|horaAvistamiento|string|Hora del avistamiento|
|reporteId|string|Clave foránea a reportes\_mascotas coincidente|
|fechaRegistro|timestamp|Timestamp del servidor Firestore|
###
### <a name="_heading=h.xx8k6tkssr0r"></a><a name="_heading=h.a96lycdhig3b"></a>**4. notificaciones**
Almacena metadatos de notificaciones push e historial de notificaciones en la aplicación.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|usuarioId|string|Clave foránea a usuarios|
|titulo|string|Título de la notificación|
|mensaje|string|Cuerpo/contenido de la notificación|
|tipo|string|Tipo/categoría de notificación|
|fecha|timestamp|Timestamp del servidor Firestore|
|leido|boolean|Estado de lectura (default: false)|
###

###
### <a name="_heading=h.7d165xqabs1d"></a><a name="_heading=h.i8fofsp3b0p4"></a><a name="_heading=h.w99434kg1bu1"></a>**5. chats**
Gestiona sesiones de conversación entre usuarios sobre reportes de mascotas específicas.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|reporteId|string|Clave foránea a reportes\_mascotas|
|tipo|string|Identificador de tipo de chat|
|publicadorId|string|ID de usuario del propietario del reporte|
|usuarioId|string|ID de usuario del otro participante|
|usuarios|array|Lista de IDs de participantes|
|fechaInicio|timestamp|Timestamp de inicio del chat|
###
###
###
###
###
###
###
###
###

### <a name="_heading=h.jc1bcbhxozd4"></a><a name="_heading=h.ri8o43ynpaeo"></a><a name="_heading=h.p2eh0ku0iujh"></a><a name="_heading=h.fyh3jkx16oml"></a><a name="_heading=h.5i9jmd4qpe3m"></a><a name="_heading=h.jeow4h6fuo4t"></a><a name="_heading=h.lswp3r4gi0m1"></a><a name="_heading=h.msbrjqma4dze"></a><a name="_heading=h.r4jprmd1jd4d"></a><a name="_heading=h.geb4u58vmrqp"></a>**6. mensajes (subcolección)**
Existe bajo cada ruta chats/{chatId}/mensajes y almacena mensajes individuales.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|chatId|string|ID del documento chat padre|
|texto|string|Contenido del mensaje|
|usuarioId|string|ID de usuario del remitente|
|fechaEnvio|timestamp|Timestamp de envío del mensaje|
### <a name="_heading=h.be78krykie2a"></a>**7. comentarios**
Almacena comentarios de usuarios con características sociales como likes y shares.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|usuarioId|string|Clave foránea a usuarios|
|texto|string|Contenido del comentario|
|autor|string|Nombre para mostrar del autor|
|fecha|timestamp|Timestamp de creación|
|mediaUrl|string|URL de medio adjunto|
|mediaType|string|Tipo de medio (imagen/video)|
|likes|array|Lista de IDs de usuarios que dieron like|
|shares|int|Contador de shares|

### <a name="_heading=h.k6ke8aqmvcng"></a>**8. respuestas (subcolección)**
Existe bajo cada ruta comentarios/{comentarioId}/respuestas para discusiones en hilo.

|Campo|Tipo|Descripción|
| :-: | :-: | :-: |
|id|string|ID del documento (auto-generado)|
|comentarioId|string|ID del documento comentario padre|
|usuarioId|string|ID de usuario del autor de la respuesta|
|texto|string|Contenido de la respuesta|
|fecha|timestamp|Timestamp de creación|
## <a name="_heading=h.54t4xnutby38"></a>**Relaciones Clave**
- reportes\_mascotas ← avistamientos (via reporteId cuando hay coincidencia IA)
- usuarios → reportes\_mascotas (via usuarioId)
- usuarios → avistamientos (via usuarioId)
- chats → reportes\_mascotas (via reporteId)
- chats → mensajes (subcolección)
- comentarios → respuestas (subcolección)
## <a name="_heading=h.z05tkb4de1tk"></a>**Notas**
- Todos los campos timestamp usan FieldValue.serverTimestamp()
- Los IDs de documentos son auto-generados por Firestore
- Los campos de clave foránea (usuarioId, reporteId) son strings que coinciden con IDs de documentos
- El modelo de datos soporta el flujo completo de búsqueda de mascotas incluyendo coincidencias con IA, comunicación en tiempo real y entrega de notificaciones


<a name="_heading=h.1t7ntrnsbjve"></a>


