import threading
import time
from Numero import Numero

class Produtor(threading.Thread):
	def __init__(self, numero: Numero, name: str, limit:int = 10, sleep_time:int = 1):
		threading.Thread.__init__(self)
		self.numero = numero
		self.name = name
		self.limit = limit
		self.sleep_time = sleep_time

	def run(self):
		for i in range(0,self.limit + 1):
			self.numero.produzir(self.name, i)
			time.sleep(self.sleep_time)