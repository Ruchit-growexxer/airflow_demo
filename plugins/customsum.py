from airflow.models.baseoperator import BaseOperator
class sumoftwo(BaseOperator):
    def __init__(self,a: int,b:int,**kwargs) -> None:
      super().__init__(**kwargs)
      self.a=a
      self.b=b
      
    def execute(self, context):
      c=self.a+self.b
      print(c)
      #message=f"Hello {self.name}"
      print(c)
      return c
