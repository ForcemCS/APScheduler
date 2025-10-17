```
async def async_hello_world():
    now = time.time()
    await asyncio.sleep(1)
    print(time.time() - now)
    print("Hello, world!")
    await asyncio.sleep(1)
    print(time.time() - now)
```

这个coroutine执行需要两秒
1.执行到第一个 await asyncio.sleep(1)：
  当前协程挂起，让出控制权。
  事件循环（event loop）可以去运行别的协程。
2.1 秒后，这个协程恢复执行，打印 "Hello"。
  执行到第二个 await asyncio.sleep(1)：
  又挂起，让出控制权。
3.事件循环又去运行别的协程。
  再过 1 秒，恢复执行，打印 "World"。