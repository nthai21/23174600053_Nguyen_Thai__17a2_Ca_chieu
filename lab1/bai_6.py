import math
#Viết chương trình nhập vào tọa độ của 2 vecto a và b.
a1,a2=map(int,input("Nhập nhập vào toạ độ của a:").split())
b1,b2=map(int,input("Mời nhập vào toạ độ của b:").split())
cong_x=a1+b1
cong_y=a2+b2
print("a+b=","(",cong_x,";",cong_y,")")
tru_x=a1-b1
tru_y=a2-b2
print("a-b=","(",tru_x,";",tru_y,")")
#Độ dài veto a,b
do_dai_a=math.sqrt(a1**2+a2**2)
print("Độ dài vecto a là :",do_dai_a)
do_dai_b=math.sqrt(b1**2+b2**2)
print("Độ dài toạ độ b là :",do_dai_b)
#Tính cos góc giữu 2 vecto a,b
tich_a_b=a1*b1+a2*b2
cos=tich_a_b/do_dai_a*do_dai_b
print("Cos của 2 vecto(a,b)=",round(cos,2))
