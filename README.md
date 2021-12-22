# Endpoint React App
`http://localhost:8000`
# Endpoint Flask API
`http://localhost:5000`
The REST API to the example app is described below.
## Get routes BGP <network>

### Request

`GET /api/routes/<network>`
### Response
    HTTP/1.1 200 OK
    Date: Thu, 22 Dec 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 4487
    {OUTPUT:"show bgp ipv4 unicast ... route-server> exit",TIME: "2021-12-09 12:03:20"}
    
# Challenge Telconet Teoría
5. El ciclo de vida vendría a ser:
   - Planificación:
     Analizar los requisitos y, de la idea abstracta del resultado final, afinar los detalles del proceso para obtener el resultado deseado.
   - Implementación y pruebas:
     El lenguaje y tecnología vendrían a ser Python y el uso de Dockers containers. Realizando el testing de los módulos de cada problema planteado, y probar su funcionamiento en conjunto.
6. Diagrama: https://drive.google.com/file/d/1qg6Hk1kORgMgaDu-WhVySXZUnWoc5s7h/view?usp=sharing 
7. Debería haber mayor seguridad. Un middleware para el uso del API y de la APP que pueda acceder a los recursos con algún token. El bot de igual forma debería acceder a los recuersos con seguridad.
8. Debería existir un mejor front en la parte de la APP. De igual forma un sistema de acceso a los recursos del API. El Bot debería desarrollar comandos interactivos con el cliente. 

   
