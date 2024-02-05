import sys
import time
import multiprocessing

def cyc(c):
    while True:
        time.sleep(0.5)
        print('cyc', c)

def main():
    # 登録
    p = multiprocessing.Process(target=cyc,args=('*'))
    # 開始
    p.start()
    for c in range(5):
        time.sleep(1.0)
        print('main', c)
    # 終了
    p.terminate()
    for c in range(5,10):
        time.sleep(1.0)
        print('main', c)

if __name__ == "__main__":
    main()
