# 0x05. Processes and signals

Project of Bash, about Processes and Signals.

## Tasks:

Exist two types of tasks in this project:

- Mandatory

- Advanced

### Mandatory

- 0-what-is-my-pid &rarr; Displays its own PID.

- 1-list_your_processes &rarr; Displays a list of currently running processes.

- 2-show_your_bash_pid &rarr; Displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

- 3-show_your_bash_pid_made_easy &rarr; Displays the PID, along with the process name, of processes whose name contain the word bash.

- 4-to_infinity_and_beyond &rarr; Displays To infinity and beyond indefinitely.

- 5-dont_stop_me_now &rarr; Stops 4-to_infinity_and_beyond process.

- 6-stop_me_if_you_can &rarr; Stops 4-to_infinity_and_beyond process.

- 7-highlander &rarr; Displays:

	- To infinity and beyond indefinitely
	- With a sleep 2 in between each iteration
	- I am invincible!!! when receiving a SIGTERM signal

- 8-beheaded_process &rarr; kills the process 7-highlander.

### Advanced

- 100-process_and_pid_file &rarr; Bash script that:

	- Creates the file /var/run/myscript.pid containing its PID.
	- Displays To infinity and beyond indefinitely.
	- Displays I hate the kill command when receiving a SIGTERM signal.
	- Displays Y U no love me?! when receiving a SIGINT signal.
	- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal.

- 101-manage_my_process, manage_my_process:
	- Write a manage_my_process Bash script that:

		- Indefinitely writes I am alive! to the file /tmp/my_process.
		- In between every I am alive! message, the program should pause for 2 seconds.

	- Write Bash (init) script 101-manage_my_process that manages manage_my_process.

- 102-zombie.c &rarr; C program that creates 5 zombie processes.

- 103-screencast_unix_signal &rarr; Create a screencast where you live-code/demo something related to Unix signals.
