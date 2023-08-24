# """def demo():
#     def function1(z):
#         count=0
#         for p in range(1,z+1):
#             if z%p==0:
#                 count=count+1
#         if count==2:
#                 return z
#     def function2(l):
#         if l!=None:
#             return l
#     def function3(y):
#         _y=str(y)
#         if len(_y)!=1:
#             if _y[-1]=="3":
#                 return _y

#     def function4(x):
#         _y=str(x)
#         if len(_y)!=1:
#             if _y[0]=="2":
#                 return _y




#     a=int(input("enter range of numbers"))
#     x=[i for i in range(1,a)]
#     l=map(function1,x)

#     l1=list(l)
#     #print(l1)





#     l2=filter(function2,l1)
#     _l2=list(l2)

#     l3=list(map(float,_l2))
#     print(_l2)
#     print()
#     print(l3)
#     print()



#     l4=list(filter(function3,_l2))

#     print(l4)
#     print()
#     print("ends with 3 and starts with 2:")
#     print("-"*30)

#     l5=list(filter(function4,l4))
#     print(l5)

#     l6=list(filter(lambda c:c>200 and c<500,l5))
#     print(l6)

# def function1(z):
#         count=0
#         for p in range(1,z+1):
#             if z%p==0:
#                 count=count+1
#         if count==2:
#                 return z"""
# """def function2(k):
#     j=[]
#     for p in range(1,k+1):
#         count=0
#         for l in range(1,p):
#             if p%l==0:
#                 count=count+1
#         if count==2:
#             j.append(p)    """



# # def function1(z):
# #     d=[]
# #     for char in z:
# #         if char == "0":
# #             d.append(char)
# #     return d



# # def function2(l):
    
# #     h=[]
# #     for char in l:
# #         if char.isdigit():
# #              num=int(char)
# #              if num!=0:
# #                 if num%2==0:
# #                         h.append(num)
# #     return h
#     # e,o=[],[]
#     # for i in k:
        
#     #     if i.isdigit():
#     #         j=int(i)
#     #         if j!=0:
#     #             if j%2==0:
#     #                 e.append(j)
#     #             else:
#     #                 o.append(j)
#     # print(e,o)

    



# """n=int(input("enter 9 digits mobile number :"))
# k=str(n)


# m=function1(k)




# n=function2(k)


# print(str(m+n))"""


# # 3........(swapping of 1st and last num in a list)

# # num1=input()
# # a=[i for i in num1 ]
# # print(a)
# # k=a[0]  
# # m=a[-1] 
# # a[0],a[-1]=m,k


# # print(a)

    
# # 3--(using function)........

# # def function(k):
# #     start,*mid,end=k
# #     k=[end,*mid,start]
# #     return k

# # num1=input()
# # a=[i for i in num1 ]
# # n=(function(a))
# # print(list(map(int,n)))





# # 4--(finding length)
# # a=[1,2345,678,909,789]
# # c=0
# # for i in a:
# #     c=c+1
# # # print(len(a))
# # print(c)



# # 5-- program to swap elements  at given positions
# # def swapPositions(list, pos1, pos2):
	
# # 	list[pos1], list[pos2] = list[pos2], list[pos1]
# # 	return list


# # List = [23, 65, 19, 90]
# # pos1, pos2 = int(input()),int(input())

# # print(swapPositions(List, pos1-1, pos2-1))



# # 6--to check whether the string is Symmetrical or Palindrome

# # a=input()
# # b=a[::-1]
# # if a==b:
# #     print("{}   is palindrome".format(a))
# # else:
# #     print("{}   is not  palindrome".format(a))
# # k=int(len(a)/2)
# # b=a[k:]
# # c=a[:k]
# # if b==c:
# #     print("{}   is symmetrical".format(a))
# # else:
# #     print("{}  is not symmetrical".format(a))




# # 7---Reverse words in a given String in Python



# # a=input()
# # b=""
# # for i in range(1,len(a)+1):
# #     b=b+a[-i]
# # if b==a:
# #     print("True")
# # else:
# #     print("False")


# # 8----Ways to remove i’th character from string in Python


# # a=input("enter string: ")
# # b=int(input("enter which position char do you whant to remove : "))
# # k=a.replace(a[b],"")
# # print(k)
    

# # 9------Python program to print even length words in a string

# # a= input("enter strings to find even length of strings: ")
# # b=a.split(" ")
# # for i in b:
# #     if len(i)%2==0:
# #         print(i)


# # 9------Python program to print even length words in a string(using lambda)

# # a= input("enter strings to find even length of strings: ")
# # b=a.split(" ")
# # k=list(filter(lambda x:len(x)%2==0,b))
# # for i in k:
# #     print(i,end=" ")


