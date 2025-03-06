list=[]
count=0
with open("crypted.txt") as f:
    for linea in f:
        if linea == '-- end --\n':
            list.append(count)
            count=0
        count=count+1
        
print("File criptato")
for i in list:
    print(i)
    

lista2=[]   
with open("words.txt") as f:
    for parola in f:
        lista2.append(parola)
        
lista2.sort()

alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter=[]
count=0
i=0
for parola in lista2:
    if parola[0]==alfabeto[i]:
        count=count+1
    else:
        counter.append(count)
        count=1
        i=i+1

print("File word")
