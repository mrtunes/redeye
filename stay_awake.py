import rumps
import subprocess
import threading
import time

class StayAwakeApp(rumps.App):
    def __init__(self):
        super().__init__("⚡️")  # Using text indicator instead of icon file
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

    def start_timer(self, sender):
        # Stop any existing timer
        if self.caffeinate_process:
            self.stop_caffeinate(None)
        
        try:
            duration = int(sender.title.split()[0])
            duration_seconds = duration * 60
            
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
            
            self.title = f"⏰ {self.remaining_time}m"
            self.menu["Stop"].hidden = False
            
        except Exception as e:
            rumps.notification(
                title="Stay Awake Error",
                subtitle="Failed to start",
                message=str(e)
            )

    def update_timer(self):
        while self.running and self.remaining_time > 0:
            self.title = f"⏰ {self.remaining_time}m"
            time.sleep(60)
            self.remaining_time -= 1

        if self.running:  # If we finished counting down
            self.stop_caffeinate(None)

    def stop_caffeinate(self, _):
        if self.caffeinate_process:
            self.running = False
            self.caffeinate_process.terminate()
            self.caffeinate_process = None
            self.title = "⚡️"
            self.menu["Stop"].hidden = True

if __name__ == '__main__':
    StayAwakeApp().run() 