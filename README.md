# ctf-nc-framework #
A tiny framework to run python challenges in raw TCP.

## Install
Just clone this repo and you are ready to go. 

To test it run:
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --task main
Running in production at port 9001
</pre>

And connect with `nc`:
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 9001
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
Running in production at port 9001
</pre>

And
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 48755
Hello!
</pre>

### Port binding

There is an option `--port` to bind running task to a particular network port. You can set it to `random` to let system give it a random port. Example:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --port random --task hello_world
Running in production at port 35839
</pre>

You can use some particular number. Like this:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --port 1337 --task hello_world
Running in production at port 1337
</pre>

Or you can use `default` value wich will bind port to a `CTFNC_PORT` value set in the `./config/config.py`. You can omit `--port` option to use default port:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --task hello_world
Running in production at port 9001</pre>

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc prod --port default --task hello_world
Running in production at port 9001</pre>

## dev option

Instead of `prod` option you can also use `dev` option to run tasks locally with input and output through terminal:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ ./ctfnc dev --task main
Hello, world!
What is your name? alex
Hello, alex!</pre>

## Docker

Docker build file has two parameters to specify:

1. `TASK_NAME` - used to run a particular task on `docker run <image>`. By default `main` is used.
2. `TASK_PORT` - used to specify which port to use when running the task. By default `CTFNC_PORT` value is used from `./config/config.py` but that won't work if you're going to use `--net host` option for `docker run` to run multiple tasks on the same host. So you can specify a particular port. But without using `--net host` option it's fine to omit this option during build.

Examples of Docker builds:

1. With `TASK_PORT` option.
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker build -t hello_world --build-arg TASK_NAME=hello_world --build-arg TASK_PORT=13337 .
Sending build context to Docker daemon  308.2kB
Step 1/8 : FROM python:3-alpine
 ---&gt; d4d4f50f871a
Step 2/8 : ARG TASK_NAME=main
 ---&gt; Using cache
 ---&gt; 0222c18af20f
Step 3/8 : ARG TASK_PORT=default
 ---&gt; Running in cddcffff08ce
Removing intermediate container cddcffff08ce
 ---&gt; f38b5f4fd6ec
Step 4/8 : ENV TASK_NAME ${TASK_NAME}
 ---&gt; Running in 7b19e72ceb56
Removing intermediate container 7b19e72ceb56
 ---&gt; 948154aead5c
Step 5/8 : ENV TASK_PORT ${TASK_PORT}
 ---&gt; Running in 4ee8a247cbca
Removing intermediate container 4ee8a247cbca
 ---&gt; 4aad6d300cb1
Step 6/8 : WORKDIR /chall
 ---&gt; Running in 1846363f1513
Removing intermediate container 1846363f1513
 ---&gt; 033af5afaa0c
Step 7/8 : COPY . .
 ---&gt; cfc18a60aa84
Step 8/8 : CMD ./ctfnc prod --port ${TASK_PORT} --task ${TASK_NAME}
 ---&gt; Running in b119846beaa8
Removing intermediate container b119846beaa8
 ---&gt; 263d08203690
Successfully built 263d08203690
Successfully tagged hello_world:latest</pre>

2. Without `TASK_PORT` option.
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker build -t hello_world --build-arg TASK_NAME=hello_world .
Sending build context to Docker daemon  308.2kB
Step 1/8 : FROM python:3-alpine
 ---&gt; d4d4f50f871a
Step 2/8 : ARG TASK_NAME=main
 ---&gt; Using cache
 ---&gt; 0222c18af20f
Step 3/8 : ARG TASK_PORT=default
 ---&gt; Using cache
 ---&gt; f38b5f4fd6ec
Step 4/8 : ENV TASK_NAME ${TASK_NAME}
 ---&gt; Using cache
 ---&gt; 948154aead5c
Step 5/8 : ENV TASK_PORT ${TASK_PORT}
 ---&gt; Running in e55c4bcabb5d
Removing intermediate container e55c4bcabb5d
 ---&gt; b1e2832a4410
Step 6/8 : WORKDIR /chall
 ---&gt; Running in 51e70a070c2f
Removing intermediate container 51e70a070c2f
 ---&gt; c945a6541c7a
Step 7/8 : COPY . .
 ---&gt; 62abac159062
Step 8/8 : CMD ./ctfnc prod --port ${TASK_PORT} --task ${TASK_NAME}
 ---&gt; Running in df114cf0e390
Removing intermediate container df114cf0e390
 ---&gt; 3d215bbbfaa8
Successfully built 3d215bbbfaa8
Successfully tagged hello_world:latest
</pre>

3. With `TASK_PORT=random` option (to use random port mapping). This will prevent conflicts on `docker run` with `--net host` option, but you can't know the port until you run the container.
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker build -t hello_world --build-arg TASK_NAME=hello_world --build-arg TASK_PORT=random .
Sending build context to Docker daemon  308.2kB
Step 1/8 : FROM python:3-alpine
 ---&gt; d4d4f50f871a
Step 2/8 : ARG TASK_NAME=main
 ---&gt; Using cache
 ---&gt; 0222c18af20f
Step 3/8 : ARG TASK_PORT=default
 ---&gt; Using cache
 ---&gt; f38b5f4fd6ec
Step 4/8 : ENV TASK_NAME ${TASK_NAME}
 ---&gt; Using cache
 ---&gt; 948154aead5c
Step 5/8 : ENV TASK_PORT ${TASK_PORT}
 ---&gt; Running in 470dba0ab817
Removing intermediate container 470dba0ab817
 ---&gt; 8f64e70a9bf2
Step 6/8 : WORKDIR /chall
 ---&gt; Running in bd1fee085dd6
Removing intermediate container bd1fee085dd6
 ---&gt; dcb20c357fd5
Step 7/8 : COPY . .
 ---&gt; 8a4b21bb7efd
Step 8/8 : CMD ./ctfnc prod --port ${TASK_PORT} --task ${TASK_NAME}
 ---&gt; Running in 4f89080ec0cb
Removing intermediate container 4f89080ec0cb
 ---&gt; c1500b5b103f
Successfully built c1500b5b103f
Successfully tagged hello_world:latest
</pre>

When you don't use `--net host` option (which seems to be not working on Windows and OS X anyway) Docker will run the task on its own virtual network. So you will not have access to the port your task is bound to:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker run --rm -it hello_world
Running in production at port 9001</pre>

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 9001
<font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ 
</pre>

So you will have to publish the application on the particular port on the host:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ sudo docker run --rm -p 43584:9001 -it hello_world
Running in production at port 9001</pre>

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents/ctf-nc-framework</b></font>$ nc localhost 43584
Hello!</pre>