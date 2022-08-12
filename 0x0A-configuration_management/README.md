
Project of Puppet, about configuration management.

## Tasks:

Exist two types of tasks in this project:

- Mandatory

### Mandatory

- **0-create_a_file.pp** &rarr; Create a file called school in `/tmp`.

	### Requirements:
	- File path is `/tmp/school`.
	- File permission is `0744`.
	- File group is `www-data`.
	- File contains `I love Puppet`.

---

- **1-install_a_package.pp** &rarr; Install `flask` from `pip3`.

	### Requirements:
	- Install `flask`.
	- Version must be `2.1.0`.

---

- **2-execute_a_command.pp** &rarr; Create a manifest that kills a process named `killmenow`.

	### Requirements:
	- Must use the `exec` Puppet resource.
	- Must use `pkill`.