# #10 ----Avoid Spaces in string length 

# # a=input("enter strings : ")
# # print(len(a))
# # b=a.replace(" ","")
# # print(len(b))

# # 11 ------Uppercase Half String

# # a=input("enter strings : ")
# # k=int(len(a)/2)
# # c=a[k:].upper()

# # d=a[:k]
# # print(d+c)


# #12 -----Python program to capitalize the first and last character of each word in a string
# # a=input("enter strings : ")
# # b=a.split(" ")
# # for i in b:
# #     h=i[0].upper()
# #     f=i[-1].upper()
# #     g=i[1:-1]
# #     print((h+g+f),end=" ")
   

# #13-----python program to print a pattern 
# # a=input("enter strings : ")
# # b=a.split()[0]
# # _b1=b[0].upper()
# # _b2=b[-1].upper()
# # _b3=b[1:-1]
# # print((_b1+_b3+_b2),end=" ")

# # c=a.split()[1]
# # d=len(c)
# # if d%2!=0:
# #     k=int(d/2)

# #     j=c[:k]
# #     l=c[k+1:]
# #     n=c[k].upper()
# #     print((j+n+l),end=" ")
# # else:
# #     l=int(d/2)
# #     k=c[:l][-1].upper()#he#e
# #     g=c[l:][0].upper()#ll#l
# #     print(c[:l-1]+k+g+c[l+1:])#h+E+L+l


# # d=a.split()[2]
# # r=int(len(d)/2)
# # z=d[r:].upper()
# # y=d[:r].lower()
# # print((y+z),end=" ")

# # m=a.split()[3]
# # r=m[::-1]
# # print(r)

# #  14--------– Maximum and Minimum K elements in Tuple
# # p=list(map(int,input("enter values:").split()))

# # print(tuple(p))
# # q=sorted(p)
# # print(q)
# # k=int(input("enter k : "))

# # a=len(q)
# # print(q[:k]+q[-k:])

# # 15-------- sum of elements in a tuple
# # a=tuple(input("enter values").split())
# # b=list(map(int,a))
# # c=0
# # for i in b:
# #     c+=i
# # print(c)



# # 16-------addings elemets in a tuple 
# # def kin():    
# #     m=[]
    
# #     for i in b:
# #         k=(list(i))
# #         m.append(k)
    
# #     t=[]
# #     for l in m:
# #         t=t+l
# #     y=0
# #     for p in t:
# #         y=y+p

# #     return y
# # a=((2,4,5,4000),(1,3,4),(56,8,9),(1000,4,6))
# # b=list(a)
# # print(kin())


# ## -------addings elemets in a tuple 

# # x=tuple(input("enter values: "))
# # l=[i for i in x]
# # p=list(map(int,l))
# # j=sum(p)
# # print(j)

# ## -------addings elemets in a tuple 
# # x=(1,2,3,4,5)
# # y=(1,2,3,4,5)
# # z=(1,2,3,4,0)
# # total=tuple(zip(x,y,z))
# # print(total)
# # t1=tuple(map(sum,total))
# # print(t1)

# # range examples
# # k=('a','b','c','d')

# # for i in range(0,10):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(10,16):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(1000,1006):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(-1,-11,1):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(-1000,-1006,-1):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(10,0,-1):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(-100,-94,1):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(10,101,1):
# #     print(i,end=' ')
# # print("--"*12)
# # for i in range(200,-1,-50):
# #     print(i,end=' ')
# # print("--"*12)


# #-------- del pop remove
# # l1=[11,7,23,4,5,9]
# # l1.remove(11)
# # del l1[:2]
# # l1.pop()
# # print(l1)

# # copy ,deep copy,shallow copy,slice based copy,index,count

# # a=[1,2,4,4,4,5,6,4]
# # print(a,id(a))
# # b=a.copy()
# # print(b,id(b))
# # c=b
# # print(c,id(c))
# # d=b[::2]
# # print(d,id(d))
# # e=a.index(4)
# # print(e)
# # print(a.count(4))

# # a={1,2,3,4,"python"}
# # print(type(a))
# # print(a[0])

# # palindrome without using pre defined functions
# # a=1221
# # k=a
# # result=0
# # while k>0:
# #     t=k%10
# #     result=(result*10)+t
# #     k=k//10

# # if a==result:print("True")
# # else:print("False")


# # fibnocci siries(0,1,1,2,3,5,8...)
# # a=0
# # b=1
# # k=int(input("enter a number in range : "))
# # print(a)
# # print(b)

# # c=0
# # while c<k:
# #     c=a+b
# #     a=b
# #     b=c
# #     if c<k:
# #         print(c)
   
