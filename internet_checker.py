import subprocess
import time
import socket
import platform

PING_TARGET = "8.8.8.8"  # Default ping target (Google's DNS server)
LOG_FILE = "internet_checker_log.txt"  # Log file to save connection status

def check_internet():
    try:
        # Check if there is internet connectivity by pinging the target
        output = subprocess.check_output(["ping", "-c", "1", PING_TARGET], stderr=subprocess.STDOUT, universal_newlines=True)
        if "1 packets transmitted, 1 received" in output:
            return True, output
        else:
            return False, output
    except subprocess.CalledProcessError as e:
        return False, e.output

def get_ip_address():
    try:
        # Get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return "N/A"

def get_network_interface():
    try:
        # Get the network interface name
        if platform.system() == "Linux":
            interface = subprocess.check_output(["ip", "route", "get", "8.8.8.8"], universal_newlines=True).split(" ")[4]
        elif platform.system() == "Darwin":  # macOS
            interface = subprocess.check_output(["route", "get", "8.8.8.8"], universal_newlines=True).split("\n")[1].split(":")[-1].strip()
        else:
            interface = "N/A"
        return interface
    except Exception as e:
        return "N/A"

def notify(status, output):
    if status:
        print("[INFO] Internet connection is up!")
        print(output)
    else:
        print("[WARNING] Internet connection is down!")
        print(output)

def log_status(status):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp}: {'Up' if status else 'Down'}\n")

def main():
    internet_status = False  # Initialize with False to handle the case where the script starts without internet

    while True:
        new_internet_status, ping_output = check_internet()

        if new_internet_status != internet_status:
            notify(new_internet_status, ping_output)
            log_status(new_internet_status)

        internet_status = new_internet_status
        time.sleep(5)  # Adjust the interval between checks as needed

if __name__ == "__main__":
    main()
