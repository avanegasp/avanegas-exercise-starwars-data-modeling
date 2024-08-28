# Modelo de Datos del Blog de StarWars
Este proyecto consiste en crear un modelo de datos para un blog de StarWars, utilizando Python y SQLAlchemy para definir y gestionar las relaciones entre las entidades en una base de datos. La finalidad es construir un diagrama de relación de entidad (ERD) para representar las interacciones entre usuarios, planetas, personajes, y sus favoritos dentro del blog.

![Starwars Diagram](https://github.com/breatheco-de/exercise-starwars-data-modeling/blob/master/assets/example.png?raw=true)


## Tecnologías Utilizadas
- **Lenguaje:** Python
- **ORM:** SQLAlchemy para el manejo de la base de datos
- **Diagrama ERD:** Herramienta de diagramación de bases de datos, como QuickDBD

## Características del Proyecto
Modelos y Relaciones

### Usuario

- **Propiedades:** id, email, password, nombre, apellido, fecha_subscripción
- **Relación uno-a-muchos** con Favoritos

### Personaje (Character)

- **Propiedades:** id, nombre, especie, planeta_origen, descripcion
- **Relación muchos-a-muchos** con Favoritos

### Planeta (Planet)

- **Propiedades:** id, nombre, clima, terreno, poblacion
- **Relación muchos-a-muchos** con Favoritos

Favoritos (Favorites)

- **Propiedades:** id, usuario_id, personaje_id, planeta_id
- **Relación muchos-a-muchos** con Usuario, Personaje y Planeta

## Objetivos del Proyecto
- **Modelado de Base de Datos:** Definir y crear tablas para usuarios, personajes, planetas, y favoritos, junto con las relaciones entre ellas.
- **Generación de Diagramas UML:** Utilizar SQLAlchemy para crear un diagrama UML que represente las entidades y relaciones de la base de datos.
- **Gestión de Dependencias:** Instalación y configuración del entorno con pipenv y manejo de dependencias para Python.

## Mejora Continua
El proyecto puede ser ampliado para incluir funcionalidades como autenticación de usuarios y operaciones CRUD adicionales para los personajes y planetas.

