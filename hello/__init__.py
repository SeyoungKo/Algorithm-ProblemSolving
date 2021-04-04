# 수행시간 측정하는 방법
# ctrl + shift + r
import time

def timer():
    start_time = time.time()
    print("코드 실행 중....")
    end_time = time.time()

    print("run time : ", (end_time - start_time))

if __name__ == '__main__':
    timer()
