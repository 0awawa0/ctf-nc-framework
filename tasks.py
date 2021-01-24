

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
	elif task_name == "permutation":
		import src.ctf_tasks.permutation.permutation
		return src.ctf_tasks.permutation.permutation.main
	elif task_name == "sbox":
		import src.ctf_tasks.sbox.sbox
		return src.ctf_tasks.sbox.sbox.main
	elif task_name == "full_aes":
		import src.ctf_tasks.full_aes.full_aes
		return src.ctf_tasks.full_aes.full_aes.main
	elif task_name == "riddler":
		import src.ctf_tasks.riddler.riddler
		return src.ctf_tasks.riddler.riddler.main
	elif task_name == "guess_the_melody":
		import src.ctf_tasks.guess_the_melody.guess_the_melody
		return src.ctf_tasks.guess_the_melody.guess_the_melody.main
	elif task_name == "guess_the_number":
		import src.ctf_tasks.guess_the_number.guess_the_number
		return src.ctf_tasks.guess_the_number.guess_the_number.main
	elif task_name == "bulls_and_cows":
		import src.ctf_tasks.bulls_and_cows.bulls_and_cows
		return src.ctf_tasks.bulls_and_cows.bulls_and_cows.main
	elif task_name == "repeater":
		import src.ctf_tasks.repeater.repeater
		return src.ctf_tasks.repeater.repeater.main
	elif task_name == "passwords_as_keys":
		import src.ctf_tasks.passwords_as_keys.passwords_as_keys
		return src.ctf_tasks.passwords_as_keys.passwords_as_keys.main
	elif task_name == "ecb_oracle":
		import src.ctf_tasks.ecb_oracle.ecb_oracle
		return src.ctf_tasks.ecb_oracle.ecb_oracle.main
	elif task_name == "ecb_cbc_wtf":
		import src.ctf_tasks.ecb_cbc_wtf.ecb_cbc_wtf
		return src.ctf_tasks.ecb_cbc_wtf.ecb_cbc_wtf.main
	elif task_name == "flipping_cookie":
		import src.ctf_tasks.flipping_cookie.flipping_cookie
		return src.ctf_tasks.flipping_cookie.flipping_cookie.main
