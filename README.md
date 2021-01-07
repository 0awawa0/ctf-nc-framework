# ctf-nc-framework #
A tiny framework to run python challenges in raw TCP.

## Install
Just clone this repo and you are ready to go. 

To test it run:
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --task main
Running in production at port 57547
</pre>

And connect with `nc`:
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 57547
Hello, world!
What is your name? alex
Hello, alex!
</pre>

## Adding your tasks

### Task format

Every task you want to run must have function with following signature in it:

```python
from lib.types import IStdin, IStdout

def function_name(stdin: IStdin, stdout: IStdout):
    # your code
```

Use ```stdin.readline()``` to read user's input as a single-line string.
Use ```stdout.write(string)``` to send data back to user. `string` must end with `\n` to be sent. Or you can use

```python
stdout.write(string)
stdout.flush()
```

to force sending. Example:

```python
string1 = "Hello, world!\n"
stdout.write(string1)

string2 = "Hello, world!"
stdout.write(string2)
stdout.flush()
```

### Configuring tasks.py

Generally all tasks are placed in `./src` folder. Although it is not necessary. All tasks are listed in file `tasks.py`.
It should look like this:

```python
def get_task(task_name):
	if task_name == "main":
		import src.main
		return src.main.main
```

So to add new task you should just add another import. Let's say we want to add task `hello_world.py`:

```python
from lib.types import IStdin, IStdout


def hello(stdin: IStdin, stdout: IStdout):
    stdout.write("Hello!\n")
```

To add to task list we should follow the algorithm:

1) Put `hello_world.py` to `./src`

2) Edit `tasks.py` as follows:

```python
def get_task(task_name):
	if task_name == "main":
		import src.main
		return src.main.main
    elif task_name == "hello_world":
        import src.hello_world
        return src.hello_world.hello
```

That's it! Now we can run 

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --task hello_world
Running in production at port 48755
</pre>

And
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 48755
Hello!
</pre>

## dev option

Instead of `prod` option you can also use `dev` option to run tasks locally with input and output through terminal:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc dev --task main
Hello, world!
What is your name? alex
Hello, alex!</pre>

## Docker

To build different tasks use `TASK_NAME` build-arg for `docker build`. By default `main` is used. Example of building and running `hello_world` task:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker build -t hello_world --build-arg TASK_NAME=hello_world .
Sending build context to Docker daemon  241.2kB
Step 1/6 : FROM python:3-alpine
 ---&gt; d4d4f50f871a
Step 2/6 : ARG TASK_NAME=main
 ---&gt; Using cache
 ---&gt; 0222c18af20f
Step 3/6 : ENV TASK_NAME ${TASK_NAME}
 ---&gt; Running in 5fd5f98e06c8
Removing intermediate container 5fd5f98e06c8
 ---&gt; ef1383b8c1a8
Step 4/6 : WORKDIR /chall
 ---&gt; Running in 066956d005b3
Removing intermediate container 066956d005b3
 ---&gt; 27bb54efdc66
Step 5/6 : COPY . .
 ---&gt; 36098a742746
Step 6/6 : CMD ./ctfnc prod --task ${TASK_NAME}
 ---&gt; Running in 8d8efffc0c04
Removing intermediate container 8d8efffc0c04
 ---&gt; e4c1cb13ff4a
Successfully built e4c1cb13ff4a
Successfully tagged hello_world:latest
<font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker run --net host --rm -it hello_world
Running in production at port 35733
</pre>

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/CTF</b></font>$ nc localhost 35733
Hello!</pre>