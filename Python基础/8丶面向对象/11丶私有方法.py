
class Sender(object):
    #私有方法：方法前有两个__下划线就是私有方法
    def __send_msg(self):
        print("-------正在发送短信——————")
    #公有方法
    def send_msg(self,new_money):
        """只有用户的账户金额大于1000才会发送调用私有方法（发送短信）"""
        if new_money > 1000:
            self.__send_msg()
        else:
            print("余额不足，请充值！")

send_msg = Sender()
send_msg.send_msg(1000000)          #余额大于1000,就会调用私有方法
send_msg.send_msg(10)               #余额不足1000,不会调用，提示请充值

