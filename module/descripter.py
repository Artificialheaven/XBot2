from module import App


def RegisterApp(funs):
    """
    funs可以传入 str 当收到该消息时，会调用被装饰的函数
    被装饰的函数要求有三个参数，group_id, user_id, msg 当group_id为None时为私聊消息
    :param funs: 欲设定的触发语句
    :return: None
    """
    def Reger(func):
        def wapper(*args, **kwargs):
            func(*args, **kwargs)
        # 在这里把 funs 注册
        App.setValue(funs, func)
        return wapper
    return Reger


def RegisterAppl(funs):
    """
    funs可以传入 list 当收到该消息时，会调用被装饰的函数
    被装饰的函数要求有三个参数，group_id, user_id, msg 当group_id为None时为私聊消息
    :param funs: 欲设定的触发语句
    :return: None
    """
    def Reger(func):
        def wapper(*args, **kwargs):
            func(*args, **kwargs)
        # 在这里把 funs 注册
        App.setValue(f'funclist_{func.__name__}', funs)
        App.setValue(func.__name__, func)
        return wapper
    return Reger


def RegisterAppre(funs):
    """
    funs可以传入 list 当收到该消息时，会调用被装饰的函数
    被装饰的函数要求有三个参数，group_id, user_id, msg 当group_id为None时为私聊消息
    :param funs: 欲设定的触发语句
    :return: None
    """
    def Reger(func):
        def wapper(*args, **kwargs):
            func(*args, **kwargs)
        # 在这里把 funs 注册
        App.setValue(f'funcre_{func.__name__}', funs)
        App.setValue(func.__name__, func)
        return wapper
    return Reger


App.init_()