import requests

uri = 'https://webfs.yun.kugou.com/202010282312/d371f7e55235f2ba03b7fb9865021135/G087/M09/16/18/94YBAFjCjLOAGXk9ADeFOk4MK5I894.mp3'
ll = requests.get(uri)

with open("E:/video/Trap.mp3", "wb") as f:
    f.write(ll.content)