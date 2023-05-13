
import pyautogui
import time
import os
import subprocess

# 相対パス表記
current_dir = os.path.dirname(os.path.abspath(__file__))
# MIKALISTディレクトリのパスを作成
mikalist_dir = os.path.join(current_dir, "MIKALIST")
# MIKATYPE.EXEファイルのパスを作成
exe_path = os.path.join(mikalist_dir, "MIKATYPE.EXE")

# EXEファイルを起動
subprocess.Popen(exe_path)
time.sleep(2)

pyautogui.write("a")
time.sleep(2)

pyautogui.write("2")
time.sleep(2)

pyautogui.write("8")


t_end = time.time() + 15 #←速く終わってしまうのならこの数字を変更して秒数を変える
while time.time() < t_end:
    pyautogui.write("abcdefghijklmnopqrstuvwxyz1234567890 abcdefghijklmnopqrstuvwxyz1234567890 abcdefghijklmnopqrstuvwxyz1234567890 ") #←パソコンのスペックに合わせて文字数を変更する。
