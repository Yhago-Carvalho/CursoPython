from time import sleep
import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(0.1)
print(emoji.emojize(use_aliases=True))
