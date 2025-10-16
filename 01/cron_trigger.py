from apscheduler.schedulers.background import BackgroundScheduler
import time

def cron_task():
    print(f"Cron job executed at: {time.strftime('%H:%M:%S')}")

scheduler = BackgroundScheduler()
scheduler.start()

# second=15`: 这是 cron 触发器的参数。它指定了任务应该在每分钟的第 15 秒执行
scheduler.add_job(cron_task, 'cron', second=15)

print("Job will execute at the 15-second mark of every minute")
print("Press Ctrl+C to exit")

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()



# # Every weekday at 9 AM
# scheduler.add_job(job_function, 'cron', day_of_week='mon-fri', hour=9)

# # Every 5 minutes during business hours
# scheduler.add_job(job_function, 'cron', 
#                   day_of_week='mon-fri', 
#                   hour='9-17', 
#                   minute='*/5')

# # First day of every month at midnight
# scheduler.add_job(job_function, 'cron', day=1, hour=0, minute=0)
