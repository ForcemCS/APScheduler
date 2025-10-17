import time
import asyncio

# 同步函数
def sync_task(task_name):
    print(f"开始同步任务: {task_name}")
    time.sleep(2)  # 模拟耗时操作
    print(f"完成同步任务: {task_name}")

def sync_main():
    print("--- 开始同步执行 ---")
    start_time = time.time()
    sync_task("任务1")
    sync_task("任务2")
    end_time = time.time()
    print(f"同步执行总耗时: {end_time - start_time:.2f} 秒")
    print("--- 同步执行结束 ---\n")

# 异步函数
# async def: 这定义了一个协程函数 (coroutine function)。调用它不会立即执行代码，而是返回一个协程对象。
async def async_task(task_name):
    print(f"开始异步任务: {task_name}")
    # await: 这是 async 的关键所在。它告诉事件循环：“这个操作（asyncio.sleep(2)）需要等待，在我等待的时候，你可以去执行其他任务”。因此，当 "任务A" 在 await 时，事件循环可以切换去执行 "任务B"。
    await asyncio.sleep(2)  # 模拟耗时操作，使用 await 等待
    print(f"完成异步任务: {task_name}")

async def async_main():
    print("--- 开始异步执行 ---")
    start_time = time.time()
    # asyncio.gather(): 这个函数接收一个或多个协程，并并发地运行它们。它会等待所有任务都完成。
    await asyncio.gather(
        async_task("任务A"),
        async_task("任务B")
    )
    end_time = time.time()
    print(f"异步执行总耗时: {end_time - start_time:.2f} 秒")
    print("--- 异步执行结束 ---")

# __name__ (注意前后是双下划线) 是 Python 中一个特殊的内置变量。对于每一个 .py 文件（Python称之为“模块”），解释器在运行它之前都会自动给这个变量赋值。
# 它的值取决于你是如何运行这个 .py 文件的。
# 当你通过命令行直接执行一个文件时, Python 解释器会将这个被直接执行的文件的 __name__ 变量设置为字符串 __main__。

# 这个 if 语句的作用就是判断当前脚本是被直接执行，还是被当作模块导入。
if __name__ == "__main__":
    sync_main()
    #asyncio.run(): 这是启动 asyncio 程序的入口。它负责创建事件循环，运行你指定的 async 函数，并在完成后关闭循环。
    asyncio.run(async_main())