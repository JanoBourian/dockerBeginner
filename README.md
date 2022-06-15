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

## Docker Compose


## Docker Registry



## Docker Engine, Storage and Networking


## COntainer Orchestration - Docker Swarm and Kubernetes

