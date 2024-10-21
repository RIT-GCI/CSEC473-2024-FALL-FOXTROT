Arianna Schwartz

Tool: Phantom

Script:

The Phantom tool is a distraction tool which makes an ascii ghost float in the user's terminal and then closes the terminal
The ghost is configured to "fly" around the terminal for a few seconds before a message is printed stating that the terminal will "disappear"
The ascii ghost and its movement, as well as the closing of the terminal is configured in the ghost_magic.sh file. 
To run this script, the command ./ghost_magic.sh can be ran, assuming the user is in the same directory as the script. 
Keep in mind this script will close your terminal every time you run it. 
In addition, this script catches the ctr+c command and renders it useless, so ctrl+c cannot be used to exit out of the script

Deployment:

The file phantomctl.yaml can be used to deploy this tool on all linux machines in the competition via ansible.
This file creates a new directory in /etc called cron.yearly and copies the ghost_magic.sh scipt into it with the name phantomctl.sh
The /etc/cron.yearly directory is then configured to run every 5 minutes.
The command to run the ansible is ansible-playbook -i inventory.ini phantomctl.yaml
