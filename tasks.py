

def get_task(task_name):
	if task_name == "main":
		import src.main
		return src.main.main
	elif task_name == "hello":
		import src.ezTask.main
		return src.ezTask.main.main