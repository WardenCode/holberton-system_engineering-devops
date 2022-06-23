# 0x07. Networking basics #0

This project is about topics of Networking. Based in question and answers.

## Tasks:

- **0-OSI\_model** &rarr; In this project we will mainly focus on:

	- The Transport layer and especially TCP/UDP
	- On the Network layer with IP and ICMP

	### Questions:

		1. What is the OSI model?
		2. How is the OSI model organized?

- **1-types\_of\_network** &rarr; LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

	### Questions:

		1. What type of network a computer in local is connected to?

		2. What type of network could connect an office in one building to another office in a building a few streets away?

		3. What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

- **2-MAC_and_IP_address** &rarr; About MAC and IP address.

	### Questions:
		1. What is a MAC address?
		2. What is an IP address?

- **3-UDP_and_TCP**

	### Statements:

	**Which statement is correct for the TCP box:**

		1. It is a protocol that is transferring data in a slow way but surely
		2. It is a protocol that is transferring data in a fast way and might loss data along in the process

	**Which statement is correct for the UDP box:**

		1. It is a protocol that is transferring data in a slow way but surely
		2. It is a protocol that is transferring data in a fast way and might loss data along in the process

	**Which statement is correct for the TCP worker:**

		1. Have you received boxes x, y, z?
		2. May I increase the rate at which I am sending you boxes?

- **4-TCP_and_UDP_ports** &rarr; Write a Bash script that displays listening ports:

	### Requirements:
		- That only shows listening sockets
		- That shows the PID and name of the program to which each socket belongs

- **5-is_the_host_on_the_network** &rarr; Write a Bash script that pings an IP address passed as an argument.

	### Requirements:

		- Accepts a string as an argument
		- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
		- Ping the IP 5 times
