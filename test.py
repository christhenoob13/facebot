import psutil
import platform
import os
import subprocess

# CPU usage (percentage)
cpu_usage = psutil.cpu_percent(interval=1)

# RAM usage (in percentage)
ram_usage = psutil.virtual_memory().percent

# Number of CPU cores
cpu_cores = psutil.cpu_count(logical=False)  # Physical cores
logical_cores = psutil.cpu_count(logical=True)  # Logical (virtual) cores

# Ping test (using subprocess to call a system ping command)
def get_ping(host="google.com"):
    try:
        # For Windows, use 'ping -n' and for Linux/Mac, use 'ping -c'
        response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            return "Ping successful"
        else:
            return "Ping failed"
    except Exception as e:
        return str(e)

# Operating system platform
os_platform = platform.system()

# CPU architecture (32-bit or 64-bit)
cpu_architecture = platform.architecture()[0]

# Display all the collected information
print(f"CPU Usage: {cpu_usage}%")
print(f"RAM Usage: {ram_usage}%")
print(f"CPU Cores: {cpu_cores} physical cores, {logical_cores} logical cores")
print(f"Ping Test: {get_ping()}")
print(f"Operating System Platform: {os_platform}")
print(f"CPU Architecture: {cpu_architecture}")
