from asyncio import Task
import unittest
from airflow.models import DagBag
import re

class test(unittest.TestCase):
   def test_dag(self):
      dagbag=DagBag(dag_folder="/opt/airflow/dags/",include_examples=False)
      dag_ids =["example_complex","demos","xcom_dag"]
      for dag_id in dag_ids:
         dag=dagbag.get_dag(dag_id)
         assert dag is not None
         assert dag_id == dag.dag_id
         print(dag_id)
         assert dagbag.size() >=3
         print(dagbag.size())
     
      dag=dagbag.get_dag("demos")
      print(dagbag.get_dag("demo"))


class test2(unittest.TestCase):
   def test_email_present(self):
    dags =DagBag(dag_folder="/opt/airflow/dags/",include_examples=False)
    email_regex = re.compile(
        r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    )  # regex to check for valid email
    
    for dag_id,dag in dags.dags.items():
      emails = dag.default_args.get("email",[])
      print("emails:",emails)
      print(email_regex)
      print(emails)
      for email in emails:
         assert email_regex.match(email) is None  

   


         

  
