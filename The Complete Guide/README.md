# Docker and Kubernetes: The complete guide

## About Docker 

Docker has a long ecosystem: 

* Docker Client
* Docker Server
* Docker Machine
* Docker Images
* Docker Hub
* Docker Compose

## First Steps

* docker run hello-world

## Docker Commands

docker run = docker create + docker start
-a : To see in the console the container's process
-i : STDIN in the container
-t : STDOUT in the container

* docker <command> <image_name> 
* docker create hello-world
* docker run hello-world
* docker ps
* docker ps --all
* docker system prune

* docker <command> <container_id>
* docker start 34e5351108a7
* docker start -a 34e5351108a7
* docker stop 34e5351108a7
* docker logs 34e5351108a7
* docker kill 34e5351108a7

* docker <command> <image_name> <command>
* docker run busybox echo hi there
* docker run busybox ping google.com
* docker run busybox ls
* docker run hello-word ls

## Multi-Command Containers

* docker run redis
* docker exec -it <container_id> <command>
* docker exec -it 82f1ede05d3f redis-cli
* docker exec -it 82f1ede05d3f sh 
* docker run -it busybox sh


## In a shell command

```bash
ls
cd /
ls
redis-cli
exit
```

## Create a Linux system in a Docker Container

* docker run ubuntu
* docker start ubuntu
* docker exec -it 466c33c57226 bash

```bash
apt update
apt install sudo
sudo apt install python3 npm nodejs
python3
```

## Create docker images

## Process

* Dockerfile: 
    * Configuration to define how our container should behave.
* Docker Client
* Docker Server
* Usable Image!

## Dockerfile

* Specify a base image
* Run some commands to install additional programs
* Specify a command to run on container startup

