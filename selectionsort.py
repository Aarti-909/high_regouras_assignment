# a = int(input("enter num: "))
# i=0
# p=[]
# while i<a:
#     k=int(input("enter your elements: "))
#     p.append(k)
#     i+=1
# print(p)
# b=int(input("enter num u want to check: "))
# j=0
# c=0
# while j<len(p):
#     if p[j]==b:
#         c+=1
#     j+=1
# if c>=1:
#     print("yes")
# else:
#     print("no")
     

# ----------------------------------------------REVERSE ARRAY---------------------------------------


# a = int(input("enter num: "))
# i=0
# c=0
# p=[None]*a
# while i<a:
#     k=int(input("enter your elements: "))
#     p[i]=k
#     i+=1
# print(p)
# l=[None]*a
# while c<len(p):
#     d=p[-c-1]
#     l[c]=d
#     c+=1
# print(l)


# ---------------------------------------MEAN MEDIAN AND MODE----------------------------------------
# i=0
# sum=0
# a = int(input("enter num: "))
# c=0
# p=[]
# while i<a:
#     k=int(input("enter your elements: "))
#     sum+=k
#     p.append(k)
#     i+=1
# print(p)
# print("mean of array is",sum/len(p))

# ------------------------------median--------------------------------------------
# a=int(input("enter num: "))
# i=0
# b=[None]*a
# while a>i:
#   c=int(input("num: "))
#   b[i]=c
#   i+=1
# if a%2!=0:
#   print((a+1)//2)
# else:
#   k=a//2
#   d=(a//2)+1
#   print((b[k]+b[d])/2)

# ---------------------------------------------------------------------------------------------

# a = int(input("enter num: "))
# i=0
# p=[]
# while i<a:
#     k=int(input("enter your elements: "))
#     p.append(k)
#     i+=1
# print(p)
# k=0
# while k<len(p):
#     j=1
#     while j<len(p):
#         if p[k]==p[j]:
#             print(p[k])
#             k+=1
#         j+=1
#     i+=1


# x = [3,1,6,8,2]
# # x = ["Aarti","aarti"]
# a = 0
# while a<len(x):
#     j=0
#     while (j+1)<len(x):
#       if x[j]>x[j+1]:   #for desecnding order just convert the sign
#         x[j],x[j+1]=x[j+1],x[j]
#       else:
#         x[j],x[j+1]=x[j],x[j+1]
#       j+=1
#     a+=1
# print(x)

# ------------------------------------------------------------------------------------------------
# a=int(input("num: "))
# i=0
# e=[None]*a
# f=[None]*a
# while a>i:
#     b=int(input("num1: "))
#     c=int(input("num2: "))
#     e[i]=b
#     f[i]=c
#     i+=1
# print(e)
# print(f)
# k=[]
# p=0
# while p<a:
#     j=0
#     while (j)<a:
#         if e[j]>f[j]:
#             e[j],f[j]=f[j],e[j]
#             k.append(e[j])
#             k.append(f[j])
#         else:
#             e[j],f[j]=e[j],f[j]
#             k.append(e[j])
#             k.append(f[j])
#             j+=1
#         p+=1
# print(k)

# --------------------------------------SELECTION SORT-----------------------------------
# a=[10,4,68,102338,74,7]
# i=0
# min=0
# k=[]
# while i<len(a):
#     if a[i]<min:
#         k.append(min)
#     else:
#         min=a[i]
#         k.append(min)
#     i+=1
# # print(k)

# a=[10,4,68,102338,74,7]
# i=0
# while i<len(a):
#     min=i
#     j=i+1
#     while j<len(a):
#         if a[j]<a[min]:
#             min=min
#         else:
#             min=a[j]
#         i+=1
# print(min)


# a=[10,4,68,102338,74,7,1]
# i=0
# min=i
# j=i+1
# while i<len(a):
#     if a[j]<min:
#         min=min
#     else:
#         min=a[j]
#         j+=1
#     i+=1
# print(min)


# a=[10,4,68,102338,74,7,1]
# i=1
# min=a[0]
# n=[]
# b=len(a)
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#         n.append(min)
#         j=0
#         while j+1<len(a):
#             if a[j]<min:
#                 a[j]=min
#                 n.append(min)
#             else:
#                 min=min
#                 n.append(min)
#             j+=1
#     i+=1
# print(min)  
# print(n)


