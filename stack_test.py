from stack import *
import unittest

class StackTestCase(unittest.TestCase):
	""" Tests for stack.py """

	def test_empty_stack_pop(self):
		""" Return None if empty stack popped """
		stack = Stack()
		self.assertIs(stack.pop(), None)

	def test_simple_push_pop(self):
		""" Does the stack return the correct pushed value when popped? """
		stack = Stack()
		stack.push(71)
		self.assertEqual(stack.pop(), 71)

	def test_big_push_pop(self):
		""" Can the stack handle a lot of values? """
		stack = Stack()
		numbers = range(99999)

		for number in numbers:
			stack.push(number)

		popped = stack.pop()
		start = popped
		while popped:
			self.assertEqual(start, popped)
			popped = stack.pop()
			start -= 1

if __name__ == '__main__':
	unittest.main()