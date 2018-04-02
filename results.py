import numpy as np
import matplotlib.pyplot as plt
import csv


dime = [4,8,16,32,64,128,256,512,1024,2048]
medias_s = []
medias_c = []
speedup = 0
t_seq = 0
t_conc = 0

tabela = [['type','dim','max','med','min']]
for d in dime:
	csv_name = str(d)+"x"+str(d)+".csv"
	file_data = open(csv_name, 'r')
	data = csv.reader(file_data)
	seq = []
	conc = []
	media_c = 0
	media_s = 0
	for line in data:
		if (line[1] == 'SEQ' or line[2] == 'CONC'):
			pass
		else:
			seq.append(float(line[1]))
			conc.append(float(line[2]))
			media_s += float(line[1])
			media_c += float(line[2])
	del(seq[0])
	del(conc[0]) 
	lets = []
	medias_s.append(media_s/(len(seq)+1))
	medias_c.append(media_c/(len(conc)+1))
	
	tabela.append(['S', d, max(seq), media_s/(len(seq)+1), min(seq)])
	tabela.append(['C', d, max(conc), media_c/(len(conc)+1), min(conc)])

	x = np.array(range(len(seq)))
	plt.title(str(d)+"x"+str(d))
	plt.plot(x,seq, label="Sequencial")
	plt.plot(x,conc, label="Concorrente")
	plt.grid(True)
	plt.xlabel("Execução")
	plt.ylabel("Tempo")
	plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
	fname = str(d)+"x"+str(d)
	plt.tight_layout()	
	plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)
	plt.show()

x = np.array(range(len(medias_s)))
plt.title('Médias')
plt.plot(medias_s)
plt.plot(medias_c)
plt.grid(True)
plt.xlabel("Dimensão")
plt.ylabel("Tempo")
plt.tight_layout()	
plt.savefig("medias", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)
plt.show()

for i in medias_s:
	t_seq += i 
for i in medias_c:
	t_conc += i

speedup = t_seq/t_conc
print ('speedup: ',speedup)

file_name = "analise_tempos.csv"
arq = open(file_name, 'w')
for linha in tabela:
	for elem in linha: 
		arq.write(str(elem))
		arq.write(",")
	arq.write("\n")
arq.close()
