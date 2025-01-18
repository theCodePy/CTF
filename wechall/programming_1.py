import requests
import time

cookie = {'WC': "32742758-70839-f6B02k5S05qnWCzQ"}

start = time.time()
r = requests.get("https://www.wechall.net/challenge/training/programming1/index.php?action=request", cookies=cookie)
# print(r.text)
r2 = requests.get(f"https://www.wechall.net/challenge/training/programming1/index.php?answer={r.text}", cookies=cookie)
print(r2.headers)
print(f"submitted done in {time.time()-start}sec..")
