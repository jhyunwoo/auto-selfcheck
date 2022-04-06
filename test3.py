import os


import json


import requests


def sendToMeMessage(text):

    header = {"Authorization": 'Bearer ' + token}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # 나에게 보내기 주소

    post = {


        "object_type": "text",


        "text": text,


        "link": {


            "web_url": "https://developers.kakao.com",


            "mobile_web_url": "https://developers.kakao.com"


        },


        "button_title": "바로 확인"


    }

    data = {"template_object": json.dumps(post)}

    return requests.post(url, headers=header, data=data)


text = "나에게 보내는 카톡("+os.path.basename(__file__).replace(".py", ")")


token = "72bce62695fb756a96e9e96d73123604"


print(sendToMeMessage(text).text)
