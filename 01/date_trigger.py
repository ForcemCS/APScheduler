from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import time

def one_time_job():
    print(f"Job executed at: {datetime.now().strftime('%H:%M:%S')}")

scheduler = BackgroundScheduler()
scheduler.start()

# Schedule job to run 10 seconds from now
run_date = datetime.now() + timedelta(seconds=10)
scheduler.add_job(one_time_job, 'date', run_date=run_date)

print(f"Job scheduled for: {run_date.strftime('%H:%M:%S')}")
print("Press Ctrl+C to exit")

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    
#    1. `scheduler = BackgroundScheduler()`:
#        * 创建 BackgroundScheduler 的一个实例。

#    2. `scheduler.start()`:
#        * 启动后台调度器。

#    3. `run_date = datetime.now() + timedelta(seconds=10)`:
#        * 这行代码计算出了任务的执行时间。它获取当前时间 (datetime.now())，然后加上10秒 (timedelta(seconds=10))。所以，run_date 变量就包含了10秒后的那个精确时间点。

#    4. `scheduler.add_job(one_time_job, 'date', run_date=run_date)`:
#        * 这是最核心的一步。它向调度器添加了一个新任务。
#        * one_time_job: 这是要执行的函数。
#        * 'date': 这是触发器的类型。date 触发器表示这个任务只会在一个特定的日期和时间点执行一次。
#        * run_date=run_date: 这指定了任务执行的具体时间，也就是我们刚刚计算出的10秒后的时间。

#    5. `print(...)`:
#        * 打印出任务被安排在何时执行，以及提示用户如何退出程序。

#    6. `try...while...except` 块:
#        * 因为调度器是在后台线程运行的，主程序需要保持活动状态，否则程序会立即退出，调度器也就没有机会执行任务了。
#        * while True: time.sleep(1) 创建了一个无限循环，让主程序一直“睡眠”，每秒钟醒来一次，但什么也不做。这有效地保持了程序的运行。
#        * except (KeyboardInterrupt, SystemExit): scheduler.shutdown() 捕获用户按 Ctrl+C 的中断信号，然后安全地关闭调度器，清理所有资源。

#   总结一下:

#   date_trigger.py 的作用是：定义一个简单的打印时间的任务，然后使用 date 触发器精确地安排这个任务在10秒后执行一次。为了确保任务能被执行，它让主程序一直运行，直到用户手动停止它。

#   这个例子清晰地展示了 date 触发器的用途：当你需要一个任务在某个绝对的时间点（例如 “2025年12月25日 00:00:00”）执行且仅执行一次时，date 触发器是最佳选择。
