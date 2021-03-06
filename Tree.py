class Tree :
	def __init__(self,initial=None) :
		self.value = initial
		if self.value:
			self.left = Tree()
			self.right = Tree()
		else:
			self.left = None
			self.right = None
		return
	
	def isempty(self) :
		return (self.value == None)
	
	def isleaf(self):
		return (self.left.isempty() and self.right.isempty())
	
	def makeempty(self) :
		self.value = None
		self.left = None
		self.right = None
		return
	
	def copyright(self) :
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right
		return
	
	def copyleft(self) :
		self.value = self.left.value
		self.left = self.left.left
		self.right = self.left.right
		return
	
	def find(self,v) :
		if self.isempty() :
			return(False)
		if self.value == v :
			return(True)
		if v < self.value :
			return (self.left.find(v))
		if v > self.value :
			return (self.right.find(v))
	
	def maxvel(self) :
		if self.right.isempty() :
			return (self.value)
		else:
			return (self.right.maxval())
	
	def insert(self,v) :
		if self.isempty() :
			self.value = v
			self.left = Tree()
			self.right = Tree()
		if self.value == v :
			return
		if v < self.value :
			self.left.insert(v)
			return
		if v > self.value :
			self.right.insert(v)
			return
	
	def delete(self,v) :
		if self.isempty() :
			return
		if v < self.value :
			self.left.delete(v)
			return
		if v > self.value :
			self.right.delete(v)
			return
		if v == self.value :
			if self.isleaf() :
				self.makeempty()
			elif self.left.isempty() :
				self.copyright()
			else :
				self.value = self.left.maxval()
				self.left.delete(self.left.maxval())
			return
	
	def inorder(self) :
		if self.isempty() :
			return ([])
		else :
			return (self.left.inorder() + [self.value] + self.right.inorder())
	
	def __str__(self):
		return (str(self.inorder()))

t = Tree()
print(t)
for i in [1,3,2,18,10,4,5,20,22,14] :
	t.insert(i)
print(t)
