Overview:
This project implements a Command and Control (C2) server designed to remotely execute commands and manage clients securely. The architecture consists of a server that communicates with multiple clients, allowing for command execution and file transfer.

Features:
1. Remote Command Execution: Execute commands on client machines.
2. File Management: Upload files to clients.
3. Obfuscation: Communications are disguised to appear like basic web communication

Installation:

Prerequisites:
1. Python3

Clone the git repo on the machine you intend to be the server, set up an Ansible to deploy the client on the target machines, run the ansible-playbook, and the client will be started on the client. Start the C2Server using Python on the server and wait for clients to connect. 

Usage:
1. The server interface lists a number of available commands. 

Options:

1. Displays a list of known clients (WILL NOT UPDATE IF CLIENT CONNECTION IS LOST)

2. Select a client to interact with
To select another client, reselect the original client to deselect them and then select the new target

3. Sends any Linux command to the selected client to be run. 
This will sleep for 5 seconds before allowing any further input to wait for the output from the client. Sometimes, the client will take longer to respond than 5 seconds as the clients implement a back-off strategy to reduce the amount of network traffic sent to and from the client. You may either wait for the output or move on from this screen. Either way the output will be displayed, but it may be disruptive elsewhere.

4. Stages a file to be sent to the client's working directory. The file will only be sent upon the next command being sent to the client. This is to reduce the amount of network traffic. 

5. Closes the server
