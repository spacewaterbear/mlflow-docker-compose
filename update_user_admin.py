import os

from mlflow.server import get_app_client

os.environ['MLFLOW_TRACKING_USERNAME'] = "admin"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "password"
tracking_uri = "http://localhost:5000/"

if __name__ == '__main__':
    new_user = os.environ['MLFLOW_TRACKING_USERNAME_NEW']
    new_password = os.environ['MLFLOW_TRACKING_USERNAME_NEW']
    if new_user and new_password:
        auth_client = get_app_client("basic-auth", tracking_uri=tracking_uri)
        auth_client.create_user(username=new_user, password=new_password)
        auth_client.update_user_admin(username=new_user, is_admin=True)
        auth_client.delete_user(username="admin")
    else:
        raise Exception("You need to provide both MLFLOW_TRACKING_USERNAME_NEW and MLFLOW_TRACKING_USERNAME_NEW")
