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

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```