import sys
import subprocess
import signal

# Get the number of sensor processes to run from the command line arguments
if len(sys.argv) < 2:
    print("Please provide a number of sensors to simulate as an argument")
    sys.exit(1)
num_sensors = int(sys.argv[1])

# List to store the child process objects
child_processes = []

try:
    # Run a separate process for each sensor
    for i in range(num_sensors):
        child_process = subprocess.Popen(["python", "sensor.py", str(i)])
        child_processes.append(child_process)
    
    # Wait for child processes to finish
    for child_process in child_processes:
        child_process.wait()
except KeyboardInterrupt:
    # Terminate child processes if main process receives KeyboardInterrupt signal
    for child_process in child_processes:
        child_process.send_signal(signal.SIGINT)
        child_process.wait()