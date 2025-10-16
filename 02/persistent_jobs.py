from scheduler import initialize_scheduler
import time
from datetime import datetime

def volatile_job():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Volatile job (in-memory)")

def persistent_job():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Persistent job (in SQLite)")

# Initialize scheduler with our job stores
scheduler = initialize_scheduler()

# Check if persistent job already exists (after restart)
existing_job = scheduler.get_job('persistent_job', jobstore='persistent')
if not existing_job:
    print("First run - adding persistent job")
    # Add a job to the persistent store
    scheduler.add_job(
        persistent_job, 
        'interval', 
        seconds=15, 
        id='persistent_job',
        jobstore='persistent'  # Specify the job store
    )
else:
    print("Job already exists - loaded from SQLite")

# Always add the volatile job (it won't survive restarts)
scheduler.add_job(
    volatile_job, 
    'interval', 
    seconds=10, 
    id='volatile_job'
)

print("Scheduler started with both volatile and persistent jobs")
print("The persistent job will survive application restarts")
print("Press Ctrl+C to exit")

try:
    # Keep the main thread alive
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler shut down")
