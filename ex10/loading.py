from tqdm import tqdm
import time

bar_format = "ETA: {remaining_s:.2f}s [{percentage:.0f}%][{bar}] {n}/{total} | elapsed time {elapsed_s:.2f}s"
def ft_progress(listy):
        for i in tqdm(listy, bar_format=bar_format):
            yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += elem % 5
    time.sleep(0.01)

print()
print(ret)



    
