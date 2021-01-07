

def get_task(task_name):
	if task_name == "main":
		import src.main
		return src.main.main
	elif task_name == "hello_world":
		import src.hello_world
		return src.hello_world.hello
	elif task_name == "matrix2bytes":
		import src.matrix2bytes.main
		return src.matrix2bytes.main.main
