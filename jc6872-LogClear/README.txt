Important Run Info

The script "LogCleaner" is a script that removes all security, system, and application logs

The script "LogUpdater" creates a scheduled task that runs "LogCleaner" every three minutes.

In the script "LogUpdater" the line, "$scriptPath = '"C:\Users\Administrator\Desktop\jc6872-LogClear\LogCleaner.ps1"'"
	can be changed to direct the LogUpdater towards the correct location of LogCleaner.

The current script path is the location of LogCleaner on the 'jc6872-WindowsTarget' openstack machine.
	The administrator password for the 'jc6872-WindowsTarget' is 'Admin123'

The scheduled task can be verified using the command "Get-ScheduledTask -TaskName "LogCleaner" | Get-ScheduledTaskInfo"

This script should be ran as administrator and is intended to be prebaked.