import re

passwords = '我的密码是，微博：abcdefg，银行卡：345678，微信：dfkksdfjsdfad，'

print(passwords)

pass_list = re.findall('：(.*?)，', passwords)
print('找到密码：{}'.format(pass_list)) 

