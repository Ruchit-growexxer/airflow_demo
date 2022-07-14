import unittest
from airflow import DAG
from datetime import datetime
from customsum import sumoftwo
from airflow.models import TaskInstance

class TestMyOperator(unittest.TestCase):

    def test_execute(self):
        dag = DAG(dag_id='sumtwo', start_date=datetime.now())
        task = sumoftwo(dag=dag, task_id='addtwo')
        ti = TaskInstance(task=task, execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertEqual(result,30)