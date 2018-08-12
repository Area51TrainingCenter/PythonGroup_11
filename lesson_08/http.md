#HTTP

##Hypertext Transfer Protocol

Protocolo de transferencia de datos en servicios web cliente - servidor. No tiene estado, no guarda información sobre conecciones anteriores.

Creado por *Tim Berners Lee*.

**IETF Working Group** es la organización que regula los estándares del protocolo Http.


HTTP 1.x | HTTP 2
---------|--------
Header extenso| Header comprimido usando PACK
Transfiere texto plano| Transfiere datos binarios
Soporta http y https| Sólo https
secuencial, bloqueante| multiplexado, server push

### Métodos HTTP

Las peticiones al servidor las podemos clasificar en distintos métodos, según la acción a realizar por el servidor. Las principales son:

####GET

Lo usamos generalmente cuando queremos solicitar datos.

####POST

Este método se usa generalmente cuando queremos modificar el modelo de datos del servidor, agregando un nuevo registro.

####PUT

Este método se usa generalmente cuando queremos modificar el modelo de datos del servido, actualizando un registro existenter.

####DELETE

Este método se usa generalmente cuando queremos modificar el modelo de datos del servidor, eliminando un registro existente.

### Códigos de estado

#### 1xx

Respuestas informativas. Indica que la petición ha sido recibida y se está procesando.

#### 2xx

Respuestas correctas. Indica que la petición ha sido procesada correctamente.

#### 3xx

Respuestas de redirección. Indica que el cliente necesita realizar más acciones para finalizar la petición.

#### 4xx

Errores causados por el cliente. Indica que ha habido un error en el procesado de la petición a causa de que el cliente ha hecho algo mal.

#### 5xx

Errores causados por el servidor. Indica que ha habido un error en el procesado de la petición a causa de un fallo en el servidor.

[Http en Wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto)
