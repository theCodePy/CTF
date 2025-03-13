import requests
from tqdm import tqdm

for i in range(-10,20):
    print(i, end=' ')
    r = requests.get(f"http://momo.hackmyvm.eu/n1lsfr4hm/index.php?user={i}")
    res = r.text
    if "<br>" in res:
        t = res.split("<br>")[-1]
        print(t)
print()
