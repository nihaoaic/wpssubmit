import requests




def test(index,_cookie,result):

    headers = {
        "authority": "f-api.wps.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "channel": "pc_browser",
        "client-type": "pc",
        "content-type": "application/json; charset=UTF-8",
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
        "x-encrypt-iv": result["iv"]
    }
    cookies = {
        "wps_sid": _cookie
    }
    url = "https://f-api.wps.cn/ksform/api/v3/campaign/" + index
    data = result["data"]
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    
    return response


    
          
    