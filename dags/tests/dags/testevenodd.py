import unittest
from datetime import datetime
from airflow import DAG
from airflow.models import TaskInstance
from evenodd import EvenNumberCheckOperator

DEFAULT_DATE = datetime(2022, 7, 14)

class EvenNumberCheckOperator(unittest.TestCase):
  def setUp(self):
    super().setUp()
    self.dag = DAG('test_dag', default_args={'owner': 'airflow', 'start_date': DEFAULT_DATE})
    self.even = 10
    self.odd = 11
    
  def test_even(self):
      
    task = EvenNumberCheckOperator(my_operator_param=self.even, task_id='even', dag=self.dag)
    ti = TaskInstance(task=task, execution_date=datetime.now())
    result = task.execute(ti.get_template_context())
    assert result is True
      
  def test_odd(self):
    task = EvenNumberCheckOperator(my_operator_param=self.odd, task_id='odd', dag=self.dag)
    ti = TaskInstance(task=task, execution_date=datetime.now())
    result = task.execute(ti.get_template_context())
    assert result is False