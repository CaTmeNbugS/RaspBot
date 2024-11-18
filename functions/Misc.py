import json

def getUserInfo(msg):

    userInfo = {
        'id':  msg.from_user.id,
        'username':  msg.from_user.username,
    }

    return json.dumps(userInfo)
