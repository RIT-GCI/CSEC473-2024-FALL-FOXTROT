Rachel Leone

Distraction --> Desktop Goose

Script:
This ansible script installs Desktop Goose on all the Windows machines. The script creates a folder, downloads and unzips the Desktop Goose files, and then runs the application.

Additionally, it sets up a scheduled task to monitor the application, ensuring it is reinstalled and restarted if it gets closed.

Deployment:
- Make sure that Ansible is installed on the targeted machines
- Run the playbook
