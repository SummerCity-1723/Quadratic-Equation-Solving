from rich import traceback
traceback.install(show_locals=True)

#函数定义
def gcd(x,y=0): #最大公因数
    a,b=abs(x),abs(y)
    if a<b:a,b=b,a
    if b==0: return a
    else: return gcd(b,a%b)

def s(x): #根号整数根号被开方数分离 -> sqrt(x)=a*sqrt(b)
    a = int(x**0.5)  #从x的0.5次方（即sqrt(x)）的整数部分开始
    b = 1  #如果a已经是最优的，则b为1
    # 尝试减小a，同时找到b，使得(b**0.5)是整数
    while True:
        if a==0:
            break  # 如果a已经为0，则无法再减小
        sqrt_b=x/(a**2)  # 尝试找到b，使得sqrt_b是整数
        if sqrt_b%1==0:  # 检查sqrt_b是否为整数
            b=int(sqrt_b)  # 直接使用整数作为b，因为sqrt_b已经是整数
            break
        a-=1
    return a,int(b)

def sqrtgcd(x,y=0,needsq=True): #delta专用求最大公因数
    a=abs(x)
    b=abs(y**2) if needsq else abs(y)
    if a<b:a,b=b,a
    if b==0: return int(a**0.5) if (a**0.5)%1==0 else s(a)[0]
    else: return sqrtgcd(b,a%b,False)

def delta(a=1,b=0,c=0): #计算方程判别式
    return (b**2)-(4*a*c)


#主函数
def qes(a=1,b=0,c=0):
    d=delta(a,b,c)
    if d<0: #无实根
        print("无实根")
        return 0

    if d==0: #相同根
        fz,fm=int(-b/gcd(-b,2*a)),int(2*a/gcd(-b,2*a)) #计算分子,分母
        print(fm==1 and f"x1=x2={fz}" or f"x1=x2={fz}/{fm}")
        return 1

    else: #不同根
        intz,intm=int(-b/gcd(-b,2*a)),int(2*a/gcd(-b,2*a)) #-b/2a部分分子分母
        sqrtz,sqrtm=int(d/(sqrtgcd(d,2*a)**2)),int(2*a/sqrtgcd(d,2*a)) #sqrt(b^2-4ac)部分分子分母

        if (sqrtz**0.5)%1==0: #sqrt(b^2-4ac)是整数
            fz,fm=int(sqrtz**0.5),sqrtm
            #接下来两行，计算x1，x2的分子分母，并将其简化
            x1fz,x1fm,x2fz,x2fm=intz*fm+intm*fz,intm*fm,intz*fm-intm*fz,intm*fm
            x1fz,x1fm,x2fz,x2fm=int(x1fz/gcd(x1fz,x1fm)),int(x1fm/gcd(x1fz,x1fm)),int(x2fz/gcd(x2fz,x2fm)),int(x2fm/gcd(x2fz,x2fm))

            print(x1fm==1 and f"x1={x1fz}" or f"x1={x1fz}/{x1fm}",end="  ")
            print(x2fm==1 and f"x2={x2fz}" or f"x2={x2fz}/{x2fm}")
        else: #sqrt(b^2-4ac)不是整数
            sqrtcj,sqrtz=s(sqrtz) #sqrt(sqrtz)=sqrtcj*sqrt(sqrtz)

            print(intm==1 and f"x1={intz}+" or f"x1={intz}/{intm}+",end="")
            if sqrtcj!=1:print(f"{sqrtcj}*",end="")
            print(sqrtm==1 and f"sqrt({sqrtz})" or f"sqrt({sqrtz})/{sqrtm}",end="  ")

            print(intm==1 and f"x2={intz}-" or f"x2={intz}/{intm}-",end="")
            if sqrtcj != 1: print(f"{sqrtcj}*", end="")
            print(sqrtm==1 and f"sqrt({sqrtz})" or f"sqrt({sqrtz})/{sqrtm}")
        return 2

def qes_enter(a=1,b=0,c=0):
    # 方程输出
    print(a==1 and "x²" or (a==-1 and "-x²" or f"{a}x²"), end="")
    if b!=0: print(b<0 and (b!=-1 and f"{b}x" or "-x") or (b!=1 and f"+{b}x" or "+x"),end="")
    if c!=0: print(c<0 and f"{c}" or f"+{c}",end="")
    print("=0",end="     ")

    g=gcd(gcd(a,b),gcd(a,c))
    if a==0: print("不是一元二次方程(二次项系数为0)") #排除错误方程
    elif a<0:
        qes(int(-a/g),int(-b/g),int(-c/g))
    else:
        qes(int(a/g),int(b/g),int(c/g))

l=[]
q="1"
print("请输入项系数a,b,c(ax²+bx+c=0)[空格间隔]:")
while q!="":
    q=input()
    if q!="":
        a=[int(i) for i in q.split(" ")]
        l.append(a)
print("========================================================================")
idx=1
for i in l:
    print(str(idx)+".",end="")
    qes_enter(i[0],len(i)>=2 and i[1] or 0,len(i)>=3 and i[2] or 0)
    idx+=1