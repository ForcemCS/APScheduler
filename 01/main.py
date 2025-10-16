from scheduler import initialize_scheduler
import time

def hello_job():
    print("Hello, APScheduler!")

#初始化并运行一个 APScheduler 实例。
scheduler = initialize_scheduler()
scheduler.add_job(hello_job, 'interval', seconds=5)

try:
    # Keep the main thread alive to allow the scheduler to run
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

    
#    - 作用: 这个文件是程序的入口，它定义了要执行的具体任务，并使用 scheduler.py 中创建的调度器来安排这个任务。
#    - from scheduler import initialize_scheduler: 从我们刚才分析的 scheduler.py 文件中导入 initialize_scheduler 函数。
#    - def hello_job():: 定义了一个名为 hello_job 的简单函数。这个函数只是打印一条信息。这就是我们希望定时执行的任务。
#    - scheduler = initialize_scheduler(): 调用函数获取一个已经启动的调度器实例。
#    - scheduler.add_job(hello_job, 'interval', seconds=5): 这是最关键的一步，它向调度器添加了一个新任务：
#        - hello_job: 要执行的函数。
#        - 'interval': 任务的触发方式。'interval' 表示“每隔一段时间执行”。
#        - seconds=5: 时间间隔，这里设置为5秒。
#        - 综合起来: 这行代码告诉调度器：“请每隔5秒钟执行一次 hello_job 函数”。
#    - while True: time.sleep(1): 这是一个无限循环，目的是保持主线程不退出。因为我们的调度器是在后台线程运行的，如果主线程（即 main.py 脚本）执行完毕并退出了，后台的调度器线程也会随之被销毁，任务也就不会再执行了。
#    - except (KeyboardInterrupt, SystemExit): scheduler.shutdown(): 这是一个优雅的退出机制。当你按下 Ctrl+C 想要停止程序时，它会捕获到 KeyboardInterrupt 异常，然后调用 scheduler.shutdown() 来安全地关闭调度器，确保所有任务都正确停止。
