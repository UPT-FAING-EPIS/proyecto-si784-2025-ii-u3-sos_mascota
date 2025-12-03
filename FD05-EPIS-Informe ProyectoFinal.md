![C:\Users\EPIS\Documents\upt.png](media/Aspose.Words.20456956-1597-43d8-946f-e8968acd9e1b.001.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**INFORME FINAL**


**Desarrollo de Aplicativo Móvil “SOS Mascota”**

Curso: Calidad y Pruebas de Software


Docente: Mag. Patrick Cuadros Quiroga


Integrantes:

- Christian Dennis Hinojosa Mucho		(2019065161)
- Royser Alonsso Villanueva Mamani		(2021071090)
- Gilmer Donaldo Mamani Condori		(2012042779)



**Tacna – Perú**

**2025**

















**Desarrollo de Aplicativo Móvil “SOS Mascota”** 

**Informe Final**

**Versión 2.0**





|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|19/09/2025|Versión Original|
|2\.0|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|Christian HInjosa<br>Royser Villanueva|20/10/2025|Versión 2.0|













# <a name="_p083twdhr3cs"></a>**ÍNDICE GENERAL**



[1.](#_5gzokml7z06t)[	](#_5gzokml7z06t)[Antecedentes	4](#_5gzokml7z06t)

[2.](#_m988zbpbrja6)[	](#_m988zbpbrja6)[Planteamiento del Problema	5](#_m988zbpbrja6)

[a.](#_6xsnyp31an9r)[	](#_6xsnyp31an9r)[Problema	5](#_6xsnyp31an9r)

[b.	Justificación	6](#_9u5nvf6m5z6q)

[c.	Alcance	6](#_4q7o6arhgp6i)

[3.](#_deb0ufvd2noh)[	](#_deb0ufvd2noh)[Objetivos	7](#_deb0ufvd2noh)

[4.](#_ryknecycrwzo)[	](#_ryknecycrwzo)[Marco Teórico	8](#_ryknecycrwzo)

[5.](#_ppkt7sv1nk6l)[	](#_ppkt7sv1nk6l)[Desarrollo de la Solución	9](#_ppkt7sv1nk6l)

[a.](#_sk9086tgh3vg)[	](#_sk9086tgh3vg)[Análisis de Factibilidad (técnico, económica, operativa, social, legal, ambiental)	10](#_sk9086tgh3vg)

[Factibilidad Operativa	10](#_muc18fr8a4x5)

[Factibilidad Legal	10](#_1upakaij9f5s)

[b.](#_2f2v5y52cxv6)[	](#_2f2v5y52cxv6)[Tecnología de Desarrollo	12](#_2f2v5y52cxv6)

[c.](#_7k5xxe2coxky)[	](#_7k5xxe2coxky)[Metodología de implementación	13](#_7k5xxe2coxky)

[6.](#_ymwbrq8l0we1)[	](#_ymwbrq8l0we1)[Cronograma	15](#_ymwbrq8l0we1)

[7.](#_bqdd5wig7vu2)[	](#_bqdd5wig7vu2)[Presupuesto	16](#_bqdd5wig7vu2)

[Costos de personal	17](#_7vcyahrw3tzm)

[8.](#_tdx8m4k4y37)[	](#_tdx8m4k4y37)[Conclusiones	19](#_tdx8m4k4y37)

[Recomendaciones	20](#_ni4wztch4r2r)

[Bibliografía	21](#_1j3tiojmefc)

[Anexos	22](#_s4027o7vc467)









1. # <a name="_5gzokml7z06t"></a>**Antecedentes**
El desarrollo del Aplicativo móvil para la gestión efectiva y localización de mascotas perdidas mediante un sistema colaborativo de voluntarios surge como respuesta a la creciente problemática de pérdida de mascotas y la necesidad de mejorar los métodos de localización y gestión de reportes en entornos urbanos. En los últimos años, tanto en comunidades locales como en plataformas digitales, se ha evidenciado la importancia de contar con herramientas que permitan a los dueños y voluntarios registrar, organizar y dar seguimiento a los casos de mascotas extraviadas de manera eficiente y colaborativa.

Experiencias previas en aplicaciones de rescate animal y plataformas de adopción han adoptado sistemas móviles y web para gestionar la información, usando bases de datos centralizadas y notificaciones en tiempo real para agilizar la localización. Sin embargo, la transición desde métodos tradicionales, como anuncios físicos, llamadas telefónicas o publicaciones en redes sociales, hacia sistemas móviles especializados ha presentado desafíos relacionados con la confiabilidad de la información, la participación de voluntarios y la trazabilidad de los reportes.

La evolución de tecnologías móviles, la geolocalización y los sistemas colaborativos ha abierto nuevas posibilidades para gestionar y mejorar la interacción entre usuarios, voluntarios y administradores. Algunos proyectos previos han demostrado que la integración de estas tecnologías puede facilitar la colaboración, la rapidez en la localización de mascotas y el registro de datos históricos, estableciendo así bases sólidas para soluciones más eficientes adaptadas a las necesidades actuales de la comunidad.

Por otro lado, las lecciones aprendidas de iniciativas similares han resaltado la importancia de aspectos como la escalabilidad, la interoperabilidad con dispositivos móviles y la adopción de estándares abiertos para el intercambio de información. Estos antecedentes han influido directamente en el diseño del sistema propuesto, que busca no solo resolver las limitaciones técnicas y logísticas existentes, sino también fomentar la participación comunitaria, el registro confiable de reportes y la colaboración efectiva entre usuarios y voluntarios, preparando a los involucrados para un entorno digital más eficiente y organizado.








1. # <a name="_m988zbpbrja6"></a>**Planteamiento del Problema**
En el ámbito urbano y comunitario, la pérdida de mascotas representa un problema creciente que afecta tanto a los dueños como a las organizaciones de rescate animal. La gestión de reportes de mascotas perdidas y la coordinación de voluntarios se ve limitada por la falta de plataformas integrales que permitan registrar, localizar y dar seguimiento a los casos de manera eficiente y colaborativa.

Uno de los principales desafíos identificados es la ausencia de un sistema que centralice la información de mascotas extraviadas, permitiendo a los usuarios reportar pérdidas, a los voluntarios localizar mascotas mediante geolocalización y al administrador mantener un control preciso sobre los reportes. Actualmente, los dueños deben recurrir a redes sociales, llamadas telefónicas o avisos físicos, lo que genera desorganización, duplicación de información y retrasos en la recuperación de las mascotas.

Además, la falta de herramientas que estructuren los reportes y permitan notificaciones en tiempo real limita la capacidad de los usuarios y voluntarios para actuar con rapidez. Esta carencia afecta directamente la efectividad de la localización y reduce la participación de la comunidad en los procesos de rescate.

La gestión de cuentas y reportes representa otro aspecto crítico. La inexistencia de funcionalidades que permitan a los usuarios y voluntarios visualizar historiales de reportes, acceder a casos previos o actualizar información sobre la localización de mascotas limita la trazabilidad y dificulta la coordinación entre los actores involucrados.

Finalmente, desde la perspectiva de seguridad y confianza, es esencial proteger los datos de los usuarios y la información de las mascotas. La falta de mecanismos de autenticación segura y control de acceso puede generar desconfianza en la plataforma y comprometer su adopción como una solución confiable para la gestión de mascotas perdidas.

1. # <a name="_6xsnyp31an9r"></a>**Problema**

El proyecto surge como respuesta a una problemática creciente en la comunidad: la falta de herramientas integrales que permitan la gestión efectiva de reportes de mascotas perdidas, facilitando su localización y promoviendo la colaboración entre voluntarios. Esta carencia afecta la recuperación de mascotas, la organización de la información y la participación de la comunidad.

- Reporte manual ineficiente: Actualmente, los dueños de mascotas deben recurrir a redes sociales, avisos físicos o llamadas telefónicas para informar sobre la pérdida, lo que consume tiempo, genera duplicación de información y dificulta la coordinación de los rescates.
- Ausencia de seguimiento estructurado: No existen herramientas que permitan organizar los reportes de manera clara, con notificaciones automáticas y geolocalización de mascotas, lo que limita la capacidad de los voluntarios para actuar rápidamente y reduce la efectividad en la recuperación.
- Falta de trazabilidad y control de casos: No hay un sistema que registre los historiales de reportes, cambios de estado de las mascotas o actualizaciones de localización. Esto dificulta la coordinación y el seguimiento de los casos a lo largo del tiempo.
- Limitada gestión de cuentas y participación: Los usuarios y voluntarios no cuentan con funcionalidades para administrar sus reportes, actualizar información sobre mascotas o monitorear el progreso de los casos, lo que reduce la organización y la eficiencia del sistema colaborativo.
- Riesgos de seguridad y privacidad: La ausencia de mecanismos de autenticación segura y control de acceso a la información de usuarios y mascotas genera desconfianza y puede afectar la adopción del sistema como herramienta confiable para la comunidad.
  1. ### <a name="_9u5nvf6m5z6q"></a>**Justificación**
La justificación del presente proyecto se basa en la necesidad creciente de la comunidad de contar con herramientas digitales que permitan gestionar de manera eficiente y segura los reportes de mascotas perdidas, optimizando su localización y promoviendo la colaboración entre voluntarios. La pérdida de mascotas es un problema frecuente que genera estrés en los dueños y dificulta la coordinación de esfuerzos para su recuperación, evidenciando la necesidad de un sistema centralizado y accesible.

Actualmente, los dueños de mascotas dependen de métodos tradicionales como avisos físicos, llamadas telefónicas o publicaciones en redes sociales, los cuales son ineficientes, desorganizados y poco confiables. Esto limita la capacidad de los voluntarios para actuar de manera oportuna y coordinar esfuerzos de rescate, afectando directamente la efectividad en la recuperación de mascotas.

El proyecto responde a la necesidad de superar estas limitaciones mediante un aplicativo móvil que permita reportar la pérdida de una mascota de manera rápida y estructurada, integrando funcionalidades como geolocalización, notificaciones automáticas y seguimiento de casos. Al centralizar la información y automatizar procesos, se mejora la coordinación entre voluntarios y se facilita la comunicación directa con los dueños.

Una característica clave de este proyecto es la incorporación de un sistema colaborativo que registra el historial de reportes, actualizaciones de estado de las mascotas y participación de voluntarios. Esto no solo mejora la trazabilidad de cada caso, sino que también fomenta la cultura de cooperación y responsabilidad dentro de la comunidad.

Además, la seguridad y protección de la información son aspectos esenciales. El aplicativo contará con mecanismos de autenticación segura, gestión de cuentas y protección de datos personales de los usuarios y mascotas, garantizando la confiabilidad del sistema y el respeto a la privacidad de los involucrados.

En síntesis, el proyecto busca brindar una solución tecnológica que facilite la recuperación de mascotas perdidas, mejore la organización de reportes, fortalezca la colaboración comunitaria y promueva buenas prácticas en la gestión de información, contribuyendo al bienestar de la sociedad y de los animales.
1. ### <a name="_4q7o6arhgp6i"></a>**Alcance**
El alcance del proyecto del Aplicativo Móvil para la Gestión y Localización de Mascotas Perdidas se fundamenta en la necesidad de contar con una herramienta digital accesible, eficiente y confiable que permita a los dueños de mascotas y voluntarios coordinar acciones de manera efectiva. En un contexto donde la pérdida de mascotas es frecuente y requiere respuestas rápidas, se busca ofrecer un sistema que centralice la información y facilite la colaboración comunitaria.

Este aplicativo permitirá a los usuarios registrar la pérdida de una mascota, incluir detalles como descripción, fotos y ubicación geográfica, y notificar automáticamente a voluntarios registrados en la zona. Al centralizar y estructurar la información, se optimiza la coordinación de esfuerzos y se mejora la probabilidad de recuperación de los animales.

El proyecto incluye funcionalidades clave para mejorar la experiencia del usuario y la efectividad del sistema, tales como:

- Geolocalización en tiempo real para identificar áreas de búsqueda y reportes de mascotas perdidas.
- Historial de reportes y seguimiento de cada caso, permitiendo a los usuarios y voluntarios consultar el estado de recuperación de las mascotas.
- Sistema de notificaciones automáticas para mantener informados a voluntarios y dueños sobre eventos relevantes, como avistamientos o avances en la búsqueda.
- Gestión de cuentas y seguridad, incluyendo autenticación segura, control de acceso y protección de datos personales de los usuarios y mascotas.

El alcance también abarca la promoción de la colaboración comunitaria, incentivando la participación de voluntarios mediante un sistema confiable y fácil de usar. La plataforma está diseñada para ser accesible desde dispositivos móviles, garantizando que los usuarios puedan reportar y recibir información en cualquier momento y lugar. En resumen, este proyecto proporciona una solución tecnológica integral que mejora la organización y eficacia de los esfuerzos de recuperación de mascotas perdidas, fomenta la cooperación entre voluntarios y dueños, y garantiza la seguridad y confiabilidad de la información, contribuyendo al bienestar de la comunidad y de los animales.
1. # <a name="_deb0ufvd2noh"></a>**Objetivos**
**Objetivo Principal:**

Diseñar e implementar un aplicativo móvil que permita la gestión eficiente y localización de mascotas perdidas, facilitando la coordinación entre dueños y voluntarios a través de un sistema colaborativo y seguro.

Objetivos Específicos:

- Registrar y gestionar reportes de mascotas perdidas: Desarrollar un módulo que permita a los usuarios ingresar información detallada sobre las mascotas desaparecidas, incluyendo fotos, descripción y ubicación geográfica.
- Implementar geolocalización en tiempo real: Permitir a los usuarios y voluntarios visualizar áreas de búsqueda y reportes recientes, optimizando las acciones de recuperación.
- Sistema de notificaciones automáticas: Mantener informados a los usuarios y voluntarios sobre avances, avistamientos o nuevos reportes en su área de interés.
- Garantizar la seguridad y privacidad de los datos: Implementar autenticación segura, control de accesos y protección de la información personal de usuarios y mascotas.

1. # <a name="_ryknecycrwzo"></a>**Marco Teórico**
El desarrollo del presente sistema se sustenta en diversos conceptos teóricos que permiten comprender la necesidad, el enfoque y la viabilidad de implementar un aplicativo móvil para la gestión efectiva y localización de mascotas perdidas mediante un sistema colaborativo de voluntarios. Estos fundamentos abarcan desde aspectos tecnológicos hasta sociales y de gestión de la información.

**4.1 Gestión de Mascotas y Participación Comunitaria**

La gestión de mascotas perdidas requiere un enfoque organizado y colaborativo, donde los dueños, vecinos y voluntarios puedan interactuar de manera efectiva. Según estudios de la ASPCA (American Society for the Prevention of Cruelty to Animals), la rapidez en la localización de mascotas perdidas aumenta significativamente las probabilidades de recuperación. La participación comunitaria mediante plataformas digitales permite coordinar esfuerzos, compartiendo información de manera inmediata y estructurada. Este enfoque fomenta la responsabilidad social y fortalece los lazos comunitarios en torno al cuidado de los animales.




**4.2 Geolocalización y Sistemas de Información Geográfica (SIG)**

La geolocalización es fundamental para ubicar y rastrear mascotas perdidas en tiempo real. Los sistemas de información geográfica (SIG) aplicados en dispositivos móviles permiten mapear avistamientos, definir áreas de búsqueda y optimizar rutas de rescate. La integración de GPS en los smartphones y la conectividad en tiempo real facilita que los voluntarios reciban alertas inmediatas sobre la ubicación de mascotas, mejorando la eficiencia en las búsquedas.

**4.3 Aplicativos Móviles y Notificaciones en Tiempo Real**

Los aplicativos móviles constituyen la herramienta principal para la interacción entre usuarios y voluntarios. La implementación de notificaciones push y alertas en tiempo real asegura que los usuarios estén informados de manera inmediata sobre nuevos reportes, avistamientos o actualizaciones en el estado de la búsqueda. Este enfoque mejora la coordinación y la capacidad de respuesta, incrementando la probabilidad de éxito en la localización de mascotas.

**4.4 Bases de Datos en la Nube y Gestión de Información**

El almacenamiento seguro y centralizado de datos es clave para garantizar la disponibilidad y trazabilidad de la información sobre mascotas y reportes de usuarios. Las bases de datos en la nube permiten manejar grandes volúmenes de información de manera escalable, asegurando la integridad de los datos y la accesibilidad desde múltiples dispositivos. La gestión eficiente de la información facilita el registro histórico de reportes y la recuperación rápida de información relevante para cada caso.

**4.5 Seguridad y Privacidad de Datos**

La protección de datos personales y la información sensible relacionada con las mascotas son aspectos críticos del sistema. La implementación de mecanismos de autenticación, control de accesos y sesiones seguras garantiza la confidencialidad y evita el uso indebido de la información. El cumplimiento de normas locales e internacionales, como la Ley de Protección de Datos Personales en Perú (Ley N° 29733), asegura que el sistema opere bajo estándares confiables de seguridad.




**4.6 Experiencia de Usuario y Usabilidad**

El diseño centrado en el usuario (DCU) y los principios de usabilidad son esenciales para que la plataforma sea intuitiva y accesible. Al enfocarse en la simplicidad, claridad y facilidad de navegación, el aplicativo móvil permite que usuarios de distintas edades y niveles técnicos puedan reportar mascotas perdidas, colaborar en búsquedas y consultar información sin dificultades. Una buena experiencia de usuario incrementa la participación de voluntarios y promueve la efectividad del sistema.
1. # <a name="_ppkt7sv1nk6l"></a>**Desarrollo de la Solución**

`	`*Tabla 01. Cuadro del Desarrollo de la Solución*
#
|1. El desarrollo del aplicativo móvil para la gestión efectiva y localización de mascotas perdidas mediante un sistema colaborativo de voluntarios se estructura mediante el uso de herramientas y tecnologías modernas que garantizan una plataforma funcional, segura y con una experiencia de usuario optimizada.|
| - |
|2. En el backend, se ha utilizado Node.js con el framework Express, que permite gestionar de manera eficiente la lógica de negocio, la autenticación de usuarios, la gestión de reportes de mascotas y la coordinación de voluntarios. Express facilita la implementación de arquitecturas limpias, como el patrón Modelo-Vista-Controlador (MBBM), adoptado en este proyecto para mantener una estructura clara, escalable y mantenible.|
|3. El sistema utiliza Firebase como base de datos en la nube, lo que proporciona almacenamiento en tiempo real, sincronización eficiente entre dispositivos y escalabilidad automática para manejar múltiples reportes y usuarios. Firebase permite integrar módulos como Firestore para la gestión de información de mascotas, Authentication para control de usuarios y Cloud Messaging para notificaciones en tiempo real. La estructura del backend se organiza en carpetas como controllers, models y services, asegurando modularidad y facilidad de mantenimiento.|
|4. En cuanto al frontend, se desarrolló la aplicación utilizando Flutter, un framework que permite construir aplicaciones móviles multiplataforma con interfaces atractivas, responsivas y consistentes en Android e iOS. Flutter facilita la integración con servicios de backend, como Firebase, y permite implementar funcionalidades clave como geolocalización, notificaciones push y visualización de reportes en mapas interactivos.|
|5. La interfaz gráfica se diseña con un enfoque centrado en el usuario, garantizando que los reportes de mascotas, las alertas de avistamiento y las opciones de colaboración para voluntarios sean intuitivas y fáciles de usar. Se incorporan componentes interactivos como listas dinámicas de mascotas reportadas, filtros por ubicación y mapas georreferenciados para optimizar la experiencia del usuario.|
|6. El entorno de desarrollo se gestiona desde Visual Studio Code, que ofrece herramientas para depuración, pruebas y despliegue eficiente del proyecto, así como extensiones útiles para Flutter y Firebase, lo que permite un flujo de trabajo ágil y organizado.|
|7. La solución adopta una arquitectura cliente-servidor, donde el móvil actúa como cliente y Firebase/Express como backend, facilitando el mantenimiento, la escalabilidad y la coordinación entre usuarios. La plataforma está diseñada para operar en la nube, garantizando disponibilidad, seguridad y sincronización en tiempo real de los reportes y las alertas de mascotas perdidas. Además, se implementan mecanismos de autenticación y control de acceso para proteger la información sensible de los usuarios y asegurar la integridad de los datos registrados.|

*Fuente: Elaboración Propia*


1. # <a name="_sk9086tgh3vg"></a>**Análisis de Factibilidad (técnico, económica, operativa, social, legal, ambiental)**

La factibilidad económica del proyecto se fundamenta en los costos asociados al desarrollo, implementación y mantenimiento del aplicativo. Los principales rubros incluyen: licencias de software (en su mayoría gratuitas por el uso de herramientas open source como Android Studio y Firebase), servicios en la nube para almacenamiento y mensajería, pruebas en dispositivos móviles y capacitación a los voluntarios para el uso de la aplicación. Además, se realizará un análisis de Retorno de Inversión (ROI) considerando los beneficios de mediano y largo plazo, como la optimización de recursos, la reducción de tiempos en la búsqueda de mascotas y el impacto positivo en la comunidad. Esto garantiza que el proyecto sea sostenible financieramente y genere valor social y académico.





## <a name="_muc18fr8a4x5"></a>**Factibilidad Operativa**

El aplicativo móvil está diseñado para optimizar el proceso de búsqueda y localización de mascotas perdidas, facilitando la colaboración activa entre dueños y voluntarios. Su interfaz será intuitiva, permitiendo que cualquier usuario, sin conocimientos técnicos avanzados, pueda reportar o buscar una mascota rápidamente.

*Tabla 02. Cuadro de Factibilidad Operativa*

|Beneficios del sistema|Contexto|
| - | - |
|Automatización de reportes|<p>Publicación inmediata de mascotas perdidas o encontradas con ubicación en tiempo real.</p><p></p>|
|Optimización de recursos|<p>Centralización de la información en una sola plataforma móvil.</p><p></p>|
|Accesibilidad y usabilidad|<p>Interfaz sencilla, diseñada para el uso cotidiano de los ciudadanos.</p><p></p>|
|Reducción de costos operativos|Al eliminar la necesidad de carteles impresos o campañas físicas, se disminuyen gastos para los dueños.|
|Compatibilidad y escalabilidad|<p>El sistema podrá ampliarse en el futuro, incorporando funciones como reconocimiento por imagen o historial de casos resueltos.</p><p></p>|

*Fuente: Elaboración Propia*

## <a name="_1upakaij9f5s"></a>**Factibilidad Legal**
El desarrollo del aplicativo deberá cumplir con la Ley de Protección de Datos Personales (Ley N° 29733, Perú), garantizando que la información de los usuarios (nombre, contacto, ubicación) sea almacenada y tratada de manera confidencial.

Principales regulaciones a considerar:






*Tabla 03. Cuadro de Factibilidad Legal*

|Ley de Protección de Datos Personales (LPDP)|<p>Uso de protocolos de seguridad y cifrado para evitar accesos no autorizados.</p><p></p>|
| - | - |
|Derechos de autor e imágenes|<p>Los usuarios deberán aceptar términos y condiciones que aseguren que las fotos de mascotas subidas sean legítimas.</p><p></p>|
|Normativas de seguridad informática|Implementación de autenticación mediante correo o redes sociales.|
|Uso responsable de la información|El sistema se enfocará exclusivamente en fines sociales y de rescate, evitando usos indebidos.|

*Fuente: Elaboración Propia*

No se identifican restricciones legales que impidan la implementación del sistema, siempre y cuando se cumpla con estas regulaciones y se implementen mecanismos de** cumplimiento normativo para asegurar que el sistema opere dentro del marco legal de Perú.

**Factibilidad Social**

*Tabla 04. Cuadro de Factibilidad Social*

El impacto social es altamente positivo, ya que el aplicativo fortalece la unión comunitaria en torno a la causa animalista.

|<p>**Accesibilidad y democratización**</p><p></p>|<p>Herramienta gratuita y disponible para cualquier persona con un celular Android.</p><p></p>|
| - | - |
|<p>**Fomento del voluntariado digital**</p><p></p>|<p>Se crea una red de apoyo comunitario activa y solidaria.</p><p></p>|
|<p>**Impacto en la comunidad**</p><p></p>|Se reduce la angustia de familias al facilitar la localización de sus mascotas.|
|<p>**Ética y buenas prácticas**</p><p></p>|Se promueve un uso responsable del aplicativo, fomentando la colaboración y la transparencia en la información compartida.|

*Fuente: Elaboración Propia*

**Factibilidad Ambiental**

El proyecto tiene un impacto ambiental positivo, ya que promueve la digitalización en lugar de medios tradicionales como carteles impresos o campañas en papel.

*Tabla 05. Cuadro de Factibilidad Ambiental*

|**Reducción del Uso de Papel**|Al usar medios digitales, se evita la impresión masiva de afiches.|
| - | - |
|**Eficiencia Energética**|<p>El uso de servicios en la nube optimiza recursos frente a procesos manuales.</p><p></p><p></p>|
|**Impacto en la Huella de Carbono**|<p>Menor necesidad de desplazamientos físicos para compartir información.</p><p></p>|
|**Gestión digital eficiente**|<p>El almacenamiento en la nube evita duplicidad de información y optimiza recursos tecnológicos.</p><p></p>|
|**Conciencia ambiental**|<p>Se sensibiliza a los usuarios sobre la importancia de emplear herramientas tecnológicas sostenibles.</p><p></p>|

*Fuente: Elaboración Propia*

1. # <a name="_2f2v5y52cxv6"></a>**Tecnología de Desarrollo**

El desarrollo del Aplicativo móvil para la gestión efectiva y localización de mascotas perdidas mediante un sistema colaborativo de voluntarios se basa en un conjunto de tecnologías modernas que garantizan una plataforma segura, escalable y accesible para los usuarios. Estas tecnologías permiten centralizar reportes, facilitar la colaboración comunitaria y optimizar la búsqueda de mascotas en tiempo real.







*Tabla 06. Cuadro de Tecnología de Desarrollo*

|<p>**Arquitectura de Estilo: Cliente–Servidor**</p><p></p>|<p>Se adopta una arquitectura cliente-servidor en la que el dispositivo móvil actúa como cliente y se comunica con un backend alojado en la nube. Este diseño permite la sincronización en tiempo real de los reportes y garantiza la disponibilidad del servicio desde cualquier ubicación.</p><p></p>|
| - | - |


|<p>**Patrón de Diseño: Modelo–Vista–Controlador (MBBM)**</p><p></p>|<p>La aplicación se organiza siguiendo el patrón MBBM, separando la lógica de negocio, la gestión de datos y la interfaz de usuario. Esto facilita la escalabilidad del sistema, la mantenibilidad del código y la claridad en la interacción entre módulos.</p><p></p>|
| - | - |

|<p>**Flutter**</p><p></p>|El frontend del aplicativo móvil se desarrolla con Flutter, orientado exclusivamente a Android. Este framework permite crear interfaces modernas, intuitivas y consistentes, además de facilitar la integración con mapas interactivos, notificaciones en tiempo real y módulos de geolocalización.|
| - | - |

|<p>**Node.js y Express**</p><p></p>|<p>En el backend se emplea Node.js con el framework Express, que gestiona la lógica de negocio, la autenticación de usuarios y la administración de reportes. Este entorno ligero y eficiente permite un alto rendimiento en la comunicación cliente-servidor.0</p><p></p>|
| - | - |




|<p>**Firebase**</p><p></p>|<p>El sistema utiliza Firebase como base de datos en la nube y motor de servicios complementarios:</p><p>- Firestore para el almacenamiento y sincronización en tiempo real de reportes.</p><p>- Authentication para la gestión segura de cuentas de usuarios y voluntarios.</p><p>- Cloud Messaging para el envío de notificaciones push inmediatas.</p>|
| - | - |

|<p>**Google Maps API**</p><p></p>|- La integración con Google Maps API permite la visualización georreferenciada de mascotas perdidas, definición de zonas de búsqueda y localización en tiempo real, mejorando la efectividad de los voluntarios en campo.|
| - | - |


|<p>**Visual Studio**</p><p></p>|<p>El desarrollo se realiza en Visual Studio Code, entorno que proporciona soporte para Flutter, Node.js y Firebase, además de herramientas de depuración, pruebas e integración con control de versiones Git.</p><p></p>|
| - | - |

|<p>**APK(despliegue)**</p><p></p>|El despliegue del sistema SOSMascota se realizará mediante la generación de un archivo APK (Android Package Kit), que permitirá instalar la aplicación directamente en dispositivos móviles con sistema operativo Android. Este proceso incluye la compilación del código en una versión optimizada de producción, la firma digital del paquete para garantizar su autenticidad y seguridad, así como la validación de compatibilidad en diferentes versiones del sistema operativo y dispositivos.|
| - | - |

*Fuente: Elaboración Propia*

Estas tecnologías trabajan en conjunto para ofrecer una plataforma móvil eficiente que responde a las necesidades actuales en la gestión y localización de mascotas perdidas. El sistema no solo optimiza procesos como el registro y seguimiento de reportes en tiempo real, sino que también fomenta la colaboración comunitaria, la trazabilidad de los casos y la seguridad en el manejo de datos personales, contribuyendo al bienestar de los dueños, voluntarios y animales de la comunidad.

1. # <a name="_7k5xxe2coxky"></a>**Metodología de implementación**
La metodología de implementación del sistema SOSMascota se organiza en fases claramente definidas, con el objetivo de garantizar un desarrollo eficiente, modular y alineado con las necesidades de la comunidad de dueños y rescatistas de mascotas. Cada fase del proceso sigue principios de ingeniería de software que aseguran tanto la calidad del producto final como su capacidad de adaptación a futuras mejoras. Esta estructura metodológica permite un enfoque flexible, asegurando que cada etapa cumpla con los estándares de calidad y que el sistema evolucione conforme a los requisitos de los usuarios.

*Tabla 07. Cuadro de la Metodología de implementación*

|**Planificación y Análisis**|
| :-: |
|Definición de Requerimientos: Se identificaron los requerimientos funcionales y no funcionales del sistema, incluyendo el registro de mascotas perdidas/encontradas, la geolocalización en tiempo real, las notificaciones automáticas, la autenticación de usuarios y la integración con redes sociales para la difusión de casos.|
|Análisis del Contexto Social: Se evaluaron las necesidades actuales de dueños, rescatistas y veterinarias, así como las limitaciones existentes en cuanto a la comunicación efectiva y la falta de un sistema centralizado de búsqueda de mascotas.|





|**Diseño**|
| :-: |
|Arquitectura del Sistema: Arquitectura de Estilo: Se baso una arquitectura Cliente–Servidor en MBBM, con separación en módulos (controllers, models, services y views), lo que facilita la escalabilidad y el mantenimiento.|
|**Diseño de Interfaz :** Se diseñaron pantallas móviles intuitivas (registro de mascota, mapa interactivo, notificaciones y perfil de usuario), aplicando principios de accesibilidad para que la aplicación sea usable por todo tipo de personas.|

|**Desarrollo**|
| :-: |
|Backend y Lógica del Negocio: Se desarrolló la lógica de registro de reportes, gestión de usuarios, envío de notificaciones y almacenamiento de datos en una base de datos relacional. Se integraron servicios de geolocalización para ubicar mascotas en tiempo real.|
|Frontend Dinámico: Se implementó la interfaz de usuario en Android/iOS con Flutter (o React Native, según el caso), integrando mapas, formularios dinámicos y notificaciones push.|

|**Pruebas**|
| :-: |
|Pruebas Unitarias e Integración: Se realizaron pruebas automatizadas y manuales para validar que cada módulo (registro, mapa, notificaciones, autenticación) funcionara correctamente de manera aislada y en conjunto.|
|Pruebas de Usabilidad: Se llevaron a cabo pruebas piloto con dueños de mascotas y voluntarios, simulando casos reales de pérdida, con el fin de evaluar la facilidad de uso y mejorar la experiencia de navegación.|



|**Mantenimiento y Evolución**|
| :-: |
|Actualizaciones Periódicas: Se planificó un ciclo de mejoras futuras como reconocimiento de mascotas por IA mediante imágenes, integración con servicios veterinarios, y funcionalidades de colaboración comunitaria.|
|Escalabilidad y Soporte Técnico: La modularidad de la arquitectura permitirá evolucionar hacia una versión distribuida en caso de crecimiento de usuarios a nivel regional o nacional.|

|**Despliegue**|
| :-: |
|El despliegue mediante APK garantiza que el sistema pueda ser evaluado en entornos reales antes de su publicación masiva. Este proceso permite validar la experiencia del usuario, la integración con las funcionalidades principales y la seguridad en la distribución inicial del aplicativo. Asimismo, se asegura la trazabilidad de las versiones y el control de calidad en cada actualización.|
|Finalmente, la publicación en la Google Play Store representa un paso clave para la masificación del sistema, al brindar a los usuarios una forma oficial y confiable de descargar la aplicación. Este canal de distribución también permitirá gestionar futuras mejoras y actualizaciones de manera automática, asegurando que la plataforma evolucione junto con las necesidades de la comunidad de dueños y rescatistas de mascotas.|

*Fuente: Elaboración Propia*

1. # <a name="_ymwbrq8l0we1"></a>**Cronograma**
   El cronograma de desarrollo del proyecto, que iniciará el 29 de octubre de 2025 y concluirá el 10 de diciembre de 2025, está diseñado para guiar de manera estructurada las fases de implementación en un periodo reducido. Las actividades se concentran en planificación, diseño, desarrollo acelerado, pruebas y despliegue final, manteniendo el cumplimiento de los objetivos principales.






*Tabla 08. Cuadro del Cronograma*

|**Semana**|**Fechas**|**Fase / Actividades**|
| - | - | - |
|Semana 1|29  – 2 septiembre|<p>Planificación y Análisis</p><p>• Requisitos funcionales y no funcionales</p><p>• Análisis del contexto social y tecnológico</p><p>• Definición de objetivos y alcance</p>|
|Semana 2|3 - 9 septiembre|<p>Diseño</p><p>• Arquitectura técnica (Backend + Frontend)</p><p>• Wireframes rápidos</p><p>• Diseño</p>|
|Semanas 3-5|10 -16 septiembre|<p>Desarrollo del Backend</p><p>• Configuración del entorno</p><p>• Implementación de API REST</p><p>• Base de datos y pruebas unitarias</p>|
|Semanas 6-7|17-23 septiembre|<p>Desarrollo del Frontend</p><p>• Maquetación de pantallas</p><p>• Integración con el backend</p><p>• Validación de formularios</p>|
|Semanas 8-9|24 - 30 septiembre|<p>Integración y Pruebas Internas</p><p>• Conexión frontend-backend</p><p>• Validación de flujos principales</p><p>• Corrección de errores iniciales</p>|
|Semana 10|1 – 29 octubre |<p>Pruebas de Usuario y Ajustes</p><p>• Sesiones piloto</p><p>• Feedback de usuarios</p><p>• Ajustes técnicos y de usabilidad</p>|
|Semanas 11-14|1 – 28 noviembre|Mejoras y Documentación- Implementación de mejoras- Documentación técnica y de usuario- Preparación para producción|
|Semanas 15-16|29 – 10 diciembre|<p>Despliegue y Cierre</p><p>• Pruebas finales</p><p>• Documentación técnica</p><p>• Despliegue en producción</p><p>• Presentación del proyecto</p>|

*Fuente: Elaboración Propia*

1. # <a name="_bqdd5wig7vu2"></a>**Presupuesto**
   Hablar de presupuestos manejables en el contexto del desarrollo de la Aplicación Móvil para la Localización de Mascotas Perdidas implica establecer una planificación financiera clara y eficiente que permita optimizar los recursos disponibles sin comprometer la calidad técnica ni el cumplimiento de los objetivos sociales y comunitarios del proyecto.

   Dado que este sistema está orientado a mejorar los procesos de búsqueda, reporte y localización de mascotas en entornos urbanos y familiares, se busca mantener un equilibrio entre funcionalidad, sostenibilidad y bajo costo operativo. Para ello, es necesario definir y proyectar los siguientes costos principales:

**Costos Generales**

`	`*Tabla 09. Cuadro de Costos Generales*

|Accesorios y Materiales|Costo por 1 mes|
| - | - |
|Papelería|S/. 15.00|
|Lapiceros|S/. 10.00|
|Cartuchos de Impresora|S/. 60.00|
|Computadora de Oficina|S/. 1500.00|
|Total|S/. 1585.00|

*Fuente: Elaboración Propia*










**Costos operativos durante el desarrollo**

*Tabla 10. Cuadro de Costos operativos durante el desarrollo*

|**Servicios**|**Costos mensuales**|
| :-: | :-: |
|Internet|S/. 100.0|
|Electricidad|S/. 70.0|
|Agua|S/. 30.0|
|Total|S/. 200.0|

*Fuente: Elaboración Propia*

**Costos del ambiente**

*Tabla 11. Cuadro de Costos del ambiente*

|**Descripción**|**Costo Mensual**|
| :-: | :-: |
|<p>Firebase Storage(uso</p><p>adicional)</p><p></p>|S/. 20.0|
|Total|S/. 20.00|
|**Descripción**|**Costo Mensual**|

*Fuente: Elaboración Propia*
###
###
###
###
###
###
###
###
###
###
###
###
###
### <a name="_fpw1phlhldob"></a><a name="_650rdmila28q"></a><a name="_ojmypzvxlphv"></a><a name="_bkcwnslvjtaj"></a><a name="_q91ijyfw0s5s"></a><a name="_xpcfhcccjd14"></a><a name="_4sm1g4te46k9"></a><a name="_6o6l5orfiulr"></a><a name="_yto5eb4zy580"></a><a name="_b8iqc22iwmpi"></a><a name="_3vdyis2tz6sv"></a><a name="_8rqy5pq6k8t1"></a><a name="_5ja0hlbnurr1"></a><a name="_7vcyahrw3tzm"></a>**Costos de personal**
Costos de sueldo del equipo de desarrollo durante la duración del proyecto.

*Tabla 12. Cuadro de Costos de personal*

|**Rol del Personal**|**Mensualmente**|
| :-: | :-: |
|Jefe del Proyecto|S/. 1000.0|
|Desarrollador Flutter|S/. 800.0|
|Tester|S/. 800.0|
|Total|S/. 2600.0|

*Fuente: Elaboración Propia*

**Costos totales del desarrollo del sistema**

*Tabla 13. Cuadro de Costos totales del desarrollo del sistema*

|***Categoría***|***Costo total (S/)***|
| :-: | :-: |
|Costos generales|S/. 1,585.0|
|Costos operativos|S/. 200.0|
|Costos del ambiente|S/. 20.0|
|Costos de personal|S/. 2600.0|
|**Costo total del proyecto**|S/. 4405.00|
|***Categoría***|***Costo total (S/)***|

*Fuente: Elaboración Propia*



1. # <a name="_tdx8m4k4y37"></a>**Conclusiones**
- El desarrollo de la Aplicación Móvil para la Localización de Mascotas Perdidas ha cumplido satisfactoriamente los objetivos generales y específicos planteados desde el inicio del proyecto. La solución resultante constituye una herramienta funcional, confiable y socialmente relevante para apoyar a las familias y comunidades en la búsqueda y recuperación de sus mascotas.
- Uno de los principales logros alcanzados ha sido la implementación de un sistema de registro y búsqueda de mascotas en tiempo real, que permite a los usuarios reportar extravíos, compartir información actualizada y recibir notificaciones inmediatas. Esta funcionalidad ha optimizado los tiempos de respuesta y ha incrementado la probabilidad de reunir a las mascotas con sus dueños.
- Asimismo, la aplicación integra características clave como geolocalización mediante mapas interactivos, registro fotográfico, validación de usuarios y comunicación comunitaria, lo que fortalece la confianza y la colaboración entre los actores involucrados.
- En materia de seguridad, se incorporaron mecanismos de autenticación y protección de datos personales, lo que garantiza un uso responsable de la información y genera un entorno seguro para los usuarios.

En resumen, el proyecto no solo alcanzó los objetivos técnicos, sino que además estableció una base escalable para futuras mejoras, consolidando un impacto social positivo en la comunidad y demostrando la viabilidad de aplicar buenas prácticas de ingeniería de software a problemas de interés social.







- ### <a name="_ni4wztch4r2r"></a>**Recomendaciones**
  Con base en la experiencia adquirida durante la ejecución del proyecto, se plantean las siguientes recomendaciones para fortalecer el desarrollo de iniciativas similares en el futuro:

- Integrar inteligencia artificial para el reconocimiento de imágenes, lo que permitiría identificar mascotas mediante fotografías y mejorar la precisión de las búsquedas.
- Ampliar la red de colaboración incluyendo a veterinarias, municipalidades y refugios, de modo que el sistema tenga un mayor alcance y cobertura en la recuperación de animales.
- Implementar pruebas automatizadas y pilotos comunitarios, con el fin de garantizar la confiabilidad del sistema y recopilar retroalimentación directa de los usuarios.
- Promover campañas de difusión y educación digital, orientadas a sensibilizar a la población sobre el uso de la aplicación y la importancia de reportar oportunamente mascotas extraviadas o encontradas.
- Fomentar la capacitación continua del equipo de desarrollo, para adoptar nuevas tecnologías móviles, metodologías ágiles y tendencias de seguridad digital.




### <a name="_1j3tiojmefc"></a>**Bibliografía**

- American Society for the Prevention of Cruelty to Animals (ASPCA). (2012). *How many pets are lost? How many find their way home? ASPCA survey has answers*. ASPCA. <https://www.aspca.org/about-us/press-releases/how-many-pets-are-lost-how-many-find-their-way-home-aspca-survey-has-answers>
- Patel, N., & Prajapati, K. (2021). *Pet Rescue: Mobile Application for Finding Lost Pets Using Geo-location Services*. *International Journal of Advanced Computer Science and Applications (IJACSA)*, 12(5). <https://doi.org/10.14569/IJACSA.2021.0120576>

- Lee, J., & Kim, H. (2020). *Location-based services and geospatial data in mobile applications*. *Sensors*, 20(24), 7230. <https://doi.org/10.3390/s20247230>
- Ojala, T., & Tyrväinen, P. (2019). *Developing mobile applications: Challenges and solutions*. *Journal of Systems and Software*, 150, 1–12. <https://doi.org/10.1016/j.jss.2019.110853>
- González, A., & Pérez, J. (2022). *Aplicaciones móviles para la protección y bienestar animal: Estado del arte y tendencias futuras*. *Revista Iberoamericana de Tecnología en Educación y Educación en Tecnología*, (30), 38–49. <https://doi.org/10.24215/18509959.30.e5>





### <a name="_s4027o7vc467"></a>**Anexos**
Anexo 01 Informe de Factibilidad Anex0 02 Documento de Visión Anexo 03 Documento SRS Anexo 04 Documento SAD

Anexo 05 Manuales y otros documentos
