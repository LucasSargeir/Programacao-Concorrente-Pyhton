import threading

class Numero:
	
	def __init__(self, numero: int):
		self.__numero = numero
		self.__disponivel = False
		self.__condition = threading.Condition() 

	def consumir(self, id_thread: str, limit: int)->int:
			
		with self.__condition:
			
			while self.__disponivel == False:
				self.__condition.wait()
				if self.__numero >= limit:
					return -1

			print(f'\tConsumidor {id_thread}', end = ' ')
			print(f'consumiu:\t{self.__numero}\n')
			self.__disponivel = False				

			self.__condition.notifyAll()

			return self.__numero

	def produzir(self, id_thread: str, valor: int):
		
		with self.__condition:	
			while self.__disponivel == True:
				self.__condition.wait()

			self.__disponivel = True
			self.__numero = valor

			self.__condition.notifyAll()

			print(f'Produtor {id_thread}', end = ' ')
			print(f'produziu:\t{valor}')
