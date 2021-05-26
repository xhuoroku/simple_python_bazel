# import boto3
import sys

def python3_only_function(parameter, *, option1=False, option2=''):
	print(sys.version)
    
def main(): 
	python3_only_function(3, option1=True, option2='Hello World!')
	print("yay done!")
    

if __name__ == '__main__':
    main()