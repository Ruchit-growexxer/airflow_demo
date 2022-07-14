from airflow.operators.bash_operator import BashOperator
import pytest
# using template
def test_bash_operator_tmpdir(test_dag, tmpdir):
  tmpfile = tmpdir.join("hello.txt")
  task = BashOperator(task_id="test", bash_command=f"echo 'create_entry_group' > {tmpfile}", dag=test_dag)
  pytest.helpers.run_task(task=task, dag=test_dag)
  assert len(tmpdir.listdir()) == 1
  assert tmpfile.read().replace("\n", "") == "create_entry_group"