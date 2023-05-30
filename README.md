# Docker and kubernetes for several platforms

# General information about Docker

## Summary
- [Introduction](#section1)
- [Docker Commands](#section2)
- [Docker Run](#section3)
- [Docker Images](#section4)
- [Docker Compose](#section5)
- [Docker Registry](#section6)
- [Docker Engine](#section7)
- [Container Orchestation](#section8)


<br>
<div id="section1">

## Introduction

### Layers

* Hardware
* OS - Ubuntu (For example)
* Docker 
    * Container
        * Libs
        * Deps
        * Application

### Where is the information?

* Docker Image: Packages, Template, Plan
* Docker Container: Copy from Docker Image

<br>
<div id="section2">

## Docker commands

```sh
docker run <CONTAINER_NAME> # run the container
docker ps # list active containers
docker ps -a # list all containers
docker stop <CONTAINER_NAME> # stop the container
docker rm <CONTAINER_NAME> # remove the container
docker images # list all images
docker rmi <IMAGE_NAME> # remove a image
docker pull <CONTAINE_IMAGE> # only download the image (without run the container)
docker exec <CONTAINER_NAME> <COMMAND> # communicate commands with the container
docker run -d <CONTAINER_NAME> # execute the container in background
docker run -it <CONTAINER_NAME> <COMMAND> # run command inside the container
```

Examples:

```sh
docker run kodekloud/simple-app
docker run -d kodekloud/simple-app
```

```sh
docker run redis
docker stop 682443bffe3a
docker start 682443bffe3a
docker exec -it 682443bffe3a sh
docker stop 682443bffe3a
```

<br>
<div id="section3">

## Docker run

General steps

```sh
docker build -t <CONTAINER_ID>/<CONTAINER_NAME>:<VERSION> .
docker run -d --name bashversion -d a54ac3793f2776bc46002f5bff45e2c691e1e92c0e3a693af4289a38df41f57a
```

## Interactive mode

```sh
docker build -t janobourian/bash:latest .
docker run -d --name bashversion -it janobourian/bash:latest
docker start -i bashversion
docker stop bashversion
```

## Port Mapping

```sh
docker build -t janobourian/flaskapp:latest .
docker run -d --name flaskapp -p 8080:3000 -d janobourian/flaskapp:latest
```

## Volume mapping

```sh
docker run -v <EXTERNAL>:<INTERNAL> mysql
```

## Inspect

```sh
docker inspect bashversion
```

## Logs

```sh
docker logs bashversion
```

<br>
<div id="section4">

## Docker images

```sh
```

```sh
```

```sh
```

```sh
```

<br>
<div id="section5">

## Docker compose

```sh
```

```sh
```

```sh
```

```sh
```

<br>
<div id="section6">

## Docker registry

```sh
```

```sh
```

```sh
```

```sh
```

<br>
<div id="section7">

## Docker engine

```sh
```

```sh
```

```sh
```

```sh
```

<br>
<div id="section8">

## Docker orchestation

```sh
```

```sh
```

```sh
```

```sh
```