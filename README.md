* This is an exercise to test your ability to both debug and add features to a python script.
* This script is meant to extract data from mysql, transform it with python, and upload it to clickhouse.


* Docker compose is used to deploy 3 containers, one for mysql, one for clikhouse, and one for python.
* The source table will be created and data will automatically be inserted in mysql when you start the containers.
* The destination table will be created and data be inserted when you run the python script (after debugging and adding features)

* Please feel free to use the internet and any LLM's, such as chatgpt.


We're running this through vscode liveshare. You will be able to make changes to files, but will need to tell us to run the script when you've made changes.

First we will try to fix the script, as it is broken in it's current state. This is to see how you debug

Then you will be asked to create two new functions that will transform the data before putting it in clickhouse.



NOTE: if you're running this on your own using docker (not on liveshare you will need the following commands)
 
# how to start all the services
```bash
docker ps
docker compose -f docker-compose.yaml up
```
 
# how to connect to the mysql  container, and create a sql client
```bash
docker exec -it interview-mysql-1 bash
mysql -h mysql -u example_user -pexample_password
```

# how to connect to clickhouse container and create client:
```bash
docker exec -it interview-clickhouse-1 bash
clickhouse-client --host=clickhouse --user=default --password=password
```
 

# Run the script
```bash
docker exec -it interview-python_service-1 /app/extraction_script.py
```

## how to connect to the python container (shouldn't need to do this)
```bash
docker exec -it interview-python_service-1 bash
```
