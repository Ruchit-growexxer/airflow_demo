import datetime
from pathlib import PosixPath
from unittest import mock
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.models import TaskInstance

def test_bash(tmp_path:PosixPath):
  with DAG(dag_id="test_mock",start_date=datetime.datetime(2022,7,14),schedule_interval="@daily")as dag:
    with mock.patch("airflow.models.variable.Variable.get") as variable_get_mock:
      emp=["ruchit","ankur","prit","shiv","dhruv"]
      variable_get_mock.return_value=emp
      outputs=tmp_path /"output.txt"
      test=BashOperator(task_id="tets_mocking",bash_command="echo {{ var.json.emp}}"+str(outputs))
      dag.clear()
      dag.run(
        start_date=dag.start_date,
        end_date=dag.end_date,
        ignore_first_depends_on_past=True,
        ignore_ti_state=True,
      )
      variable_get_mock.assert_called_once()
      assert outputs.read_text() == f"{{', '.join(emp)}}\n"