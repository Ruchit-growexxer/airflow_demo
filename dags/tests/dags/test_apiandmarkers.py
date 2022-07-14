# run successfully.
import token
import pytest
import requests
import json
import pytest
import sys
import math

def main_url():
  return "https://reqres.in"

def test_login():
  url="https://reqres.in/api/login/"
  data={'email': 'eve.holt@reqres.in','password': 'cityslicka'}
  response=requests.post(url,data=data)
  token=json.loads(response.text)
  assert response.status_code == 200
  assert token['token'] == "QpwL5tke4Pnpja7X4"

@pytest.mark.skip(reason="unwanted test_case.")
def test_add_num():
  assert 2+5 == 7

@pytest.mark.skipif(sys.version_info >(3,9),reason="unwanted test case")
def test_add_str():
  assert 3+9 == 12

@pytest.mark.xfail(sys.platform == "linux",reason="It is only accepted with window system")
def test_add_num():
  assert 4+6 == 10
  raise Exception()

@pytest.mark.parametrize("a,b,e",[(1,2,3),("a","b","ab")])
def test_add(a,b,e):
  assert 1+2 == 3