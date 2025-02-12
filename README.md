* This is an exercise to test your ability to both debug and add features to a python script.
* This script is meant to extract data from mysql, transform it with python, and upload it to clickhouse.
* Docker compose is used to deploy 3 containers, one for mysql, one for clikhouse, and one for python.
* The source table will be created and data will automatically be inserted in mysql when you start the containers.
* The destination table will be created and data be inserted when you run the python script (after debugging and adding features)
* Please feel free to use the internet and any LLM's, such as chatgpt.
 
# how to start app
```bash
docker ps
docker compose -f docker-compose.yaml up
```

# how to connect to the mysql python container
```bash
docker exec -it interview-mysql-1 /app//
docker exec -it interview-python_service-1 bash
```

## how to connect to mysql in the terminal
```bash
mysql -h mysql -u example_user -pexample_password
```