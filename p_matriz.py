#!/usr/bin/python3
import time
import csv
import threading
import pandas as pd

class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.val = 0

	def run_thread(self, matrizA, matrizB, i):
		for j in range(len(matrizA)):
			for k in range(len(matrizA)):
				self.val += int(matrizA[i][k])*int(matrizB[k][j])
		return self.val

def prodMatrix_con(matrizA, matrizB):
	sizeA = len(matrizA)
	matrizR = []
	
	for i in range(sizeA):	
		matrizR.append([])
		thread1 = myThread()
		thread1.start()
		val = thread1.run_thread(matrizA,matrizB,i)
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

def get_matrix(dim):
	file_name = "Matrizes/A"+str(dim)+"x"+str(dim)+".txt"
	mA = open(file_name, 'r')
	mB = open(file_name, 'r')

	matrizA = list((line.split()) for line in mA if line.strip())
	matrizB = list((line.split()) for line in mB if line.strip())
	del(matrizA[0])
	del(matrizB[0])
	return matrizA, matrizB

if __name__ == "__main__":
	
	import sys
	if (len(sys.argv)<3):
		print ("Modo de Análise")
		exe = 'A'
	else: 
		dim = sys.argv[1]
		exe = sys.argv[2]
	#sequencial
	if (exe is 'S'): 
		matrizA, matrizB = get_matrix(dim)
		ini = time.time()
		matrizR = prodMatrix_seq(matrizA, matrizB)
		fim = time.time()
		print ("Tempo de execução sequencial: ", (fim-ini))
	#concorrente
	elif (exe is 'C'): 
		matrizA, matrizB = get_matrix(dim)
		ini = time.time()
		matrizR = prodMatrix_con(matrizA, matrizB)   
		fim = time.time()
		print ("Tempo de execução concorrente: ", (fim-ini))
	#analise
	elif(exe is 'A'):
		dime = [4,8,16,32,64,128,256,512,1024,2048]
		for d in dime:
			csv_name = str(d)+"x"+str(d)+".csv"
			matrizA, matrizB = get_matrix(d)
			metric_list = [['ID', 'SEQ', 'CONC']]

			for i in range(20):
				lista_tempo = []
				lista_tempo.append(i)
				print(i, "-", csv_name)

				ini = time.time()
				matrizR = prodMatrix_seq(matrizA, matrizB)
				fim = time.time()
				lista_tempo.append(fim-ini)
				print ("sequencial:", fim-ini)
				ini = time.time()
				matrizR = prodMatrix_con(matrizA, matrizB)
				fim = time.time()
				lista_tempo.append(fim-ini)
				print ("concorrente:", fim-ini)			
				metric_list.append(lista_tempo)
		
			with open(csv_name, 'wt') as file:
				writer = csv.writer(file)
				writer.writerows(metric_list)

	else:
		print ("ERRO")	
	file_name = "C"+dim+"x"+dim+".txt"
	arq = open(file_name, 'w')
	for linha in matrizR:
		for elem in linha: 
			arq.write(str(elem))
			arq.write(" ")
		arq.write("\n")
	arq.close()