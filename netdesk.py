import time
import psutil
from plyer import notification

def check_internet():
    try:
        # Attempt to resolve a well-known domain
        psutil.net_if_addrs()
        return True
    except Exception:
        return False

def send_notification(message):
    notification.notify(
        title='Internet Status Change',
        message=message,
        app_name='Internet Status Notifier'
    )

def main():
    was_connected = check_internet()
    
    while True:
        is_connected = check_internet()
        
        if is_connected != was_connected:
            if is_connected:
                send_notification('Internet Connected')
            else:
                send_notification('Internet Disconnected')
            
            was_connected = is_connected
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == '__main__':
    main()
