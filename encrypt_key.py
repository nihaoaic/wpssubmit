import requests
import json

def encrypt_key():
    headers = {
        "authority": "f-api.wps.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-type": "application/json; charset=utf-8",
        "origin": "https://f.wps.cn",
        "pragma": "no-cache",
        "referer": "https://f.wps.cn/",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    url = "https://f-api.wps.cn/ksform/api/v3/config"
    response = requests.get(url, headers=headers).text
    response = json.loads(response)
    return response["data"]["encrypt"]
  


if __name__ == "__main__":
    print(encrypt_key())



