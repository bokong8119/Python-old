from ctypes.wintypes import PINT
import turtle


a=0
b=0
a=input('press the enter')
while True:
#Ture 应当大写，不然报错
    if b==1000:
#平常的=在python为==，=为写入
        break
    else:
        b=b+1
        continue
#continue为继续循环，break为打破循环
print ("已确认打醒")
#while下面有空格（至少空四格的），上面的则不在循环范围内 如果要跳出循环 按Ctrl+c（不是复制）