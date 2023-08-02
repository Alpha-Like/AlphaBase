import psycopg2
from typing import Tuple
import sys
import random

class Database:
  def __init__(
    self,
    host: str,
    port: int = 5432,
    dbname: str = 'postgres',
    user: str = 'postgres',
    password
  ):
    try:
      self.conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
      )
      self.cursor = conn.cursor()
    except Exception as e:
      print('Cannot connect to Database !')
      print(e)
      sys.exit()
  
  def execute(self, *args: str) -> list[Tuple]:
    for x in args:
      self.cursor.execute(args)
    try:
      res: list = self.cursor.fetchall()
    except:
      res: list = []
    self.conn.commit()
    return res

  def exit(self) -> bool:
    try:
      self.cursor.close()
      self.conn.close()
      return True
    except:
      return False 
