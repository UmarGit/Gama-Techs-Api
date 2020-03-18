import requests

def update():
  params2 = {
  "api_key": "tFO5MS3MqZZ2",
  "send_email": "1"
  }
  r = requests.post("https://www.parsehub.com/api/v2/projects/tb8TVjOOkGtq/run", data=params2)
  content = '<h1>=>>>> DATA UPDATED SUCCESSFULLY</h1>'
  return content