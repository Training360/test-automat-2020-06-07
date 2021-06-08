FROM postman/newman:5-ubuntu
COPY postman postman
ENTRYPOINT ["newman", "run", "postman/TestCreateLocation.postman_collection.json", "-e", "postman/Docker.postman_environment.json"]