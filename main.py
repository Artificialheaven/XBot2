from module import sender, initer, globals, descripter


def AppInfo():
    # 编写插件信息
    globals.init_()
    globals.setValue('Plugins_name', 'XBot2')
    globals.setValue('Plugins_info', '我是XBot2示例插件')
    initer.init()


@descripter.RegisterAppl(['testA', 'testB'])
def testApp(group_id, user_id, msg):
    if group_id:
        sender.sendGroupMsg(group_id, 'Hello World!')
    else:
        sender.sendPrivateMsg(user_id, 'Hello World!')


@descripter.RegisterApp('test')
def testApp2(group_id, user_id):
    if group_id:
        sender.sendGroupMsg(group_id, 'Hello World!!')
    else:
        sender.sendPrivateMsg(user_id, 'Hello World!!')


@descripter.RegisterAppre('\\[CQ:at,qq=3399088205\\] test(.*)')
def testAppre(group_id, user_id, msg):
    if group_id:
        sender.sendGroupMsg(group_id, 'Hello World!!!')
    else:
        sender.sendPrivateMsg(user_id, 'Hello World!!!')


AppInfo()
