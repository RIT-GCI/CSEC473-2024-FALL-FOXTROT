# Joseph Cremeno

# define path to LogCleaner.ps1
$scriptPath = '"C:\Users\Administrator\Desktop\jc6872-LogClear\LogCleaner.ps1"'

# Create task that runs the LogCleaner script
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File $scriptPath"

# Run task every 3 minutes
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(5) -RepetitionInterval (New-TimeSpan -Minutes 3)

# Register task to run as system
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "LogCleaner" -Description "Cleans event logs regularly" -User "SYSTEM" -RunLevel Highest