#Nhập vào toạ độ 4 đỉnh của tứ giác 
m1,m2=map(int,input("Mời nhập vào toạ độ của M:").split())
n1,n2=map(int,input("Mời nhập vào toạ độ của N:").split())
p1,p2=map(int,input("Mời nhập vào toạ độ của P:").split())
q1,q2=map(int,input("Mời nhập vào toạ độ của Q:").split())
print("M(",m1,",",m2,")")
print("N(",n1,",",n2,")")
print("P(",p1,",",p2,")")
print("Q(",q1,",",q2,")")
#Toạ độ MN
td_mn=(m1+n1)/2
td1_mn=(m2+n2)/2
#Toạ độ pq
td_pq=(p1+q1)/2
td1_pq=(p2+q2)/2
#Toạ đọ MP
td_mp=(m1+p1)/2
td1_mp=(m2+p2)/2
#Toạ độ NP
td_np=(n1+p1)/2
td1_np=(n2+p2)/2
#Toạ độ MQ
td_mq=(m1+q1)/2
td1_mq=(m2+q2)/2
#Toạ đọ NQ
td_nq=(n1+q1)/2
td1_nq=(n2+q2)/2
print("MN(",td_mn,",",td1_mn,")")
print("PQ(",td_pq,",",td1_pq,")")
print("MP(",td_mp,",",td1_mp,")")
print("NP(",td_np,",",td1_np,")")
print("MQ(",td_mq,",",td1_mq,")")
print("NQ(",td_nq,",",td1_nq,")")












