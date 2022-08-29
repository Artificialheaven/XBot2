import asyncio
import time
import websockets
import json
import re

import App
import globals


async def runWebsocket():
    url = f'ws://{globals.getValue("websocket_url")}:{globals.getValue("websocket_port")}'
    while True:
        try:
            async with websockets.connect(url) as websocket:
                globals.setValue('websocket', websocket)    # 添加全局websocket
                while True:
                    res = await websocket.recv()
                    js = json.loads(res)
                    jsonParse(js)
        except Exception as e:
            print(f'\033[0;31;40m error=> 连接websocket服务器{url}时发生错误，错误信息{e} \033[0m')
            print('将在五秒后重新连接，按 Ctrl+C 关闭。')
            time.sleep(5)


def jsonParse(js: dict):
    if js['post_type'] == 'message':
        try:
            post_type = js['post_type']
            message_type = js['message_type']
            if message_type == 'group':
                group_id = js['group_id']
                user_id = js['sender']['user_id']
                msg = js['raw_message']
                print(f'{post_type}|{message_type}[{group_id}]({user_id}){msg}')    # 群聊消息
                # if msg in App.getDict():
                #     App.getValue(msg)(group_id, user_id)
                for i in App.getDict():
                    if i.startswith('funclist_'):
                        if msg in App.getValue(i):
                            funcname = i.replace('funclist_', '')
                            App.getValue(funcname)(group_id, user_id, msg)
                    elif i.startswith('funcre_'):
                        if re.search(App.getValue(i), msg):
                            App.getValue(i.replace('funcre_', ''))(group_id, user_id, msg)
                    else:
                        if msg == i:
                            App.getValue(i)(group_id, user_id)
            elif message_type == 'private':
                user_id = js['sender']['user_id']
                msg = js['raw_message']
                print(f'{post_type}|{message_type}({user_id}){msg}')    # 私聊消息
                for i in App.getDict():
                    if i.startswith('funclist_'):
                        if msg in App.getValue(i):
                            funcname = i.replace('funclist_', '')
                            App.getValue(funcname)(None, user_id, msg)
                    elif i.startswith('funcre_'):
                        if re.search(App.getValue(i), msg):
                            App.getValue(i.replace('funcre_', ''))(None, user_id, msg)
                    else:
                        if msg == i:
                            App.getValue(i)(None, user_id)
        except Exception as e:
            print(f'\033[0;31;40m error=> 解析json数据{js}时发生错误，错误信息{e} \033[0m')


def runBot():
    asyncio.run(runWebsocket())