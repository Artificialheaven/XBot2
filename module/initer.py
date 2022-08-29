import configparser
import os
import sys

from module import globals
from module import ws


def init():
    config = configparser.ConfigParser()
    if os.path.isfile('../config.ini'):
        #   文件存在。
        config.read('./config.ini')
        ip = config['Bot']['ip']
        hp = config['Bot']['hp']
        wp = config['Bot']['wp']
    else:
        #   文件不存在，创建并提示要求修改该文件。
        #   file = open('./config.ini','w')
        #   file.close()
        config['Bot'] = {
            'ip': '127.0.0.1',
            'hp': '5700',
            'wp': '8888'
        }
        with open('../config.ini', 'w') as configfile:
            config.write(configfile)
        print('未检测到配置文件，已生成于 ./config.ini 请修改后重启本程序。')
        sys.exit()
    globals.setValue('websocket_url', ip)
    globals.setValue('websocket_port', wp)
    globals.setValue('http_port', hp)
    # 输出插件信息
    print(f'欢迎使用 {globals.getValue("Plugins_name")} !')
    print(f'{globals.getValue("Plugins_info")}')
    url = f'ws://{globals.getValue("websocket_url")}:{globals.getValue("websocket_port")}'
    print(f'即将连接Websocket服务器 {url}')
    print('高性能しぶそうしん機 !!')
    ws.runBot()
