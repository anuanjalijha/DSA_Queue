from sys import stdin
import queue



class Stack :
	def __init__(self):
		self.q1 = queue.Queue()
		self.q2 = queue.Queue()
		

	#Define data members and __init__()




	'''----------------- Public Functions of Stack -----------------'''


	def getSize(self) :
		return self.q1.qsize() 
		#Implement the getSize() function



	def isEmpty(self) :
		return self.getSize()==0
		#Implement the isEmpty() function



	def push(self, data) :
		#Implement the push(element) function
		self.q1.put(data)
		




	def pop(self) :

		if self.isEmpty():
			return -1
		while self.q1.qsize()>1:
			self.q2.put(self.q1.get())
		
		ans = self.q1.get()
		temp = self.q1
		self.q1 = self.q2 
		self.q2 = temp


		# self.__q1,self.__q2 = self.__q2,self.__q1
		
	
		return ans	



		#Implement the pop() function



	def top(self) :
		if self.isEmpty():
			return -1
		while self.q1.qsize()>1:
			self.q2.put(self.q1.get())
		ans = self.q1.get()
		self.q2.put(ans)
		temp = self.q1
		self.q1 = self.q2 
		self.q2 = temp
		# self.__q1, self.__q2 = self.__q2, self.__q1
		return ans	
		#Implement the top() function
