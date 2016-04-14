class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def prepend(self, node):
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def remove_first(self):
		if self.head is None:
			return None
		else:
			popped = self.head
			if self.head.next is not None:
				self.head = self.head.next
			else:
				self.head = None
			return popped.data