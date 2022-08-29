# XBot2
为go-cqhttp设计的简易PythonSDK

# 配置
+ Python库： requests websockets json

# 开始使用
下载本库，在main.py中编写功能
    
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


    @descripter.RegisterAppre('\\[CQ:at,qq=(.*)\\] (.*)')
    def testAppre(group_id, user_id, msg):
        if group_id:
            sender.sendGroupMsg(group_id, 'Hello World!!!')
        else:
            sender.sendPrivateMsg(user_id, 'Hello World!!!')
            

+ 使用 @descripter.RegisterApp('test') 装饰的函数会在收到消息为 test 时被调用。（消息完全匹配内容时）
+ 使用 @descripter.RegisterAppl(['testA', 'testB']) 装饰的函数会在收到 testA 或 testB 时被调用。（消息属于列表中任意一个时）
+ 使用 @descripter.RegisterAppre('\\[CQ:at,qq=(.*)\\] test(.*)') 装饰的函数会在任意人被艾特时调用。（消息被正则表达式匹配时）
