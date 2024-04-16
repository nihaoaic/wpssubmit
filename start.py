import re
from encrypt_key import encrypt_key
from register import give_cookie
from test import test
from create_data import create_data
from form_data import form_data
import json
import threading
from password_key import decrypt



def start(_cookie, key, extracted_content, result_):
    while True:
        result = test(extracted_content, _cookie, result_)
        header = result.headers

        text = result.text

        res = json.loads(decrypt(text, header["x-encrypt-iv"], key["aes_key"]))
        
        if res["code"] == 13015 or res["code"] == 11001:
            print(res["result"])
            break

        if res["code"] == 0:
            print("已成功")
            break
        

if __name__ == '__main__':
    
    print("*"*60)
    print("欢迎使用表单脚本(多核抢注脚本) by:nihao_")
    print("*"*60)
    _cookie = give_cookie()
    key = encrypt_key()
    url = input("请输入文档地址") 
    match = re.search(r'/g/([a-zA-Z0-9]+)', url)
    if match:
        extracted_content = match.group(1)
        news = form_data(extracted_content,key)
    else:
        print("输入的格式错误")
        exit()

    result = create_data(news,key)

    number = input("请输入线程数(不输入默认2,建议不要超过5个线程数,否则会有崩表单服务器风险):")
    if not number:
        number = 2
    else:
        number = int(number)


    # 开启多线程
    threads = []
    for i in range(number):
        threads.append(threading.Thread(target=start,args=[_cookie, key, extracted_content, result]))

    for i in threads:
        i.start()

    for i in threads:
        i.join()