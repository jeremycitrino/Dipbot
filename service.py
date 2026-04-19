# service.py
import os
import sys
from time import sleep

# Add the current directory to Python path so we can import nostop
sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':
    import nostop
    nostop.start_bot()
    
    # Keep service alive
    while True:
        sleep(1)
