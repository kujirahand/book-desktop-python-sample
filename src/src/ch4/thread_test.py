import time
from threading import Thread

# 仕事をする関数 --- (*1)
def do_work(no):
    print(f">>> 仕事{no}を始めます")
    time.sleep(1)
    print(f"<<< 仕事{no}が終わりました")

# 仕事を並列で実行 --- (*2)
jobs = []
for i in range(5):
    # スレッドを作成 --- (*3)
    job = Thread(target=do_work, args=(i,))
    # スレッドを開始
    job.start()
    jobs.append(job)
    time.sleep(0.5)
# 仕事が終わるまで待つ --- (*4)
for job in jobs:
    job.join() # 仕事の終了を待つ
print("--- 全ての仕事が終わりました")
