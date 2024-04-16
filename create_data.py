
import time
import json
from password_key import encrypt



def create_data(result,key):
    res = {
        "answerJson": {
            "answers": {
                
            },
            "consumeTime": 8
        },
        "phoneNumber": "",
        "editVersion": 2,
        "token": result["token"],
        "_t": int(time.time()*1000)
    }
    for item in result.keys():
        if item == "token":
            continue
        if len(item) == 6 and result[item]["type"] == "select":
           
            aaa = []
            jso = result[item]["selectInfo"]
            print(result[item]["title"])
            print("该字段有如下选择:\n" + str(jso))
            number = int(input("请选择第几个")) -1
            dic = result[item]["selectInfo"][number]
            aaa.append(dic)
            
            result[item]["selectValue"] = aaa
           
            del result[item]["selectInfo"]
        elif len(item) == 6:
            
            answer = input(result[item]["title"])
        
            result[item]["strValue"] = answer

        
        
        res["answerJson"]["answers"][item] = result[item]
        del res["answerJson"]["answers"][item]["title"]

    

    ########################################################
    res = json.dumps(res)
    res = encrypt(res,key["aes_key"])
    return res


if __name__ == "__main__":
    print(create_data())