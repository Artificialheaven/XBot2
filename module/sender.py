from module import globals
import requests


def sendGroupMsg(group_id, msg):
    """
    发送群聊消息 采用Post
    :param group_id: 欲发送到的群聊
    :param msg: 欲发送的消息
    :return: gocqhttp返回的数据
    """
    url = f'http://{globals.getValue("websocket_url")}:{globals.getValue("http_port")}/send_group_msg'
    # res = requests.post(url, data=f'group_id={group_id}&message={msg}')
    url = url + f'?group_id={group_id}&message={msg}'
    res = requests.get(url)
    return res


def sendPrivateMsg(group_id, msg):
    """
    发送群聊消息 采用Post
    :param user_id: 欲发送到的群聊
    :param msg: 欲发送的消息
    :return: gocqhttp返回的数据
    """
    url = f'http://{globals.getValue("websocket_url")}:{globals.getValue("http_port")}/send_private_msg'
    # res = requests.post(url, data=f'group_id={group_id}&message={msg}')
    url = url + f'?user_id={group_id}&message={msg}'
    res = requests.get(url)
    return res