from lib.types import IStdin, IStdout
from src.ezTask.secondary import print_hello

def main(stdin: IStdin, stdout: IStdout):
	stdout.write(print_hello())
	stdout.flush()