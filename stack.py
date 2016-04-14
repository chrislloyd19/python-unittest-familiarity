from linked_list import *

class Stack(object):
	def __init__(self):
		self.linked_list = LinkedList()

	def push(self, data):
		node = Node(data)
		self.linked_list.prepend(node)

	def pop(self):
		return self.linked_list.remove_first()