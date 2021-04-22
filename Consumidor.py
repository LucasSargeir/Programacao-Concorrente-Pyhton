import threading
import time
from Numero import Numero

class Consumidor(threading.Thread):
	def __init__(self, numero: Numero, nome: str, limit:int = 10, sleep_time:int = 2):
		threading.Thread.__init__(self)
		self.numero = numero
		self.nome = nome
		self.limit = limit
		self.sleep_time = sleep_time

	def run(self):
		valor  = []
		numero = 0

		while numero < 10:
			numero = self.numero.consumir(self.nome, self.limit)
			if numero != -1:
				valor.append(numero)
			else:
				break
			time.sleep(self.sleep_time)

		time.sleep(self.sleep_time)
		print(f'Consumidor {self.nome} consumiu -> {valor}')