# a=int(input("enter num: "))
# b=[0]*a
# i=0
# while i<a:
#     n=int(input())
#     b[i]=n
#     i+=1
# print(b)


# a=[10,4,68,102338,74,7,1]
# i=0
# min=a[0]
# b=[]
# while i<len(a):
#     if a[i]<min:
#         min,a[i]=a[i],min
#         b.append(min)
#     else:
#         min,a[i]=min,a[i]
#         b.append(a[i])
#     i+=1
# print(min)
# print(b)



# a=[12,54,758,11,876,2,2,25]
# b=len(a)
# i=0
# while i<b:
#     min=i
#     j=0
#     while j+1<b:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[i],a[min]=a[min],a[i]



# -----------------------------------------------------------------------------------------

# a=[1,2,3,4]
# b=[2,4,5,6,7]
# i=0
# j=0
# c=[]
# while i<len(a):
#   j=0
#   while j<i:
#     if a[i]>b[j]:
#       c.append(a[i])
#     elif a[i]==a[j]:
#       c.append(a[i])
#     else:
#       c.append(a[j])
#     j+=1
#   i+=1
# print(c)

# a=[6,7,8,9]
# b=[2,4,5,6,7,34,6,2,3]
# c=[]
# i=0
# j=0
# a=int(input("enter num: "))
# i=0
# c=[None]*a
# e=[None]*a
# while i<a:
#     b=int(input("enter num: "))
#     d=int(input("hello: "))
#     c[i]=b
#     e[i]=d
#     i+=1
#     k=[None]*(a+a)
#     while i<(a):
#         j=0
#         while a>j:
#             if c[i]==e[j]:
#                 k[j]=c[i]
#                 # c.append(a[i])
#             j+=1
#         i+=1
# print(k)


# ================================================================================================

# Merge two sorted array:-------------------------------------------------------------------------

# a=int(input("enter len of list1: "))
# b=int(input("enter len of list2: "))
# i=0
# j=0
# a1=[None]*a
# b1=[None]*b
# while i<a:
#   a2=int(input("num: "))
#   a1[i]=a2
#   i+=1
# while j<b:
#   b2=int(input("num: "))
#   b1[j]=b2
#   j+=1

# print(b1)
# print(a1)

# c=[]
# k=0

# while k<a:
#     x=0
#     while x<a:
#         if a1[k]>b1[x]:
#             c.append(b1[x])
#             b1[x]="A"
#         x+=1
#     c.append(a1[k])
#     k+=1
# for d in range (b):
#   if b1[d]!="A":
#     c.append(b1[d])
# print(a1)
# print(b1)
# print(c)



# ==================================================================================================

# MODE

# a=int(input("num: "))
# i=0
# a1=[0]*a
# while a>i:
#   n=int(input("num: "))
#   a1[i]=n
#   i+=1
# j=0
# c=0
# while j<a:
#   c1=0
#   k=0
#   while k<a:
#     if a1[k]==a1[j]:
#       c1+=1
#     k+=1
#   if c<c1:
#     c=c1
#     i=a[j]
#   j+=1
# print("mode is: " ,i )

# ----------------------------------------------------------------------------------------------------

# ROTATION

# a=int(input("num: "))
# i=0
# b=[None]*a
# while a>i:
#     n=int(input("num2: "))
#     b[i]=n
#     i+=1
# j=0
# a1=[0]*a
# k=int(input("enter num of rotation: "))
# while j<(a**2):
#     c=0
#     p=0
#     while c<=k:
#         if b[p]=="A":
#             pass
#         elif c==3:
#             a1[j]=b[p]
#             b[p]="A"
#         c+=1
#         p+=1
#     j=(j+1)%a
# print(a1)

# M------------------A-------------------------I-------------------------------N-----------------
# a=int(input("num: "))
# i=0
# b=[0]*a
# while a>i:
#     n=int(input("num2: "))
#     b[i]=n
#     i+=1
# j=0
# a1=[0]*a
# k=int(input("enter num of rotation: "))
# t=0
# c=0
# s=0
# while t<a:
#     if b[j]!="A":
#         c+=1
#     if c==k:
#         a1[s]=b[j]
#         b[j]="A"
#         t+=1
#         c=0
#         s+=1
#     j=(j+1)%a
# print(a1)
# ----------------------------------------------------------------------------------------------------

# INTERSECTION AND UNION: 

