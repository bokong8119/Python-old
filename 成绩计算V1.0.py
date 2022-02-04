#本次采用python3.0编写，请确保已在python3.0环境下运行，否则开头就报错（你自己干的，有本事你采用python3.0编写【滑稽】【滑稽】）
number=eval(input("人数!!!"))
sum=0.0
#初始化，采用0.0而不用0是因为如果用0，结果会四舍五入
for i in range (number):
#上面for i in range(变量): 为固定搭配
    X=eval(input("输入分数"))
    sum=sum+X
l1=sum/number 
#本次/为除号
print("平均数为：",l1)