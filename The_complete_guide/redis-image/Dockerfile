# Specify a base image
FROM alpine

# Run some commands to install addtional programs
RUN apk add --update redis
RUN apk add --update gcc

# Specify a command to run on container startup
CMD ["redis-server"]