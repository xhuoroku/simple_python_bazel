# import boto3
import sys
from helper import helper_function

def main():
  print("Python 2 only!")
  print(sys.version)
  helper_function()
  print("\n".join(sys.path))


if __name__ == '__main__':
  main()
