# -*-encoding=utf8-*-
import os
import tkinter
from tkinter.filedialog import askopenfilename
import time

root = tkinter.Tk()
root.withdraw()
default_dir = r"文件路径"
file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
try:
    os.system("del log.txt")
    os.system("del rengong_zimu.txt")
    os.system("del machine_zimu.txt")
except:
    pass
with open(file_path, 'r', encoding='utf8') as f:
    res = f.readlines()
    urls_num = len(res)
    print("总共有音频数: ", urls_num)
    for index, url in enumerate(res):
        print("当前正在处理第{}条音频，已完成{}%".format(index, round(index / urls_num * 100, 5)))
        if len(url) < 10:
            continue
        command = "youtube-dl --list-subs " + url.strip() + " >> log.txt"
        print(command)
        os.system(command)
        time.sleep(0.1)

with open("log.txt", 'r', encoding='utf8') as f:
    res = f.readlines()
rengong_zimu = []
machine_zimu = []

for i in res:
    if i.find("Available subtitles for") > -1:  # 发现字幕
        video_id = i.split('for')[1].split(":")[0].strip()
        print(video_id)
        rengong_zimu.append(video_id)
    if i.find("Available automatic captions for") > -1:  # 发现字幕
        video_id = i.split('for')[1].split(":")[0].strip()
        machine_zimu.append(video_id)

rengong_zimu = ["https://www.youtube.com/watch?v=" + i for i in rengong_zimu]
machine_zimu = ["https://www.youtube.com/watch?v=" + i for i in machine_zimu]

with open("rengong_zimu.txt", 'a', encoding='utf8') as f1:
    f1.write("\n".join(rengong_zimu))
    f1.write("\n")
with open("machine_zimu.txt", 'a', encoding='utf8') as f2:
    f2.write("\n".join(machine_zimu))
    f2.write("\n")