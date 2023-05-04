# Integration

```bash
docker pull jenkins/jenkins
mkdir jenkins
cd jenkins
```

## docker-compose.yaml

```yaml
version: '3'
services:
  jenkins:
    container_name: jenkins
    image: 'jenkins/jenkins'
    ports:
      - "8080:8080"
    volumes:
      - "C:\\jenkins_home:/var/jenkins_home"
    networks:
      - net
networks:
  net: 
```

## commands after creating docker-compose

```bash
docker-compose up --build
docker-compose stop
docker-compose start
```

## Inside our docker container

You can execute operation and you can copy information inside you container
```bash
docker exec -it c7def5f4e99b bash
docker cp script.sh jenkins:/tmp/script.sh
docker cp script.sh c7def5f4e99b:/tmp/script.sh
```
## Script in build steps inside jenkins

```bash
rm -rf /tmp/info
NAME=janobourian
echo "Hello $NAME the current date is: $(date)" > /tmp/info
cat /tmp/info
/tmp/script.sh janobourian lastname
```

```bash
```

```bash
```

```bash
```