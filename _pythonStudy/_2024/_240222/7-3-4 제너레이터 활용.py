# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))

"""
필요한 경우에만 호출하여 사용. (lazy evaluation)
"""