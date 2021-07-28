# import boto3
import sys
from helper import helper_function
from src.main.python.another_folder.a import foo_a

def main():
  print(sys.version)
  helper_function()
  print("\n".join(sys.path))
  foo_a()


if __name__ == '__main__':
  main()
