import sys
import time
import threading

# Function to display the loading animation

def loading_animation():
    animation = ['|', '/', '-', '\']  # Animation frames
    while True:
        for frame in animation:
            sys.stdout.write('\rLoading... ' + frame)
            sys.stdout.flush()
            time.sleep(0.1)

# Start the animation in a separate thread
animation_thread = threading.Thread(target=loading_animation)
animation_thread.daemon = True  # Daemonize thread
animation_thread.start()

# Simulate a long-running process
try:
    time.sleep(10)  # Simulate work being done for 10 seconds
finally:
    sys.stdout.write('\rDone!')
    sys.stdout.flush()