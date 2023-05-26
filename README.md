# Docker and kubernetes for several platforms

# General information about Docker

## Summary
- [Introduction](#section1)
- [Docker Commands](#section2)
- [Test](#section3)

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

## Topic 2