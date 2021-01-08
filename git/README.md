### Comandos basicos de docker 

 

Docker es un proyecto de codigo abierto en el cual se permite usar la prescencia de contenedores
para poder manejar un entorno modular, en donde cada contenedor trabajara de manera independiente,
por lo que el sistema no colapsara completamente ante un incidente.

 

```sh
$ docker run it "name of operative system"
$ docker run -it -p "8080:80 nginx"
$ docker ps
$ docker rm -f "id_container"
$ docker exec -it e86f70a90521 cat /jesus_ariel/archivo.txt


```