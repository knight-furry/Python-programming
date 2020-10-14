class Node:
	def __init__(self,v = None):
		self.value = v
		self.next = None
		return
	
	def isempty(self):
		if self.value == None:
			return (True)
		else:
			return (False)
	
	def append(self,v):
		if self.isempty():
			self.value = v
		elif self.next == None:
			newnode = Node(v)
			self.next = newnode
		else:
			self.next.append(v)
		return
	
	def insert(self,v):
		if self.isempty():
			self.value = v
			return
		newnode = Node(v)
		(self.value,newnode.value) = (newnode.value,self.value)
		(self.next,newnode.next) = (newnode.next,self.next)
		return
	
	def delete(self,v):
		if self.isempty():
			print ("Empty list...!")
			return
		if self.value == v:
			self.value = None
			if self.next != None:
				self.next = self.next.value
				self.next = self.next.next
			return
		else:
			if self.next != None:
				self.next.delete(v)
				if self.next.value == None:
					self.next = None
		return
	
	def __str__(self):
		selflist = []
		if self.value == None:
			return (str(selflist))
		temp = self
		selflist.append(temp.value)
		while temp.next != None:
			temp = temp.next
			selflist.append(temp.value)
		return (str(selflist))
H = Node(5)