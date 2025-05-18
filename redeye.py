import rumps
import subprocess
import threading
import time
import sys
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.expanduser('~/redeye.log')),
        logging.StreamHandler(sys.stdout)
    ]
)

class RedEyeApp(rumps.App):
    def __init__(self):
        try:
            logging.info("Initializing RedEyeApp")
            super().__init__("👁️")  # Changed icon to eye emoji
            self.caffeinate_process = None
            self.timer_thread = None
            self.remaining_time = 0
            self.running = False
            
            # Menu items
            self.menu = [
                rumps.MenuItem("15 min", callback=self.start_timer),
                rumps.MenuItem("30 min", callback=self.start_timer),
                rumps.MenuItem("60 min", callback=self.start_timer),
                rumps.MenuItem("120 min", callback=self.start_timer),
                None,  # Separator
                rumps.MenuItem("Stop", callback=self.stop_caffeinate, key='s')
            ]
            # Hide the Stop button initially
            self.menu["Stop"].hidden = True
            logging.info("RedEyeApp initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing app: {str(e)}", exc_info=True)
            raise

    def start_timer(self, sender):
        try:
            logging.info(f"Starting timer with sender: {sender.title}")
            # Stop any existing timer
            if self.caffeinate_process:
                self.stop_caffeinate(None)
            
            duration = int(sender.title.split()[0])
            duration_seconds = duration * 60
            
            logging.info(f"Starting caffeinate process for {duration} minutes")
            self.caffeinate_process = subprocess.Popen(
                ['caffeinate', '-i', '-t', str(duration_seconds)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.remaining_time = duration
            self.running = True
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
            
            self.title = f"🔴 {self.remaining_time}m"  # Changed to red circle when active
            self.menu["Stop"].hidden = False
            logging.info("Timer started successfully")
            
        except Exception as e:
            logging.error(f"Error starting timer: {str(e)}", exc_info=True)
            rumps.notification(
                title="RedEye Error",
                subtitle="Failed to start",
                message=str(e)
            )

    def update_timer(self):
        try:
            logging.info("Starting timer update loop")
            while self.running and self.remaining_time > 0:
                self.title = f"🔴 {self.remaining_time}m"  # Changed to red circle when active
                time.sleep(60)
                self.remaining_time -= 1

            if self.running:  # If we finished counting down
                logging.info("Timer completed")
                self.stop_caffeinate(None)
        except Exception as e:
            logging.error(f"Error in update_timer: {str(e)}", exc_info=True)

    def stop_caffeinate(self, _):
        try:
            logging.info("Stopping caffeinate process")
            if self.caffeinate_process:
                self.running = False
                self.caffeinate_process.terminate()
                self.caffeinate_process = None
                self.title = "👁️"  # Changed icon to eye emoji
                self.menu["Stop"].hidden = True
                logging.info("Caffeinate process stopped successfully")
        except Exception as e:
            logging.error(f"Error stopping caffeinate: {str(e)}", exc_info=True)

if __name__ == '__main__':
    try:
        logging.info("Starting RedEyeApp")
        RedEyeApp().run()
    except Exception as e:
        logging.error(f"Fatal error in main: {str(e)}", exc_info=True)
        sys.exit(1)