# a=[6,7,8,9]
# b=[2,4,5,6,7,7]
# a1=int(input("nm1: "))
# b1=int(input("num2: "))
# a=[0]*a1
# b=[0]*b1
# k=0
# l=0
# while k<a1:
#   n=int(input("num: "))
#   a[k]=n
#   k+=1
# while l<b1:
#   n1=int(input("num: "))
#   b[l]=n1
#   l+=1
# print(a)
# print(b)
# c=[]
# i=0
# while i<a1:
#     j=0
#     while b1>j:
#       if b[j]=="A":
#         pass
#       elif a[i]==b[j]:
#         c.append(b[j])
#         b[j]="A"
#       j+=1
#     i+=1
# print(c)
# p=0
# A = a1
# B = b1
# s=[]
# if A<B:
#     A,B=B,A
# while A>p:
#   if p>=len(a):
#     pass
#   elif a[p]!="A":
#     s.append(a[p])
#   if p>=len(b):
#     pass
#   elif b[p]!="A":
#     s.append(b[p])
#   p+=1
# print(s)



# contiguous sum:----------------------------------------------------------------------

    
# N=int(input("enter num: "))
# i=0
# a=[None]*N
# while N>i:
#   n=int(input("num: "))
#   a[i]=n
#   i+=1
# p=0
# j=1
# s=int(input("num: "))
# while j<N:
#   if a[p]+a[j]==s:
#     print(a[p],a[j])
#   j+=1
#   p+=1



# -------BINARY SEARCH------==========----------------==========-------------==========------------===========



# a=int(input("num: "))
# i=0
# n=[0]*a
# while a>i:
#     n[i]=int(input("num2: "))
#     i+=1
# print(n)
# c=int(input("num u want to check: "))
# min=0
# max=len(n)
# mid=0
# i=0
# k=False
# while i<len(n):
#     mid=(min+max)//2
#     if n[mid]==c:
#         print("yes")
#         k=True
#         break
#     elif n[mid]<c:
#         min=mid
#         max=max

#     else:
#         max=mid
#     i+=1
# if k==False:
#     print("element not present")


# --------------------s------i------e--------v----------e------------------------------
# a=int(input("num: "))
# i=0
# n=[0]*a
# while a>i:
#     n[i]=1
#     i+=1
# print(n)
# j=0
# while j<a:
#     if j!=2 and j%2==0:
#         n[j]=0
#     elif j!=3 and j%3==0:
#         n[j]=0
#     elif j!=5 and j%5==0:
#         n[j]=0
#     elif j!=7 and j%7==0:
#         n[j]=0

#     j+=1
# print(n)
# k=[]
# for i in range (a):
#     if i==1:
#         pass
#     elif n[i]!=0:
#         k.append(i)
# print(k)

# w--------r-------o------n--------------------g(incomplete)



# n=int(input())
# a=[1]*n
# for i in range(2,n):
#     if a[i]==1:
#         for j in range(i*i,n,i):
#             a[j]=0
# for i in range(2,n):
#     if a[i]==1:
#         print(i,end=" ")


# t=int(input())
# for i in range (t):
#     n=int(input())
#     j=0
#     while j<n:
#         n=list(map(int,input().split()))
#         p=0
#         while p<n:
#             n=list(map(int,input().split()))
#             p+=1
#         j+=1
 
# t=int(input())
# for i in range (t):
#     n=int(input())
#     n1=list(map(int,input().split()))
#     n2=list(map(int,input().split()))
#     k=1
#     c=0
#     if n1[0]>=n2[2]:
#         c+=1
#     while k<n:
#         if (n1[k]-n1[k-1])>n2[k]:
#             c+=1
#         k+=1
#     print(c)


# T=int(input())
# i=0
# while T>i:
#     n,k=map(int,input().split())
#     if k=0 and (4+n)%2!=0:
#         print("on")
#     elif k=0 and (4+n)%2==0:
#         print("off")
#     elif k=1 and n==0:
#         print("on")
#     elif k=1:
#         print("ambiguous")
#     i+=1

# t=int(input())
# i=0
# while t>i:
#     n,k=map(int,input().split())
#     if k==0 and (4+n)%2!=0:
#         print("on")
#     elif k==0 and (4+n)%2==0:
#         print("off")
#     elif k==1 and n==0:
#         print("on")
#     elif k==1:
#         print("ambiguous")
#     i+=1