# # --fibnocci series of given k numbers

# # a=0
# # b=1
# # k=int(input("enter a number in range : "))
# # print(a)
# # print(b)

# # i=0
# # while i<(k-2):
# #     c=a+b
# #     a=b
# #     b=c
# #     i=i+1
# #     print(c)


# # fibnocci using for loop
# # a=0
# # b=1
# # k=int(input("enter number : "))
# # print(a,b,end=" ")

# # for i in range (k-2):
# #     c=a+b
# #     a=b
# #     b=c
# #     print(c,end=" ")



# # given number prime  number or not

# # a=(int(input("enter a digit to check :")))
# # count=0
# # for j in range(1,a+1):
# #     if a%j==0:
# #         count=count+1 
# # if(count==2):print("true")
# # else:print("false")
        
    
# # a=(int(input("enter a digit to print prime numbers in that range :")))
# # for b in range(1,a+1):
# #     # if b>1:
# #         for i in range(2,b):
# #             if b%i==0:
# #                 break
# #         else:
# #              print(b)
    



# # example for loop
# # for i in range(10,16):
# #     print(i,end=' ')
# #     for i in range(20,26):
# #         print(i,end=' ')
# #     print()
# # print("--"*12)


# #find factorial of the given number

# # a=int(input("enter num :"))
# # m=1
# # for i in range(1,a+1):
# #     c=((a+1)-i)
# #     m=m*c
# # print(m)

# #find factorial of the given number

# # a=int(input("enter num :"))
# # m=1
# # for n in range(1,a+1):
# #     m=m*n
# # print(m)


# # armstrong number

# # a=int(input("enter : "))
# # j=a
# # res=0
# # # sum=0
# # while j>0:
# #     k=j%10
# #     res=res+k*k*k
# #     # sum=sum+res
# #     # print(res)
# #     j=j//10
# # if res==a:print("True")
# # else:print("False")
# #     print(l)
# # print(res)









# # multiplication table 
# # k=int(input("enter which number multiplication table do u want : "))  #4
# # i=0
# # while i<11:
# #     c=k*i
# #     print("{}*{}={}".format(k,i,c))
# #     i=i+1

# # def fun(a,b):
# #     c=a+b
# #     d=a-b
# #     e=a*b
# #     f=a/b
# #     return c,d,e,f
# # x=(int(input("enter 1 st value : ")))
# # y=(int(input("enter 1 st value : ")))
# # c=(fun(x,y))
# # print(c)










# # a=[1,2,3,4,56]
# # c=a
# # k=int(input("enter your index : "))
# # b=12
# # j=0
# # for i in (c):
# #     j=j+1

# # a[j:]=[31]
# # print(a)
# # # p=input("enter:")
# # # for n in range(j):
# # #     if c[k]==a[n]:
# # #         a[n]=p
# # # y=(a)
# # # print(y)
    




a="divija"
r=0
for i in (a):
    r=r+1
length=(r)
k=" "
for j in range(length):
    s=1
    for i in range(j+1,length):
        if a[j]==a[i]:
            s=s+1
    if a[j] not in k:
        k=k+str(s)+a[j]
print(k)





# # s=""
# # for j in[i for i in "divija is good girl " if i!=" "]:
# #     s=s+j
# # print(s)

# ascending the list
# # l=[1,5,8,8,41,-1]
# # c=0
# # for i in l:
# #     c=c+1
# # k=c
# # p=0
# # while p<k:
# #     for s in range(k-p-1):
# #            if l[s] <l[s+1]:
# #                 l[s],l[s+1]=l[s+1],l[s]

# #     p+=1
# # print(l)


# a="asd asdf erfg awer"
# b=[]
# c=" "
# for i in range(len(a)):
#     if a[i]==" ":
#         b=b+c
#         c=" "
#     else:
#       b=b+i
# c=c+[b]
# print(b)


# a="bobbysdfghjssssss"
# s=a[0]+""
# for i in range(1,len(a)):
#     if a[i]==a[0]:
#         s+="$"
#     else:s+=a[i]
# print(s)


# string dividing without using split

# a="divi chell now"
# f=[]
# b=0
# e=0
# for i in range(len(a)):
#     if a[i]==" ":
#         s=a[b:e]
#         b=i+1
#         f=f+[s]
        
#     else:
#         e=i+1
# f=f+[a[b:e]]

# print(f)

# enumerate function
# a=["sdfg" ,"frtgb"]
# b="wergt frgt"
# for s,i in enumerate(a,2):
#     print(s,"------",i)


# # print(list(enumerate(a,2)))


# t=[]
# print(len(t))