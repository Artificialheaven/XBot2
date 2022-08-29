def init_():
    global _dict
    _dict = {}


def setValue(key, value):
    _dict[key] = value


def getValue(key):
    try:
        if key in _dict:
            return _dict[key]
        else:
            print(f'\033[0;31;40m error=> 获取全局变量{key}时发生错误，全局变量不存在 \033[0m')
            return None
    except Exception as e:
        print(f'\033[0;31;40m error=> 获取全局变量{key}时发生错误，错误信息{e} \033[0m')
