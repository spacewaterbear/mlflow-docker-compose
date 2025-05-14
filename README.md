# MLflow On-Premise Deployment using Docker Compose
Easily deploy an MLflow tracking server with 1 command.

MinIO S3 is used as the artifact store and MySQL server is used as the backend store.

## How to run

1. Build and run the containers with `docker-compose`

    ```bash
    compose up -d --build
    ```

4. Access MLflow UI with http://localhost:5000

5. Access MinIO UI with http://localhost:9000

   
Change user admin
first add default admin user and password

```bash
export MLFLOW_TRACKING_USERNAME_NEW=<your_new_username>
export MLFLOW_TRACKING_PASSWORD_NEW=<your_new_password>
```
And then 
`make`
`make clean`





## Containerization

The MLflow tracking server is composed of 3 docker containers:

* MLflow server
* MinIO object storage server
* MySQL database server



## External usage : 

Make sure to have these env present when you use mlflow
    ```bash
   export MLFLOW_TRACKING_URI=http://localhost:5000
   export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
   export AWS_ACCESS_KEY_ID=minio
   export AWS_SECRET_ACCESS_KEY=minio123
   
    ```

