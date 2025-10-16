from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

#定义一个初始化并返回调度器实例的函数。
def initialize_scheduler():
    scheduler.start()
    return scheduler


#    - 作用: 这个文件的核心任务是创建并启动一个调度器（Scheduler）。
#    - from apscheduler.schedulers.background import BackgroundScheduler: 这行代码从 apscheduler 库中导入 BackgroundScheduler 类。BackgroundScheduler 是一种可以在后台运行任务的调度器，它不会阻塞主程序的执行。
#    - scheduler = BackgroundScheduler(): 这里创建了 BackgroundScheduler 的一个实例，我们后续将用它来管理任务。
#    - initialize_scheduler(): 这个函数封装了启动调度器的逻辑。
#        - scheduler.start(): 启动调度器。一旦启动，它就会在后台线程中等待执行任务。
#        - return scheduler: 返回已经启动的调度器实例，以便其他文件（如 main.py）可以使用它。

#   小结: scheduler.py 提供了一个已经配置好并启动的后台调度器。
