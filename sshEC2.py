//Install Python, Pip, Pandas and s3fs
// open ssh into EC2 instance and run below commands

sudo yum install python3 -y
sudo yum install python3-pip -y
sudo yum groupinstall "Development Tools" -y
pip3 install pandas --user
pip3 install s3fs --user
python3 -m pip install boto3

//Install Airflow, intilize Airflow database, create new user for Airflow
pip3 install "apache-airflow[celery,redis,postgres]" --user
airflow db init
airflow users create \
    --username your_username \
    --firstname your_firstname \
    --lastname your_lastname \
    --role Admin \
    --email your_email@example.com

//Start Airflow webserver and scheduler
airflow webserver --port 8080
airflow scheduler
