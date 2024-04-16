import requests
import json
from password_key import decrypt

def form_data(index,key):
    data = {}
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
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "x-encrypt-alg": "aes-128-ofb",
        
    }

    url = "https://f-api.wps.cn/ksform/api/v3/campaign/" + index
    response = requests.get(url, headers=headers)
   
    res = decrypt(response.text,response.headers['x-encrypt-iv'],key["aes_key"])
    res = json.loads(res)
    for re in res["data"]["questionMap"]:

        data[re] = {}
        data[re]["type"] = res["data"]["questionMap"][re]["type"]
        data[re]["title"] = res["data"]["questionMap"][re]["title"]
        if data[re]["type"] == "select":
            data[re]["selectInfo"] = res["data"]["questionMap"][re]["selectInfo"]["selects"]
    data["token"] = res["data"]["token"]
    return data

  