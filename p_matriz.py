#!/usr/bin/python3
import time
import threading

class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.val = 0

	def run_thread(self, matrizA, matrizB, i, j	):
		for k in range(len(matrizA)):
			self.val += int(matrizA[i][k])*int(matrizB[k][j])
		return self.val

def prodMatrix_con(matrizA, matrizB):
	sizeA = len(matrizA)
	matrizR = []
	
	for i in range(sizeA):	
		matrizR.append([])
		for j in range(sizeA):
			thread1 = myThread()
			thread1.start()
			val = thread1.run_thread(matrizA,matrizB,i,j)
			matrizR[i].append(val)
	return matrizR

def prodMatrix_seq(matrizA, matrizB):
	sizeA = len(matrizA)
	sizeB = len(matrizB)
	matrizR = []
	
	for i in range(sizeA):
		
		matrizR.append([])

		for j in range(sizeA):
			
			val = 0
			for k in range(sizeA):
				val += int(matrizA[i][k])*int(matrizB[k][j])
			matrizR[i].append(val)
	return matrizR

if __name__ == "__main__":
	
	import sys
	dim = sys.argv[1]
	exe = sys.argv[2]

	file_name = "Matrizes/A"+dim+"x"+dim+".txt"
	mA = open(file_name, 'r')
	mB = open(file_name, 'r')

	matrizA = list((line.split()) for line in mA if line.strip())
	matrizB = list((line.split()) for line in mB if line.strip())
	del(matrizA[0])
	del(matrizB[0])
	ini = time.time()
	if (exe is 'S'): 
		matrizR = prodMatrix_seq(matrizA, matrizB)
		fim = time.time()
		print ("Tempo de execução sequencial: ", (fim-ini))

	elif (exe is 'C'): 
		matrizR = prodMatrix_con(matrizA, matrizB)   
		fim = time.time()
		print ("Tempo de execução concorrente: ", (fim-ini))

	else:
		print("ERRO NA ENTRADA")
	fim = time.time()
	
	file_name = "C"+dim+"x"+dim+".txt"
	arq = open(file_name, 'w')
	for linha in matrizR:
		for elem in linha: 
			arq.write(str(elem))
			arq.write(" ")
		arq.write("\n")
	arq.close()