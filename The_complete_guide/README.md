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
-p : To set the port configuration
-v : Volume persistence
-d : Detached mode
--name :

## More commands

build :
run :
start :
stop : 
inspect : 
logs :
ps : 
kill : 
exec : 
images : 
rm : 
rmi :
pull :
version :

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
apt install sudo curl
sudo apt install python3 npm nano
npm install -g n   
n latest
hash -r
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
apt install python3.10-venv
sudo apt install git-all
python -m venv .venv
source .venv/bin/activate
sudo apt install gh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo service docker start
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

or 

* install an operating system
* start up your default browser
* navigate to chrome.google.com
* download installer 
* open file/folder explorer
* execute chrome_installer.exe
* execute chrome.exe

## Redis image

* docker build .
* docker images
* docker run d7e6cf8d9f47
* docker build -t <docker_ID>/<Project_name>:latest .
* docker build -t janobourian/test:latest .
* docker run -d --name testing -d janobourian/test:latest
* docker run -d --name visitorapp -p 8000:80 -d 1965ba51b2989a351b5d15ae836f2b947f94e641e28c7384fb72264ea24c5027

## Instructions inside Dockerfile

<instruction> <argument>

```Dockerfile
FROM alpine
RUN apk add --update redis
RUN apk add --update gcc
CMD ["redis-server"]
```

## fastapi-container

* Create NodeJS web app
* Create a Dockerfile
* Build image from Dockerfile
* Run image as container
* Connect to web app from a browser

```bash
# FROM
FROM python:latest

# WORKDIR
WORKDIR /code

# COPY
COPY ./requirements.txt /code/requirements.txt

# RUN
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY
COPY ./app /code/app

# CMD 
CMD ["uvicorn", "app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "80"]
```

## Docker compose

* Separate CLI that gets installed along with Docker
* Used to start up multiple Docker container at the same time
* Automates some of the long-winded arguments we were passing to 'docker run'

* docker-compose up --build
* docker-compose up -d
* docker-compose down 
* docker-compose ps

## Restart policies

* "no"
* always
* on-failure
* unless-stopped

## Docker compose structure

```yaml
# version
version: '3'
# services
services:
# each container
  webapp:
    restart: always
    build: .
    ports: 
      - "3000:3000"
    volumes:
      - /app/node_modules
      - .:/app
```

```yaml
version: '3'
services:
  redis-server:
    image: 'redis'
  visitorapp:
    restart: always
    build: .
    ports:
      - "8081:80"
```

More information: https://geshan.com.np/blog/2021/12/docker-postgres/

## Production-Grade Workflow

* Github reposiroty
  * feature -> master
  * Jenkins
  * AWS hosting

## Dockerfile.dev

*Dockerfile.dev* is using in development.

* docker build -f Dockerfile.dev -t janobourian/frontend:latest .
* docker run -p 3000:3000 c290d930338f

## Docker Volumes

Re-running in Linux

* docker run -p 3000:3000 -v /app/node_modules -v $(pwd):/app --name reactapp c290d930338f .

## Docker compose with tests

```yaml
# version
version: '3'
# services
services:
# each container
  webapp:
    restart: always
    build: 
      context: .
      dockerfile: Dockerfile.dev
    ports: 
      - "3000:3000"
    volumes:
      - /app/node_modules
      - .:/app
  tests:
    restart: on-failure
    build: 
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - /app/node_modules
      - .:/app
    command: ["npm", "test"]
```