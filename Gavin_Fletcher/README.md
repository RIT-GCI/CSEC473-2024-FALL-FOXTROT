How to use each tool:</br>

**grass.py**

 REQUIREMENTS </br>
*Access to Sudo ONLY IF "pynput" is not installed.*
*If you can prebake, run command **"sudo apt install python3-pynput -y"***

1. Make sure that when you SSH into the box you do "-X" to allow for X11 forwarding
    ![image](https://github.com/user-attachments/assets/a01fbcfd-0784-4a41-9496-72378373d33c)

2. wget using the file link: https://raw.githubusercontent.com/gfletcher0311/CDT_redTeamTool/refs/heads/main/grass.py

3. Run "python3 grass.py" from ssh</br>
![image](https://github.com/user-attachments/assets/4572955f-273c-4bb0-bc17-8b3bf242c2a5)

Now whenever the target machine presses the "enter" key, a terminal of grass will pop up, making it extemeley difficult to continue working on the machine until the file is deleted or the SSH session is closed.
