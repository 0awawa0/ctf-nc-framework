

def get_task(task_name):
	if task_name == "main":
		import src.main
		return src.main.main
	elif task_name == "hello_world":
		import src.hello_world
		return src.hello_world.hello
	elif task_name == "matrix2bytes":
		import src.ctf_tasks.matrix2bytes.main
		return src.ctf_tasks.matrix2bytes.main.main
	elif task_name == "add_round_key":
		import src.ctf_tasks.add_round_key.main
		return src.ctf_tasks.add_round_key.main.main
	elif task_name == "sbox":
		import src.ctf_tasks.sbox.sbox
		return src.ctf_tasks.sbox.sbox.main
