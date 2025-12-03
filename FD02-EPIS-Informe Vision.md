

` `**![C:\Users\EPIS\Documents\upt.png](media/Aspose.Words.c5692615-757d-4668-829d-d990d7c8af90.001.png)**




** 

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

` `**Desarrollo de Aplicativo Móvil “SOS Mascota”**

Curso: Calidad y Pruebas de Software



Docente: Mag. Patrick Cuadros Quiroga


Integrantes:

- Christian Dennis Hinojosa Mucho		(2019065161)
- Royser Alonsso Villanueva Mamani		(2021071090)
- Gilmer Donaldo Mamani Condori		(2012042779)




**Tacna – Perú**

**2025**













**Desarrollo de Aplicativo Móvil “SOS Mascota”**

**Documento de Visión** 

**Versión *2.0***



















|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|19/09/2025|Versión Original|
|2\.0|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|20/10/2025|Versión 2.0|

**ÍNDICE GENERAL**

[1. Introducción	5](#_heading=h.y1azpy1iwac)

[1.1. Propósito	5](#_heading=h.tyrt0o4h0b84)

[1.2. Alcance	5](#_heading=h.ozhpd5iokjj9)

[1.3. Definiciones, Siglas y Abreviaturas	5](#_heading=h.qy1d5tbw4oca)

[1.4. Referencias	6](#_heading=h.txgpv0ohid9b)

[1.5. Visión General	6](#_heading=h.h1hf8tco64iu)

[2. Posicionamiento	6](#_heading=h.ng4h9l8enf9g)

[2.1. Oportunidad de negocio	6](#_heading=h.s4m5v1rytiat)

[2.2. Definición del problema	7](#_heading=h.5my4m7ktjb43)

[3. Descripción de los interesados y usuarios	7](#_heading=h.162o29flh50r)

[3.1. Resumen de los interesados	7](#_heading=h.h15fbyhgm9dj)

[3.2. Resumen de los usuarios	8](#_heading=h.jqju5ftgvr3u)

[3.3. Entorno de usuario	8](#_heading=h.5d2pfaen4up)

[3.4. Perfiles de los interesados	9](#_heading=h.xhp1zvk9yx34)

[3.5. Perfiles de los usuarios	11](#_heading=h.w4y7odj1w5qq)

[3.6. Necesidades de los interesados y usuarios	13](#_heading=h.janhs8yf5eyd)

[4. Vista General del Producto	15](#_heading=h.4a7ljy3e6hp7)

[4.1. Perspectiva del producto	15](#_heading=h.3r4vb6lb95s)

[4.2. Resumen de capacidades	15](#_heading=h.zelv4d8mxq4q)

[4.3. Suposiciones y dependencias	16](#_heading=h.ktxbv59yq1f1)

[4.4. Costos y precios	16](#_heading=h.26c1xqfyz378)

[4.5. Licenciamiento e instalación	17](#_heading=h.w0tzua9ntuu8)

[5. Características del producto:	18](#_heading=h.dku4zdoeksbe)

[6. Restricciones	19](#_heading=h.ctufgdraswo8)

[7. Rangos de calidad	20](#_heading=h.kh4q5tsd6q1o)

[8. Precedencia y Prioridad:	21](#_heading=h.ogdgb0s7lwdc)

[9. Otros requerimientos del producto	23](#_heading=h.es4p6ez89j8k)

[Conclusiones	24](#_heading=h.y877zsku40fe)

[Recomendaciones	24](#_heading=h.oxjb80a35j4d)



































**Informe de Visión**
1. # <a name="_heading=h.y1azpy1iwac"></a>**Introducción**
   1. ## <a name="_heading=h.tyrt0o4h0b84"></a>**Propósito**
El propósito del proyecto es desarrollar una aplicación móvil llamada “SOS Mascota” que facilite la atención inmediata de mascotas en situación de riesgo mediante la conexión eficiente entre usuarios comunes y veterinarios. La aplicación busca promover la colaboración ciudadana para reportar, localizar y ayudar mascotas perdidas, en adopción o que necesitan asistencia, mejorando la comunicación, seguridad y rapidez en la respuesta. Además, se incorpora un rol administrativo para monitorear el uso y efectividad del sistema.
1. ## <a name="_heading=h.ozhpd5iokjj9"></a>**Alcance**
Este informe presenta el desarrollo y análisis del aplicativo móvil “Mascota SOS”. Se abordarán los siguientes puntos:

- Funcionalidades principales del sistema para usuarios comunes, veterinarios y administradores.
- Beneficios sociales y operativos del aplicativo para la atención de mascotas en situación de riesgo.
- Mecanismos de interacción y comunicación interna entre los usuarios y veterinarios.
- Aspectos de seguridad, privacidad y gestión de datos dentro de la aplicación.
- Resultados esperados en la mejora de la atención y rescate de mascotas a través del uso de la plataforma.

  1. ## <a name="_heading=h.qy1d5tbw4oca"></a>**Definiciones, Siglas y Abreviaturas**
- **SOS Mascota:** Aplicativo móvil diseñado para reportar, localizar y gestionar emergencias relacionadas con mascotas, facilitando la comunicación entre usuarios comunes, veterinarios y administradores.
- **Usuario:** Persona que utiliza la aplicación para reportar mascotas perdidas, en adopción o que necesitan ayuda, así como para comunicarse con veterinarios.
- **Veterinario:** Profesional registrado en la aplicación que brinda ayuda y atención especializada a las mascotas reportadas en situación de emergencia.
- **Administrador:** Usuario con permisos para visualizar estadísticas y monitorear el uso general de la aplicación para mejorar su gestión y funcionamiento.
- **Chat Interno:** Sistema de mensajería dentro de la aplicación que permite la comunicación privada entre usuarios y veterinarios sin compartir datos personales.
- **Geolocalización:** Función que permite identificar la ubicación exacta de las mascotas reportadas mediante mapas integrados en la aplicación.
  1. ## <a name="_heading=h.txgpv0ohid9b"></a>**Referencias**
Los documentos que se van a utilizar como referencia serán los siguientes:

- Documento de Especificación de Requerimientos – SRS 
- Documento de Arquitectura de Software – SAD
- Documento de Informe de Factibilidad
  1. ## <a name="_heading=h.h1hf8tco64iu"></a>**Visión General**
     Este documento describe el propósito, alcance, funcionalidades y limitaciones del aplicativo móvil “Mascota SOS”. Además, detalla los perfiles de los usuarios involucrados, usuarios comunes, veterinarios y administradores  y las capacidades necesarias para reportar, localizar y gestionar emergencias relacionadas con mascotas. El sistema busca facilitar la comunicación segura entre usuarios y profesionales veterinarios, integrando funciones como geolocalización, chat interno y gestión de reportes para mejorar la atención y protección de las mascotas.
1. # <a name="_heading=h.ng4h9l8enf9g"></a>**Posicionamiento**	
   1. ## <a name="_heading=h.s4m5v1rytiat"></a>**Oportunidad de negocio**


El desarrollo del aplicativo móvil “Mascota SOS” representa una oportunidad para cubrir la creciente necesidad de atención rápida y eficiente a mascotas en situación de emergencia, pérdida o adopción. Al facilitar la comunicación directa entre usuarios y veterinarios, así como la geolocalización de mascotas, la app puede posicionarse como una herramienta clave para comunidades, clínicas veterinarias y organizaciones de protección animal. Esto abre posibilidades de colaboración con entidades veterinarias, adopción responsable y empresas relacionadas, además de fomentar una comunidad activa comprometida con el bienestar animal.
1. ## <a name="_heading=h.5my4m7ktjb43"></a>**Definición del problema**
   Actualmente existe una falta de una plataforma eficiente y centralizada que permite reportar y gestionar mascotas perdidas, en adopción o que necesitan ayuda, lo que dificulta la comunicación rápida entre los usuarios afectados y los veterinarios encargados de brindar apoyo. Esta carencia limita la capacidad de atención oportuna, reduce las probabilidades de encontrar mascotas y dificulta la coordinación para brindar ayuda veterinaria, afectando el bienestar animal y la tranquilidad de los dueños.
1. # <a name="_heading=h.162o29flh50r"></a>**Descripción de los interesados y usuarios**
   1. ## <a name="_heading=h.h15fbyhgm9dj"></a>**Resumen de los interesados**

|Interesados|Representante|Papel|
| :-: | :-: | :-: |
|Royser Alonsso Villanueva Mamani|Jefe de proyecto|Responsable de la planificación, seguimiento y gestión general del proyecto.|
|Christian Dennis Hinojosa|Analista y programador|Responsable del análisis de requerimientos y desarrollo de funcionalidades clave del sistema.|
|Gilmer Donaldo Mamani Condori|Coordinador de pruebas|Responsable de la validación, pruebas y aseguramiento de calidad del proyecto|




1. ## <a name="_heading=h.xwzu3t2ph3lw"></a><a name="_heading=h.jqju5ftgvr3u"></a>**Resumen de los usuarios**

|Nombre|Descripción|
| :-: | :-: |
|Usuarios comunes|Personas que reportan mascotas perdidas, en adopción o que necesitan ayuda, y usan la app para buscar y comunicar la situación.|
|Veterinarios|Profesionales que atienden a las mascotas que necesitan ayuda, visualizan reportes específicos y coordinan la asistencia a través del chat.|
|Administradores|Usuarios encargados de monitorear las estadísticas de la aplicación y el uso, para optimizar y mejorar la plataforma.|

1. ## <a name="_heading=h.5d2pfaen4up"></a>**Entorno de usuario**
   La aplicación Mascota SOS estará dirigida a diferentes tipos de usuarios, incluyendo personas comunes que reportan y buscan mascotas, veterinarios que brindan atención y asistencia, y administradores que gestionan y supervisan el funcionamiento del sistema. Cada grupo interactúa con la aplicación según sus necesidades específicas para facilitar la comunicación, el seguimiento y la ayuda efectiva a las mascotas en situación de pérdida, adopción o emergencia.

1. ## <a name="_heading=h.xhp1zvk9yx34"></a>**Perfiles de los interesados**

|**Perfil de de Interesado**||
| - | :- |
|Representante|Royser Alonsso Villanueva Mamani |
|Descripción|Jefe de proyecto encargado de supervisar la gestión y avance del desarrollo de la aplicación Mascota SOS.|
|Tipo|Líder del proyecto|
|Responsabilidades|Supervisa el estado del proyecto y su manejo hasta la conclusión del mismo.|
|Criterios|El éxito es la finalización del proyecto dentro del tiempo estimado. También debe haber una percepción general del proyecto satisface las necesidades de todos los interesados.|
|Implicación|Revisor de requisitos y supervisor del desarrollo.|
|Entregables|Ninguno|



|**Perfil de Interesado**||
| - | :- |
|Representante|Christian Dennis Hinojosa|
|Descripción|Analistas y programadores responsables de diseñar y desarrollar las funcionalidades de la aplicación.|
|Tipo|Equipo de desarrollo|
|Responsabilidades|<p>Implementar módulos para usuarios (normales, veterinarios y administradores).</p><p>Garantizar la correcta comunicación y gestión de reportes, chats y perfiles.</p>|
|Criterios|<p>Código funcional y probado que cumpla con los requerimientos definidos.</p><p>Entrega oportuna de funcionalidades.</p>|
|Implicación|Desarrollo, pruebas y mantenimiento de la aplicación.|
|Entregables|Código fuente, documentación técnica y versiones funcionales de la app.|



|**Perfil de Interesado**||
| - | :- |
|Representante|Gilmer Donaldo Mamani Condori|
|Descripción|Coordinador de pruebas, responsable de la validación, pruebas y aseguramiento de calidad del proyecto.|
|Tipo|Control de calidad|
|Responsabilidades|<p>Planificar y ejecutar pruebas para garantizar el correcto funcionamiento del sistema.</p><p>Detectar y reportar errores o fallas en el aplicativo.</p><p>Verificar que se cumplan los requisitos de calidad establecidos.</p><p></p>|
|Criterios|<p>Detección oportuna de fallos.</p><p>Cumplimiento de estándares de calidad.</p>|
|Implicación|Evaluación continua y aseguramiento de calidad.|
|Entregables|Reportes de pruebas y validación, informe de calidad.|

1. ## <a name="_heading=h.w4y7odj1w5qq"></a>**Perfiles de los usuarios**

|**Perfil de Usuario**||
| - | :- |
|Representante|Usuarios comunes|
|Descripción|Personas que reportan mascotas perdidas, en adopción o que necesitan ayuda, y usan la app para buscar y comunicar la situación.|
|Tipo|Beneficiarios|
|Responsabilidades|<p>Reportar información veraz y actualizada sobre mascotas.</p><p>Utilizar la aplicación para buscar ayuda o dar seguimiento a casos.</p>|
|Criterios|<p>Facilidad de uso y acceso a la app.</p><p>Rapidez en la comunicación y respuesta.</p>|
|Implicación|Son los principales usuarios que demandan funcionalidades para reportar y buscar mascotas.|
|Entregables|Ninguna|


|**Perfil de Usuario**||
| - | :- |
|Representante|Veterinarios|
|Descripción|Profesionales que atienden a las mascotas que necesitan ayuda, visualizan reportes específicos y coordinan la asistencia a través del chat.|
|Tipo|Proveedores de servicio|
|Responsabilidades|<p>Revisar y atender los reportes de mascotas en situación de emergencia o adopción.</p><p>Coordinar con usuarios para brindar atención veterinaria adecuada.</p>|
|Criterios|<p>Precisión y oportunidad en la atención brindada.</p><p>Uso eficiente de las herramientas de comunicación.</p>|
|Implicación|Participan activamente en la resolución de casos reportados.|
|Entregables|Reportes de atención y seguimiento de casos.|


|**Perfil de Usuario**||
| - | :- |
|Representante|Administradores|
|Descripción|Usuarios encargados de monitorear las estadísticas de la aplicación y el uso, para optimizar y mejorar la plataforma.|
|Tipo|Administradores|
|Responsabilidades|<p>Supervisar el funcionamiento general de la app.</p><p>Analizar datos de uso para implementar mejoras.</p><p>Gestionar permisos y roles de usuarios.</p>|
|Criterios|<p>Eficiencia en la gestión y resolución de problemas.</p><p>Capacidad para interpretar estadísticas y tomar decisiones.</p>|
|Implicación|Aseguran la continuidad y mejora de la plataforma.|
|Entregables|Reportes estadísticos, actualizaciones del sistema.|

1. ## <a name="_heading=h.janhs8yf5eyd"></a>**Necesidades de los interesados y usuarios**

|**Necesidades**|**Prioridad**|**Inquietudes**|**Solución Actual**|**Solución Propuesta**|
| - | - | - | - | - |
|Permitir a los usuarios reportar mascotas perdidas o en adopción de forma rápida y sencilla.|Alta|Dificultad para comunicar y compartir información sobre mascotas en situación de riesgo.|Uso de grupos de Facebook, WhatsApp o carteles físicos con baja efectividad y alcance limitado.|Desarrollo de una app móvil que facilite reportes estructurados y geolocalizados para mejorar la visibilidad y respuesta..|
|Facilitar la comunicación entre usuarios y veterinarios para coordinar ayuda efectiva.|Alta|Falta de un canal directo y confiable para contactar profesionales y coordinar atención.|Mensajes dispersos en redes sociales o llamadas informales.|Implementación de un chat integrado en la app para comunicación directa y seguimiento..|
|Monitorear estadísticas y uso de la app para mejorar la atención a las mascotas y la experiencia de los usuarios.|Media|No existe un control o análisis formal sobre reportes, zonas con mayor incidencia o efectividad de respuestas.|Sin un sistema unificado de seguimiento.|Panel administrativo que permita visualizar métricas, gestionar reportes y optimizar recursos.|
|Generar confianza y seguridad para los usuarios al momento de reportar o adoptar.|Alta|Miedo a fraudes o información falsa que afecta la credibilidad del servicio.|Uso de plataformas abiertas sin controles ni verificación.|Incorporación de mecanismos de validación y moderación de reportes y usuarios en la app.|




1. # <a name="_heading=h.iinznoss8h7b"></a><a name="_heading=h.4a7ljy3e6hp7"></a>**Vista General del Producto**
   1. ## <a name="_heading=h.3r4vb6lb95s"></a>**Perspectiva del producto**
      La aplicación **SOS Mascota** se presenta como una solución innovadora para facilitar la comunicación y colaboración entre personas que reportan mascotas perdidas, en adopción o que necesitan ayuda, y profesionales veterinarios encargados de su atención. Esta plataforma móvil permitirá optimizar la búsqueda y cuidado de mascotas, aumentando la eficiencia en la gestión de reportes y promoviendo la adopción responsable. Además, al ofrecer un sistema confiable y fácil de usar, **SOS Mascota** contribuirá a fortalecer el compromiso social con el bienestar animal y facilitará la coordinación rápida entre usuarios y veterinarios, mejorando la calidad de vida de las mascotas en riesgo.	
   1. ## <a name="_heading=h.zelv4d8mxq4q"></a>**Resumen de capacidades**
- Reporte y Gestión de Incidencias: Capacidad para que los usuarios puedan registrar y describir situaciones relacionadas con mascotas perdidas, en adopción o que requieren ayuda, con un sistema intuitivo y accesible desde dispositivos móviles.
- Comunicación en Tiempo Real: Funcionalidad de chat integrado que permita la interacción directa entre los reportantes y los veterinarios, facilitando la coordinación rápida y eficiente de la atención y rescate de mascotas.
- Monitoreo y Estadísticas: Habilidad para recopilar y mostrar estadísticas sobre los reportes, adopciones y acciones realizadas dentro de la aplicación, permitiendo a los administradores evaluar el uso y efectividad de la plataforma para optimizar su funcionamiento.
- Integración con Geolocalización: Uso de tecnologías para mostrar la ubicación de los reportes y usuarios, facilitando la búsqueda y localización de mascotas en tiempo real.





1. ## <a name="_heading=h.ktxbv59yq1f1"></a>**Suposiciones y dependencias**

- Disponibilidad de Reportes de Usuarios: Se asume que los usuarios de la aplicación “SOS Mascota” reportará de manera frecuente y precisa las situaciones relacionadas con mascotas perdidas, en adopción o en riesgo, para mantener la información actualizada y útil.
- Acceso a Conectividad y Dispositivos Móviles: Se depende de que los usuarios cuenten con acceso a internet y dispositivos móviles compatibles para usar la aplicación y comunicarse en tiempo real con veterinarios y otros usuarios.
- Colaboración de Veterinarios: Se asume que los profesionales veterinarios estarán disponibles y activos en la plataforma para atender reportes, responder consultas y coordinar acciones de rescate o asistencia.
- Funcionalidad de Geolocalización: El correcto funcionamiento del sistema depende de que los dispositivos móviles permitan la geolocalización y que la app tenga acceso a esta información para facilitar la localización de mascotas.
- Mantenimiento y Actualización de la Plataforma: Se depende del soporte continuo y las actualizaciones periódicas de la aplicación para garantizar su estabilidad, seguridad y mejora funcional según el feedback de los usuarios.

1. ## <a name="_heading=h.26c1xqfyz378"></a>**Costos y precios**
   El proyecto “SOS Mascota” se basa en el desarrollo de una aplicación móvil utilizando tecnologías de código abierto, lo que permite minimizar los costos asociados a licencias de software. La inversión principal estará enfocada en el tiempo de diseño, desarrollo, pruebas y mantenimiento de la aplicación. Asimismo, se considerará una posible inversión futura en servicios de alojamiento en la nube para escalar el sistema.

   Para determinar la viabilidad financiera de “SOS Mascota”, todos los costos serán detallados y evaluados en el estudio de factibilidad correspondiente.





1. ## <a name="_heading=h.w0tzua9ntuu8"></a>**Licenciamiento e instalación**
   El software desarrollado para el proyecto **Sos Mascota** será de **código abierto**, permitiendo que otros desarrolladores, ONGs o instituciones educativas puedan mejorarlo o adaptarlo a otras realidades. Esta decisión busca fomentar la colaboración y la evolución continua de la aplicación, especialmente en el ámbito de la protección animal.

<a name="_heading=h.e26oed9sbssy"></a>**Requisitos de instalación**

Para garantizar el correcto funcionamiento del sistema, se deben cumplir los siguientes requisitos:

<a name="_heading=h.vdo4zdf7vs2"></a>**Hardware recomendado**

- **Procesador:** Intel Core i7/i9 o AMD Ryzen 7/9
- **Memoria RAM:** Mínimo 8 GB (recomendado 16 GB para un rendimiento óptimo)
- **Almacenamiento:** SSD de al menos 512 GB para velocidad y eficiencia
- **Conectividad:** Acceso estable a internet
- **Sistema operativo:** Windows 10/11, macOS, o distribuciones Linux compatibles con Flutter

<a name="_heading=h.umath7r5wapf"></a>**Software necesario**

- **Visual Studio Code (VS Code)** versión 1.98 o superior
- **Flutter SDK 3.x** o versión más actual
- **Dart SDK** (incluido con Flutter)
- **Firebase SDK**: Para funcionalidades de autenticación, almacenamiento en la nube y base de datos en tiempo real
- **Android SDK y emulador Android**: Para pruebas de la aplicación móvil
- **Google Maps API**: Para visualización de ubicaciones y reportes en tiempo real dentro de la app







1. # <a name="_heading=h.dku4zdoeksbe"></a>**Características del producto:**

   El sistema desarrollado **SOS Mascota** permitirá a los usuarios reportar, visualizar y recibir alertas sobre mascotas perdidas o encontradas en tiempo real, facilitando así la conexión entre dueños y rescatistas. Está diseñado para ser una herramienta accesible, intuitiva y eficiente para apoyar la protección y recuperación de mascotas en entornos urbanos.

   **Características principales:**

- Geolocalización en tiempo real
- Visualización de mascotas perdidas y encontradas en un mapa interactivo utilizando Google Maps API.
- Posicionamiento automático basado en la ubicación del dispositivo móvil del usuario.
- Filtros por tipo de mascota, fecha del reporte y ubicación.
- <a name="_heading=h.5bj7y2uhnvr2"></a> Publicación de reportes
- Los usuarios pueden publicar reportes con foto, descripción, ubicación y estado de la mascota.
- Clasificación como “Perdida” o “Encontrada”.
- Almacenamiento seguro de datos en Firebase Realtime Database y Firebase Storage para imágenes.
- <a name="_heading=h.u86ph0s1igsu"></a>Autenticación de usuarios
- Registro e inicio de sesión mediante correo electrónico y/o redes sociales, usando Firebase Authentication.
- Gestión segura de usuarios y control de reportes realizados por cada cuenta.
- <a name="_heading=h.kdv6ns1zholi"></a> Panel administrativo
- Acceso para moderadores o administradores donde pueden visualizar estadísticas de reportes, zonas más activas y usuarios más participativos.
- Herramientas para revisión y moderación de contenido publicado.
- <a name="_heading=h.1t0db6xdhbf"></a> Código abierto y escalable
- Desarrollo con Flutter y lenguaje Dart, permitiendo compatibilidad multiplataforma (Android e iOS).
- Licencia MIT, permitiendo su uso, modificación y mejora por parte de la comunidad o instituciones públicas.\
  Escalabilidad asegurada mediante servicios cloud de Firebase, adaptables a mayor volumen de usuarios y datos.


1. # <a name="_heading=h.ctufgdraswo8"></a>**Restricciones**
   El desarrollo y funcionamiento del sistema **Sos Mascota** está sujeto a ciertas limitaciones técnicas y operativas que pueden influir en su rendimiento y cobertura. A continuación, se detallan las principales restricciones del proyecto:

- Dependencia de servicios de terceros:\
  El sistema depende de servicios externos como Firebase, Google Maps API y Firebase Cloud Messaging, lo cual implica estar sujeto a cambios en sus políticas, disponibilidad o posibles costos futuros por uso extendido.
- Conectividad a Internet:\
  La funcionalidad del sistema (ubicación en tiempo real, almacenamiento, alertas) requiere acceso constante a Internet. Sin conexión, algunas funciones clave como el mapa o las notificaciones no estarán disponibles.
- Capacidad de almacenamiento y ancho de banda:\
  Aunque Firebase ofrece una cuota gratuita, existe un límite en la cantidad de imágenes, datos y transferencias por día. En caso de superar estos límites, podrían requerirse planes pagos.
- Precisión de la información ingresada por usuarios:\
  El sistema depende de la calidad y veracidad de los datos ingresados por los usuarios al reportar una mascota. Información incompleta o incorrecta puede dificultar el proceso de recuperación.
- Privacidad de los usuarios:\
  Se debe limitar la información personal mostrada públicamente para proteger la identidad de los usuarios, cumpliendo así con buenas prácticas de protección de datos.
- Cobertura geográfica limitada al inicio:\
  ` `En una primera etapa, el sistema estará disponible sólo en determinadas regiones, lo cual puede limitar su utilidad en zonas no cubiertas por los servicios de localización.

1. # <a name="_heading=h.kh4q5tsd6q1o"></a>**Rangos de calidad**
   Para asegurar que el sistema SOS Mascota funcione de manera eficiente, confiable y amigable para los usuarios, se han establecido los siguientes criterios de calidad que deben cumplirse durante el desarrollo y ejecución del sistema:

**Criterios de Calidad:**

Precisión en la localización y reporte de mascotas:

- El 95% de las ubicaciones geográficas de mascotas perdidas o encontradas deben coincidir correctamente con la dirección proporcionada por el usuario.
- El sistema validará los datos ingresados para evitar publicaciones duplicadas o con información incompleta.

Eficiencia en la carga y respuesta del sistema:

- La aplicación móvil debe cargar en menos de 3 segundos en conexiones estándar.
- El tiempo de respuesta al guardar o recuperar información desde Firebase no debe superar los 2 segundos.

Compatibilidad y escalabilidad:

- La aplicación debe ser totalmente funcional en dispositivos Android (versión 8.0 o superior) y tener compatibilidad proyectada para iOS.
- El diseño de la base de datos y la arquitectura del sistema deben permitir el crecimiento en número de usuarios y publicaciones sin afectar el rendimiento.

Usabilidad e interfaz de usuario:

- El sistema debe presentar una interfaz clara, intuitiva y adaptada para usuarios de diferentes edades.
- Se espera que al menos el 90% de los usuarios pueda completar un reporte de mascota en menos de 2 minutos, sin requerir asistencia técnica.

Disponibilidad del sistema:

- La disponibilidad del sistema debe ser del 99% mensual, asegurando que los usuarios puedan acceder a la plataforma en cualquier momento.

1. # <a name="_heading=h.ogdgb0s7lwdc"></a>**Precedencia y Prioridad:**
   El desarrollo del sistema **SOS Mascota** se organizará por etapas prioritarias que aseguren la funcionalidad base y progresiva del sistema, priorizando las necesidades fundamentales de los usuarios:

   <a name="_heading=h.ero6ugcl0wr8"></a>**Registro y Autenticación de Usuarios (Alta prioridad):**

- Es el primer paso necesario para asegurar que solo usuarios verificados puedan publicar y buscar mascotas.
- Este módulo incluye el registro, inicio de sesión y validación con Firebase Authentication.

<a name="_heading=h.d8obk0khxzqw"></a>**Publicación y Búsqueda de Mascotas (Alta prioridad):**

- Una vez autenticado, el usuario debe poder publicar reportes de mascotas perdidas o encontradas, y buscar en el sistema según ubicación, tipo de mascota o características.
- Este módulo es esencial para cumplir con el propósito principal del sistema.

<a name="_heading=h.yh96d9hm34za"></a>**Geolocalización y Visualización en Mapa (Alta prioridad):**

- Usando Google Maps API, los reportes deben mostrarse en un mapa interactivo.
- Este componente permite a los usuarios visualizar dónde se extraviaron o encontraron mascotas, agilizando la búsqueda.

<a name="_heading=h.xbg8duzgar96"></a>**Notificaciones y Comunicación entre Usuarios (Media prioridad):**

- Permite el contacto entre quien encuentra y quien busca una mascota mediante mensajería o alertas.
- Mejora la efectividad del sistema, aunque puede implementarse después de las funciones básicas.

<a name="_heading=h.8dvp9yrd1l2k"></a>**Gestión de Imágenes y Almacenamiento (Media prioridad):**

- Las fotos de mascotas serán almacenadas en Firebase Storage, acompañando la publicación.
- Este módulo complementa la funcionalidad básica, y es vital para la identificación visual de las mascotas.

<a name="_heading=h.aubj3hmy77ke"></a>**Panel de Administración y Moderación (Baja prioridad):**

- Este módulo permitirá a los administradores gestionar contenido, resolver reportes y eliminar publicaciones inapropiadas.
- Aunque importante, puede añadirse en fases posteriores cuando el sistema tenga un volumen considerable de usuarios.
1. # <a name="_heading=h.es4p6ez89j8k"></a>**Otros requerimientos del producto**
1. **Estándares legales:**
- El sistema cumplirá con las normativas de protección de datos personales (como la Ley N° 29733 - Ley de Protección de Datos Personales en Perú), garantizando el consentimiento explícito del usuario para el uso de su información.
- Se incluirán términos y condiciones de uso, así como una política de privacidad clara dentro de la app, informando sobre el tratamiento de datos y responsabilidades.
1. **Estándares de comunicación:**
- La aplicación debe permitir una comunicación efectiva y segura entre los usuarios mediante formularios internos o mensajes vinculados a correos electrónicos verificados.
1. **Estándares de cumplimiento de la plataforma:**
- La app seguirá las guías de diseño y publicación de Google Play Store y, si se amplía a iOS, las de la App Store.
- El código será compatible con Flutter SDK, asegurando el correcto despliegue en Android y potencialmente en iOS.
1. **Estándares de calidad y seguridad:**
- Autenticación segura mediante Firebase Authentication con protección contra accesos no autorizados.
- Verificación y validación de entradas de usuario para evitar inyecciones de código o información falsa.
- Imágenes y archivos serán verificados antes del almacenamiento, previniendo contenido malicioso.
- Se establecerá un protocolo básico de respaldo de datos y recuperación.
1. **Estándares de escalabilidad:**

   El uso de Firebase (Realtime Database o Firestore) garantiza una escalabilidad automática conforme aumenta el número de usuarios y publicaciones.

   El sistema se diseñará con una arquitectura modular, facilitando futuras integraciones como:

- Sistema de recompensas o donaciones.
- Estadísticas de mascotas recuperadas.
- Integración con veterinarias u organizaciones de rescate.
# <a name="_heading=h.y877zsku40fe"></a>**Conclusiones**
El desarrollo del sistema “SOS Mascota” permitió evidenciar la necesidad de una solución tecnológica que facilite la publicación y localización de mascotas perdidas o encontradas, optimizando la comunicación entre dueños, rescatistas y la comunidad en general. Gracias al uso de Flutter y Firebase, se logró crear una aplicación móvil multiplataforma, escalable y en tiempo real, capaz de gestionar datos con geolocalización, imágenes y validación efectiva. Esta herramienta no solo mejora las posibilidades de reencuentro entre mascotas y dueños, sino que también sienta las bases para futuras integraciones con organizaciones animalistas, sistemas de notificación por zonas y campañas de adopción, consolidando a “Sos Mascota” como una plataforma útil, segura y con gran potencial de impacto social.
# <a name="_heading=h.oxjb80a35j4d"></a>**Recomendaciones**
Se recomienda ampliar la funcionalidad del sistema “SOS Mascota” integrando un sistema de notificaciones por geolocalización que alerte a los usuarios cercanos cuando se publique una mascota perdida o encontrada. Asimismo, se sugiere establecer alianzas con veterinarias, refugios y municipalidades para validar publicaciones y aumentar el alcance de la aplicación. Es importante fomentar el uso responsable de la plataforma mediante campañas educativas y moderación de contenido, garantizando que la información publicada sea veraz. También se aconseja implementar un panel web administrativo para facilitar el monitoreo y análisis estadístico de los casos reportados, lo cual permitirá mejorar continuamente el servicio y promover futuras actualizaciones orientadas a la adopción y cuidado responsable de animales.


