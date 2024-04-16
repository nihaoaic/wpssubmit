import requests
import time
import re
import subprocess



def give_png():
    return subprocess.Popen(["cmd.exe", "/c", "start", "./p1.png"])

   

def give_cookie():

    time_ = str(int(time.time() * 1000))

    headers = {
        "Accept": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": f"https://account.wps.cn/?qrcode=kdocs&logo=kdocs&accessid=AK20210823OPGONG&from=v1-web-kdocs-login&cb=https://account.wps.cn/api/v3/session/correlate/redirect?t={time_}&appid=375024576&cb=https://www.kdocs.cn/singleSign4CST?t={time_}&cb=https%3A%2F%2Fwww.kdocs.cn%2F%3Ffrom%3Ddocs",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://account.wps.cn/api/v3/miniprogram/code/img"
    params = {
        "action": "verify",
        "data": "{\"qrShowAgreement\":true,\"keeponline\":1,\"from\":\"v1-web-kdocs-login\"}",
        "_": str(int(time.time()*1000))
    }
    response = requests.get(url, headers=headers,params=params)

    json_res = response.json()

    new_url = json_res["url"]
    change = json_res["channel_id"]
    response = requests.get(new_url, headers=headers,params=params).content

    with open("./p1.png","wb")as f:
        f.write(response)
    
    picture_pid = give_png()
    while True:
        headers = {
            "authority": "qr.wps.cn",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://account.wps.cn/",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }

        url = "https://qr.wps.cn/api/v3/channel/wait"
        params = {
            "_jsonp": "miniprogramcodeJsonpCallback",
            "channel_id": change,
            "_": str(int(time.time()*1000)),
            "callback": "miniprogramcodeJsonpCallback"
        }
        response = requests.get(url, headers=headers, params=params)

        res = re.findall(r'state":"(.*?)"',response.text)[0]
        if res == 'notified':
    
            print("请点击确认进行登录")

            break

        print("请扫描二维码登录")


    url = "https://qr.wps.cn/api/v3/channel/wait"
    params = {
        "_jsonp": "miniprogramcodeJsonpCallback",
        "channel_id": change,
        "_": str(int(time.time()*1000)),
        "callback": "miniprogramcodeJsonpCallback"
    }
    response = requests.get(url, headers=headers, params=params).text


    ssid = response.split("}")[0].split("\\")[-2].split('"')[1]
    
    time_2 = str(int(time.time() * 1000))

    headers = {
        "authority": "account.wps.cn",
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": f"https://account.wps.cn/v1/chooseaccount?qrcode=kdocs&logo=kdocs&accessid=AK20210823OPGONG&from=v1-web-kdocs-login&cb=https%3A%2F%2Faccount.wps.cn%2Fapi%2Fv3%2Fsession%2Fcorrelate%2Fredirect%3Ft%3D{time_2}%26appid%3D375024576%26cb%3Dhttps%253A%252F%252Fwww.kdocs.cn%252FsingleSign4CST%253Ft%253D{time_2}%2526cb%253Dhttps%25253A%25252F%25252Fwww.kdocs.cn%25252F%25253Ffrom%25253Ddocs&logintype=weblogin_v2&verifyresult=ok&utype=wechat&ssid={ssid}",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }

    url = "https://account.wps.cn/api/v3/login/users"
    params = {
        "ssid": ssid,
        "filter_rule": "normal",
        "_": str(int(time.time() * 1000))
    }
    response = requests.get(url, headers=headers, params=params)

    userid = response.json()["users"][0]["userid"]




    headers = {
        "authority": "account.wps.cn",
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://account.wps.cn",
        "pragma": "no-cache",
        "referer": f"https://account.wps.cn/v1/chooseaccount?qrcode=kdocs&logo=kdocs&accessid=AK20210823OPGONG&from=v1-web-kdocs-login&cb=https%3A%2F%2Faccount.wps.cn%2Fapi%2Fv3%2Fsession%2Fcorrelate%2Fredirect%3Ft%3D{time_2}%26appid%3D375024576%26cb%3Dhttps%253A%252F%252Fwww.kdocs.cn%252FsingleSign4CST%253Ft%253D{time_2}%2526cb%253Dhttps%25253A%25252F%25252Fwww.kdocs.cn%25252F%25253Ffrom%25253Ddocs&logintype=weblogin_v2&verifyresult=ok&utype=wechat&ssid={ssid}",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "x-csrftoken": "hn4jfrPpJEafhX78reacbDayXaBFeM6k",
        "x-requested-with": "XMLHttpRequest"
    }

    url = "https://account.wps.cn/api/v3/login/web_login"
    data = {
        "qrcode": "kdocs",
        "logo": "kdocs",
        "accessid": "AK20210823OPGONG",
        "from": "v1-web-kdocs-login",
        "cb": f"https://account.wps.cn/api/v3/session/correlate/redirect?t={time_2}&appid=375024576&cb=https%3A%2F%2Fwww.kdocs.cn%2FsingleSign4CST%3Ft%3D{time_2}%26cb%3Dhttps%253A%252F%252Fwww.kdocs.cn%252F%253Ffrom%253Ddocs",
        "logintype": "weblogin_v2",
        "verifyresult": "ok",
        "utype": "wechat",
        "ssid": ssid,
        "page": "weblogin_v2",
        "userids": userid
    }

    response = requests.post(url, headers=headers,data=data)
    if(response.status_code == 200):
        time.sleep(1)  
        picture_pid.terminate()
        print("登录成功")
    return response.cookies["wps_sid"]


if __name__ == "__main__":
    print(give_cookie())
