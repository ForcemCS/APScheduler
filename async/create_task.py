import asyncio
import random

async def fetch_server_status(server_id):
    print(f"开始查询服务器 {server_id}")
    await asyncio.sleep(random.uniform(1, 3))  # 模拟IO
    print(f"完成服务器 {server_id}")
    return f"server_{server_id}_ok"

async def main():
    # 先启动所有任务
    tasks = [asyncio.create_task(fetch_server_status(i)) for i in range(3)]
    
    print("任务都启动了，但我可以先做别的事...")
    await asyncio.sleep(0.5)
    print("现在再去等结果")

    # 等待某个结果（或者全部结果）
    results = await asyncio.gather(*tasks)
    print("所有任务结果:", results)

asyncio.run(main())



# 主协程开始运行 main()
# ↓
# 执行 for 循环，创建 3 个任务
# ↓
# 每个 create_task() 把 fetch_server_status(i) 注册到事件循环中
# ↓
# print("任务都启动了，但我可以先做别的事...")
# ↓
# await asyncio.sleep(0.5)
#     ↳ 在这 0.5 秒里，事件循环调度那 3 个任务运行！
# ↓
# 当 sleep(0.5) 结束，主协程恢复执行，执行 print("现在再去等结果")
# ↓
# await asyncio.gather(*tasks)
#     ↳ 等待所有任务完成