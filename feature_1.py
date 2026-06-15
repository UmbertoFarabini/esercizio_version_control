import os
from datetime import datetime
import time



def create_folders() -> str:
  """crea cartelle di lavoro se non esistenti"""
  f_list = os.listdir()
  if "in" not in f_list:
    os.mkdir("./in")
    ret = "cartella \"in\" inizializzate correttamente"
  else: ret = "cartella \"in\" già esistente"
  return ret

def create_file() -> str:
  file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
  f = open(f"in/{file_name}", "x")
  return f"creato file \"./in/{file_name}\""



print(create_folders())

while True:
  print(create_file())
  time.sleep(10)
