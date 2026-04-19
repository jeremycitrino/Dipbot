# service.py
import os
import sys
from time import sleep

# Import your bot's main entry point
# Ensure nostop.py is in the same directory
sys.path.append(os.path.dirname(__file__))

# If nostop.py defines start_bot(), call it
if __name__ == '__main__':
    # The service will run this script; we need to import and start the bot
    # Assuming nostop.py has a function start_bot() that starts the bot threads
    import nostop
    nostop.start_bot()
    
    # Keep the service alive
    while True:
        sleep(1)
