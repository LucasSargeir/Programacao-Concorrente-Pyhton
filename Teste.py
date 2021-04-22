from Numero import Numero
from Produtor import Produtor
from Consumidor import Consumidor
import threading

if __name__ == '__main__':

	n = Numero(0)
	p = Produtor(n, 'P1')
	c1 = Consumidor(n, 'C1')
	c2 = Consumidor(n, 'C2')
	c3 = Consumidor(n, 'C3')

	p.start()
	c1.start()
	c2.start()
	c3.start()
	
	main_thread = threading.currentThread()
	for t in threading.enumerate():
		if t is not main_thread:
			t.join()