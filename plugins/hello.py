from airflow.models.baseoperator import BaseOperator

class HelloOperator(BaseOperator):
    def __init__(self,task_id:str,a:int,b:int) -> None:
        super().__init__(**kwargs)
        self.a=a
        self.b=b
        self.task_id=task_id

    def execute(self, context):
        c=self.a+self.b
        d=self.task_id
        print(c)
        return c,d