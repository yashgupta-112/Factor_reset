from tqdm import tqdm
from time import sleep
pbar = tqdm(range(100))
count = 5

for i in range(count):
    print(i)
    sleep(0.2)
    pbar.update((i/count)*100)