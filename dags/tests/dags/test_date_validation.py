import unittest
from airflow.models import DagBag
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import unittest
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
class testdemo(unittest.TestCase):
  def test_mydag(self):
    dag_bag=DagBag(dag_folder="opt/airflow/dags/",include_examples=False)
    assert not dag_bag.import_errors

    for dag_id,dag in dag_bag.dags.items():
      err_msg=f'{dag_id} in {dag.full_filepath} has no tags'
      assert dag.tags,err_msg

  def test_bash(self):
    test=BashOperator(task_id="test",bash_command="echo ruchit ")
    re=test.execute(context={})
    assert re == "ruchit"

  def test_python_operator(self):
    def returntoday(**context):
      return f"Today is {context['execution_date'].strftime('%d-%m-%Y')}"
  
    test=PythonOperator(task_id="testdate",python_callable=returntoday)
    re=test.execute(context={'execution_date':datetime(2022,7,14)})
    assert re =="Today is 15-07-2022"
