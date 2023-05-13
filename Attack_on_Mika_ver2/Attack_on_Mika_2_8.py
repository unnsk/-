# 画像と一致する座標を全て格納する（aとbの違いは画像の縦座標の誤差に合わせるため）
class searchCher:
    tc =[]
    def a(i,ipng):
        for pos in pyautogui.locateAllOnScreen(ipng,confidence=0.95):
            img_x,img_y = pyautogui.center(pos)
            searchCher.tc.append({"dccher":i, "dcx":img_x, "dcy":img_y})

    def b(i,ipng):
        for pos in pyautogui.locateAllOnScreen(ipng,confidence=0.95):
            img_x,img_y = pyautogui.center(pos)
            searchCher.tc.append({"dccher":i, "dcx":img_x, "dcy":img_y +1})



import pyautogui
import time
from operator import itemgetter
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

# 項目を選んで少し待つ
pyautogui.write("a")
time.sleep(1)

pyautogui.write("2")
time.sleep(1)

pyautogui.write("8")
time.sleep(1)

# 文字それぞれでsearchCherをする
searchCher.a("0","0.png")
searchCher.a("1","1.png")
searchCher.a("2","2.png")
searchCher.a("3","3.png")
searchCher.a("4","4.png")
searchCher.a("5","5.png")
searchCher.a("6","6.png")
searchCher.a("7","7.png")
searchCher.a("8","8.png")
searchCher.a("9","9.png")

searchCher.a("q","q.png")
searchCher.a("w","w.png")
searchCher.a("e","e.png")
searchCher.a("r","r.png")
searchCher.a("t","t.png")
searchCher.a("y","y.png")
searchCher.a("u","u.png")
searchCher.a("i","i.png")
searchCher.a("o","o.png")
searchCher.a("p","p.png")

searchCher.b("a","a.png")
searchCher.b("s","s.png")
searchCher.b("d","d.png")
searchCher.b("f","f.png")
searchCher.b("g","g.png")
searchCher.b("h","h.png")
searchCher.b("j","j.png")
searchCher.b("k","k.png")
searchCher.b("l","l.png")

searchCher.a("z","z.png")
searchCher.a("x","x.png")
searchCher.a("c","c.png")
searchCher.a("v","v.png")
searchCher.a("b","b.png")
searchCher.a("n","n.png")
searchCher.a("m","m.png")

# 格納した文字と座標を縦の座標で昇順に並び替えて、同じ縦座標ごとに横座標を昇順に並び替える
dctc = sorted(searchCher.tc,key=itemgetter("dcy","dcx"))
xx = " "   #文字だけを入れるリストを初期化

# xxにdctcの文字を格納する（５文字ごとにスペースを入れる）
for i in range(len(dctc)):
    if i == 0:
        xx = str((dctc[i]["dccher"]))
    else:
        xx += str((dctc[i]["dccher"]))
    
    if (i + 1) % 5 == 0:
        xx += " "
print(xx) #デバッグ用
pyautogui.write(xx) #美佳タイプに文字を入力する