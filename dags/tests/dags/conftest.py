import datetime
import airflow
from airflow.models import DAG
import pytest
from datetime import timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
pytest_plugins=['helpers_namespace']

@pytest.fixture
def test_dag():
  return DAG(
    "my_dag",
    start_date=datetime.datetime(2022,7,14),
    schedule_interval=timedelta(days=1), 
  )

@pytest.helpers.register
def run_task(task,dag):
  dag.clear()
  task.run(start_date=dag.start_date, end_date=dag.start_date)

def test_bash_operator_tmpdir(test_dag, tmpdir):
  tmpfile = tmpdir.join("hello.txt")
  task = BashOperator(task_id="create_entry_group", bash_command=f"echo 'create_entry_group123456' > {tmpfile}", dag=test_dag)
  pytest.helpers.run_task(task=task, dag=test_dag)
  assert len(tmpdir.listdir()) == 1
  print(tmpfile)
  assert tmpfile.read().replace("\n", "") == "create_entry_group123456"

def test_full_context(test_dag, tmpdir):
  def do_magic(**context):
    with open(tmpdir / "test.txt", "w") as f:
      f.write(context["ds"])
  task = PythonOperator(task_id="test", python_callable=do_magic, provide_context=True, dag=test_dag)
  pytest.helpers.run_task(task=task, dag=test_dag)
  with open(tmpdir / "test.txt", "r") as f:
    assert f.readlines()[0] == test_dag.start_date.strftime("%Y-%m-%d")

def odd_even(**context):
  return context["sum"] + 11%2
def test_python_operator():
  test = PythonOperator(task_id="test", python_callable=odd_even, provide_context=True)
  testdate = 0
  result = test.execute(context={"sum": testdate})
  assert result == 0 