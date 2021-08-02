create virtual envirment

$python3.9 -m venv <envirment name, im using 'airflow'>

activate it

$source airflow/bin/activate

install airflow

$pip3 install apache-airflow

edit bash/zsh

$sudo nano ~/.rshrc

and add

export AIRFLOW_HOME="/Users/<path to dir of lab>/airflow_home/"

save and run

$source ~/.rshrc

create dir for AIRFLOW_HOME

$mkdir airflow_home

and a dir for DAGS

$mkdir $AIRFLOW_HOME/dags

init airflow

$airflow db init

create User

$airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

to check it worked

$ cd $AIRFLOW_HOME
$ tree .

install ploylt

$pip3 install plotly
