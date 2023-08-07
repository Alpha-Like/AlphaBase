import psycopg2
import sys

def parse_args(*args: tuple) -> str:
  txt: str = ''
  for x in args:
    txt += f'{x[0]} {x[1]}'
    txt += ', '
  return txt[:-1]

def iterable_to_string(iterable: tuple | list | set | dict, seperator: str = ' ') -> str:
  txt: str = ''
  for x in iterable:
    txt += x + seperator
  return txt.strip()

class Database:
  def __init__(
    self,
    host: str,
    port: int = 5432,
    dbname: str = 'postgres',
    user: str = 'postgres',
    password: str
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
      print('Cannot connect to SQL Alphabase !')
      print(e)
      sys.exit()
  
  def execute(self, *args: str) -> list[tuple]:
    for x in args:
      self.cursor.execute(args)
    try:
      res: list = self.cursor.fetchall()
    except:
      res: list = []
    self.conn.commit()
    return res

  def create_table(self, table_name: str, *args: str):
    self.execute(f'CREATE TABLE {table_name} ({iterable_to_string(*args)});')

  def insert(self, table_name: str, *args):
    values = *args
    self.execute(f'INSERT INTO {table_name} VALUES ({iterable_to_string(values)});')

  def delete(self, table_name: str, column_name: str, value):
    self.execute(f'DELETE FROM {table_name} WHERE {column_name}={value};')

  def drop_table(self, table_name: str):
    self.execute(f'DROP TABLE {table_name};')

  def exit(self) -> bool:
    try:
      self.cursor.close()
      self.conn.close()
      return True
    except:
      return False 
