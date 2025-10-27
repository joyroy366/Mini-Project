lst_id=[2,1,2,2,5,1,0,3,3,6,6]
unique_id = []
for item in lst_id:
    if item not in unique_id:
        unique_id.append(item)
print(unique_id)
a=len(unique_id)

lst_chr=["J","O","Y","R","O","Y"]
unique_chr = []
for item in lst_chr:
    if item not in unique_chr:
        unique_chr.append(item)

b=len(unique_chr)
if a>b:
    i=b
    c=a-b
    for i in range(c):
        unique_chr.append("*")

print(unique_chr)

user_input=input("Enter your Number :")
lst=[int(digit) for digit in str(user_input)]
print(lst)

output_lst=[]

for  i in range(len(lst)):
    if  lst[i] not in unique_id :
        output_lst.append(lst[i])
    else:
      for j in range(len(unique_id)):
          if lst[i]==unique_id[j]:
              output_lst.append(unique_chr[j])
print(output_lst)

for i in range(len(output_lst)):
    print(output_lst[i] , end = "")
