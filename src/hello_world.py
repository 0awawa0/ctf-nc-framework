from lib.types import IStdin, IStdout


def hello(stdin: IStdin, stdout: IStdout):
    stdout.write("Hello!\n")
