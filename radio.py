
def check_interval(tFile,tPrograma):
    tolerance = 0.03; #Tolerância de 3%
    if(tFile > (tPrograma * (1 + tolerance))):
        print("A duração do ficheiro excede em 3% ou mais o tempo do programa")
        validade = 0
		
    elif(tFile < (tPrograma * (1 - tolerance))):
        print("O ficheiro tem 3% ou mais a menos de duração do que a duração normal do programa")
        validade = 1
    else:
        print("A duração do ficheiro está entre os limites definidos para o programa")
        validade = 1
    return validade;
	
#Idealmente teriamos uma possivel matriz 2 x n (Lista[Filename[],tPrograma[]])
#Onde na primeira coluna temos um vetor que contém o nome de cada ficheiro a verificar (Filename[])
#e na segunda coluna temos o tipo/duração do tipo de programa (tPrograma[])

#for x in range (0,len(Filename))
#    tFile[x] = get_tFile(Filename[x])
	
	
tFile = []
tPrograma = []	

#Feito à mão para testes
tFile.append(1670) #Tempo dentro do intervalo para programas com duração de 28 minutos / 1680 segundos
tFile.append(3419) #Tempo dentro do intervalo para programas com duração de 57 minutos / 3420 segundos
tFile.append(7020) #Tempo dentro do intervalo para programas com duração de 117 minutos /7020 segundos
tFile.append(1740) #Tempo excedente em mais de 3% para programas com duração de 28 minutos / 1680 segundos
tFile.append(5000) #Tempo excedente em mais de 3% para programas com duração de 57 minutos / 3420 segundos
tFile.append(10000) #Tempo excedente em mais de 3% para programas com duração de 117 minutos /7020 segundos
tFile.append(1000) #Tempo com 3 ou menos % da duração esperada para programas com duração de 28 minutos / 1680 segundos
tFile.append(2500) #Tempo com 3 ou menos % da duração esperada para programas com duração de 57 minutos / 3420 segundos
tFile.append(4000) #Tempo com 3 ou menos % da duração esperada para programas com duração de 117 minutos /7020 segundos


t1 = 1680 #segundos // 28 minutos
t2 = 3420 #segundos // 57 minutos
t3 = 7020 #segundos // 117 minutos

tPrograma.append(t1) #Tempo dentro do intervalo para programas com duração de 28 minutos / 1680 segundos
tPrograma.append(t2) #Tempo dentro do intervalo para programas com duração de 57 minutos / 3420 segundos
tPrograma.append(t3) #Tempo dentro do intervalo para programas com duração de 117 minutos /7020 segundos
tPrograma.append(t1) #Tempo excedente em mais de 3% para programas com duração de 28 minutos / 1680 segundos
tPrograma.append(t2) #Tempo excedente em mais de 3% para programas com duração de 57 minutos / 3420 segundos
tPrograma.append(t3) #Tempo excedente em mais de 3% para programas com duração de 117 minutos /7020 segundos
tPrograma.append(t1) #Tempo com 3 ou menos % da duração esperada para programas com duração de 28 minutos / 1680 segundos
tPrograma.append(t2) #Tempo com 3 ou menos % da duração esperada para programas com duração de 57 minutos / 3420 segundos
tPrograma.append(t3) #Tempo com 3 ou menos % da duração esperada para programas com duração de 117 minutos /7020 segundos


for y in range (0,len(tFile)):
    validade = check_interval(tFile[y],tPrograma[y])
    print("Validade = ",validade, "\n")
	
input("Pressiona enter para sair")