import numpy as np

#Declaracao das matrizes que serao invertida

a = np.matrix([[0,1,3],[3,-1,2],[-2,2,-4]],dtype=float)
#a = np.matrix([[2,4,3],[0,6,5],[0,0,2]],dtype=float)
#a = np.matrix([[2,0,0],[3,4,0],[4,5,6]],dtype=float)
#a = np.matrix([[4,-1,0],[-1,4,-1],[0,-1,4]],dtype=float)
#a = np.matrix([[1,2,4],[1,3,9],[1,4,16]],dtype=float)
#a = np.matrix([[1,0.5,0.25,0.125],[0,1,0.33,0.11],[0,0,1,0.25],[0,0,0,1]],dtype=float)
#a = np.matrix([[1,3,-9,6,4],[2,-1,6,7,1],[3,2,-3,15,5],[8,-1,1,4,2],[11,1,-2,18,7]],dtype=float)
print(a)
print("----------------------------------------------------")

#Ininci uma matriz com os pivos com valor de 1
inv = np.zeros(shape=(len(a),len(a)))
for i in range(0,len(inv)):
    for j in range(0,len(inv)):
        if(i==j):
            inv[i,j]=1

#Executa uma substituicao simples caso algum pivo da matriz original seja 0
for i in range(0,len(a)):
    if(a[i,i] == 0 and a[i+1,i] != 0):
       mat = a[i,:].copy()
       matinv = inv[i,:].copy()
       a[i,:] = a[i+1,:]
       inv[i,:] = inv[i+1,:]
       a[i+1,:] = mat
       inv[i+1,:] = matinv
#Executa a eliminacao da parte inferior da matriz
for i in range(1,len(a)):
    for j in range(0,len(a)-1):
        if(i!=j):
            if(a[i,j] != 0 and i>j):
                inv[i,:] = inv[i,:] - a[i,j]*inv[j,:]/a[j,j]
                a[i,:] = a[i,:] - a[i,j]*a[j,:]/a[j,j]
#Executa a operacao que deixa os pivos com valor de 1
for i in range(0,len(a)):
    inv[i,:] = inv[i,:]/a[i,i]
    a[i,:]=a[i,:]/a[i,i]
#Executa a eliminacao para a parte superior do matriz
for i in range(1,len(a)):
    for j in range(0,len(a)-1):
        if(i!=j):
            if(a[j,i] != 0):
                inv[j,:] = inv[j,:] - a[j,i]*inv[i,:]/a[i,i]
                a[j,:] = a[j,:] - a[j,i]*a[i,:]/a[i,i]

print(inv)