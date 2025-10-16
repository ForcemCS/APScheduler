from apscheduler.schedulers.background import BackgroundScheduler
import time

def scheduled_task():
    print(f"Interval job executed at: {time.strftime('%H:%M:%S')}")

scheduler = BackgroundScheduler()
scheduler.start()

# Run job every 5 seconds
scheduler.add_job(scheduled_task, 'interval', seconds=5)

print("Job scheduled to run every 5 seconds")
print("Press Ctrl+C to exit")

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
