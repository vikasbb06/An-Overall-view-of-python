# n=[12,13,14,15,16,17,18,19,20]
# for i in n:
#     if i%2==1:
#         continue
#     print("Even Number:", i)
# for i in n:
#     if i%2==1:
#         break
#     print("\t", i)
# print("Done")
# str="Hello World"
# vowels="aeiou"
# res=" "
# for ch in str:
#     if ch not in vowels :
#         res+=ch
# print(res)
def matrix(a,b,n):
    c=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]+=a[i][k]*b[k][j]
    return c

n=int(input("Enter the size of the matrix: "))   
a=[[0 for _ in range(n)] for _ in range(n)]
b=[[0 for _ in range(n)] for _ in range(n)]
print("Enter the elements of the first matrix:")
for i in range(n):
    for j in range(n):
        a[i][j]=int(input(f"Enter element [{i}][{j}]:"))
print("Enter the elements of the second matrix:")
for i in range(n):
    for j in range(n):
        b[i][j]=int(input(f"Enter element [{i}][{j}]: "))
result=matrix(a,b,n)
for row in result:
    print(f"rows is :{row}")