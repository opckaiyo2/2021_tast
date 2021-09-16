#coding: utf-8
import sys
import time
import configparser

# 自作関数の場所をsystempathに追加
sys.path.append("/home/pi/2021/main/my_mod")
# motor制御
from my_motor import Motor
from my_operatfunction import OF

def Teaching(sen_data):

    of = OF()
    motor = Motor()

    # データがすべて揃うまでループ endtimeはデータの一番後列
    while(not('endtime' in sen_data)):
        pass

    # 初期向きの暗記
    ini_x = sen_data["x"]

    # 初期向きの反対(Uターンなどで使う)
    ini_opx = 0

    if ini_x < 180:
        ini_opx = ini_x+180
    elif ini_x > 180:
        ini_opx = ini_x-180
    elif ini_x == 180:
        ini_opx = 180

    print("ini_x : "+str(ini_x))
    print("ini_opx : "+str(ini_opx))

    # 設定ファイル読み込み-------------------------------------------

    INI_FILE = "/home/pi/2021/main/config/config.ini"
    inifile = configparser.ConfigParser()
    inifile.read(INI_FILE,encoding="utf-8")

    # どのデータを読み込むか
    rotate = eval(inifile.get("teaching","rotate"))

    # 設定ファイル読み込み-------------------------------------------


    # log再生------------------------------------------------------


    # 潜水位置まで-------------------------------------------------
    print("潜水位置まで")
    of.pid_goback_rotate_stop(100,ini_x,sen_data)
    # 潜水位置まで-------------------------------------------------

    # 潜水位置まで潜水---------------------------------------------
    print("潜水")
    of.diving(sen_data)
    # 潜水位置まで潜水---------------------------------------------

    # 浮上位置まで------------------------------------------------
    print("浮上位置")
    of.pid_goback_rotate_stop(0,ini_x,sen_data)
    # 浮上位置まで------------------------------------------------

    # 浮上-------------------------------------------------------
    print("浮上")
    of.ascend(sen_data)
    # 浮上-------------------------------------------------------

    # Uターン----------------------------------------------------
    print("Uターン")
    of.rotate_yaw(ini_opx,sen_data)
    # Uターン----------------------------------------------------

    # 潜水位置まで-------------------------------------------------
    print("潜水位置")
    of.pid_goback_rotate_stop(0,ini_opx,sen_data)
    # 潜水位置まで-------------------------------------------------

    # 潜水位置まで潜水---------------------------------------------
    print("潜水")
    of.diving(sen_data)
    # 潜水位置まで潜水---------------------------------------------

    # 浮上位置まで------------------------------------------------
    print("浮上位置")
    of.pid_goback_rotate_stop(0,ini_opx,sen_data)
    # 浮上位置まで------------------------------------------------

    # 浮上-------------------------------------------------------
    print("浮上")
    of.ascend(sen_data)
    # 浮上-------------------------------------------------------

    # スタート位置まで--------------------------------------------
    print("スタート位置")
    of.pid_goback_rotate_stop(0,ini_opx,sen_data)
    # スタート位置まで--------------------------------------------

    # すべてのモータstop
    motor.stop()

    # log再生------------------------------------------------------

if __name__ == "__main__":
    Teaching()
