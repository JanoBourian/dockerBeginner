# dockerBeginner
The first Docker Course for beginners

## Information 
    - docker container
    - docker image
    - docker images https://hub.docker.com/

## Install 
    - Docker in windows: https://docs.docker.com/desktop/windows/install/
    - docker --version

## Docker Commands
    - docker run <img name> : init or download the image
    - docker run <img name> sleep 20 : init or download the image
    - docker run redis:latest
    - docker run redis:4.0
    - docker ps : show info about containers that it's running
    - docker ps -a : show info about all containers
    - docker stop <container name | container id> : stop container
    - docker rm <container name> : remove container
    - docker images : show a list of all images availables
    - docker rmi <image name> : remove image
    - docker run -d <img name>
    - docker exec <container id> cat /etc/hosts : run command inside the container
    - docker pull <img name> : download image but docker doesn't run it
    - docker version
    
### Practices
    - docker run centos
    - docker run -it centos bash
    - cat /etc/*release*
    - exit
    - cls
    - docker run -d centos sleep 20 
    - docker stop <container name | container id>
    - docker rm <container name | container id>
    - docker rm [<container name | container id>, <container name | container id>, <container name | container id> ...]

### Tags
    - a : actives
    - d : in de background
    - i : interactive mode in the console
    - it : interactive mode and terminal
    - p : port assigment (or mappping ports)
    - v :

## Docker Run
    - docker run -p 80:5000 <container name>
    - docker run -p <external port>:<internal port> <container name>
    - docker run -v /opt/datadir:/var/lib/mysql mysql
    - docker run -v <external route>:<internal route> <container name>
    - docker inspect <container id> : container details in json format
    - docker logs <container name | container id>

### Jenkins Practices
    - for more information visit: https://github.com/jenkinsci/docker/blob/master/README.md
    - docker ps
    - docker ps -a
    - docker run ubuntu:17.10 sleep 150
    - docker run -d ubuntu:17.10 sleep 150
    - docker attach <container id> : Return to specific container (disabled interactive mode)
    - docker pull jenkins/jenkins
    - docker run jenkins/jenkins
    - docker inspect <container id>
    - docker run -p 8080:8080 jenkins/jenkins
    - Entry to ip:8080 url and follow the instructions
    - docker run -d -v /jenkins01:/var/jenkins_home -p 8080:8080 -p 50000:50000 -u root jenkins/jenkins
    - docker run -d -v C:<windows path>\jenkins01:/var/jenkins_home -p 8080:8080 -p 50000:50000 -u root jenkins/jenkins

## Docker Images
    
    - Overview:
        - Instructions --> Arguments
    - docker build . -f Dockerfile -t <image name>
    - docker push <image name>
    - docker build . -f Dockerfile -t <image name>

    - Flask app instructions:
        - OS - Ubuntu
        - Update apt repo
        - Install dependencies usign apt
        - Install Python dependencies using pip
        - Copy source code to /opt folder
        - Run the web server using "flask" command
    -
```
FROM Ubuntu

RUN apt-get update && apt-get -y install python

RUN pip install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```
## FAST API IMAGE AND CONTAINER

```
# docker-container-fastapi
A docker container for fastapi

# Create docker image
docker build -t myimage .

# Run docker container
docker run -d --name mycontainer -p 80:80 myimage
```

### Environment variables
    into the code color = os.environ.get('APP_COLOR')
    - docker run -e APP_COLOR=blue simple-webapp-color
    - docker inspect <container name> : in Config.Env section we can see the env variables

### Other ways

```
- docker build -t healt . 
- docker run -d --name healt -p 3001:3001 healt
- docker run --restart=always -dti --name "resthellowworld" -p 3001:3001 --env="PORT=3001" resthellowworld:1.0
- docker logs CONTAINER_ID
```

## Command vs Entrypoint
    - sleep 5
    - CMD ["command", "param1"]
    - ENTRYPOINT ["sleep"] & CMD["5"]
        - docker run ubuntu-sleeper 10


## Docker Compose

Docker compose is a yaml file with all configuration, example:

```
docker run mongodb
docker run redis:alpine
docker run ansible
```

docker-compose.yml
```
services:
    web:
        image: "mmushad/simple-webapp"
    database:
        image: "mongodb"
    messaging:
        image: "redis:alpine"
    orchestration:
        image: "ansible"
```

after: docker-compose up

## Example
    - voting-app: python
    - in-memory DB: redis
    - worker: .net core
    - db: postgresql
    - result-app: node-js

## Steps

First structure
```
docker run -d --name=redis redis
docker run -d --name=db postgres
docker run -d --name=vote -p 5000:80 voting-app
docker run -d --name=result -p 5001:80 result-app
docker run -d --name=worker 
```

With link option
```
docker run -d --name=redis redis
docker run -d --name=db postgres
docker run -d --name=vote -p 5000:80 --link redis:redis voting-app
docker run -d --name=result -p 5001:80 --link db:db  result-app
docker run -d --name=worker --link redis:redis --link db:db worker
```

with docker-compose.yaml when all images are already
```
redis:
    image:redis
db:
    postgres:9.4
vote:
    image:voting-app
    ports:
        - 5000:80
    links:
        - redis
result:
    image: result-app
    ports:
        - 5001:80
    links:
        - db
worker:
    image: worker
    links:
        - redis
        - db
```

After
```
docker compose up
```

with docker-compose.yaml when I will clone the repo or some images are not availables in docker hub (and these images are in own files directories)
```
redis:
    image:redis
db:
    postgres:9.4
vote:
    image:./vote
    ports:
        - 5000:80
    links:
        - redis
result:
    image: ./result
    ports:
        - 5001:80
    links:
        - db
worker:
    image: ./worker
    links:
        - redis
        - db
```

versions
```
version: 3
services:
    redis:
        image:redis
        networks:
            - backend
    db:
        postgres:9.4
        networks:
            - backend
    vote:
        image:./vote
        ports:
            - 5000:80
        links:
            - redis
        depends_on:
            - redis
        networks:
            - fontrend
            - backend
    result:
        image: ./result
        ports:
            - 5001:80
        links:
            - db
        networks:
            - fontrend
            - backend
    worker:
        image: ./worker
        links:
            - redis
            - db
        networks:
            - backend
networks:
    frontend
    backend

```

Networks inside the app

## Important

If We will go to download a github repo and start to work first we need to create the images for each part of the app, for example for voting-app, for worker, etc...

```
docker build . -t voting-app
docker run -p 5000:80 --link redis:redis voting-app
docker run -d --name=db postgres:9.4 <-- only if the image is downloaded of dockerhub
```

Because if we work with docker compose the steps will be less
    - Install Docker Compose
    - Create Compose File
    - Run Docker Compose

```
docker-compose up
```

## Docker Registry



## Docker Engine, Storage and Networking


## COntainer Orchestration - Docker Swarm and Kubernetes

