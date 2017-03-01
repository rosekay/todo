#Todo console Application
#functions:
	# todo create
	# todo open
	# item add
	# todo list
	# todo <todo name or todo id>
	# list items <by name or by id>

class ToDo(object):	

	id_ = 0
	todos = {}
	item_id = 0
	def todo_create(self, name):
		self.todo_task = name
		self.id_ += 1
		self.todos = {self.id_ : [self.todo_task]}
		return "Created: %s" % self.todo_task

	def todo_open(self, name):
		for key, value in self.todos.iteritems():
			if name in value or id_ in key:
				return "Opened: %s" % self.todos[key] 
			return "No ToDo with that name"	

	def item_add(self, item):
		self.added = item
		self.item_id += 1
		self.item_added = {self.item_id: self.added}
		self.todos[self.id_].append([self.added])
		return "You added:\n %s IN: %s"% (self.added, self.todos[self.id_][0])


	def todo_list(self):
		return self.todos[self.id_]

	def item_list_by_name(self, name):
		for key in self.item_added:
			if name == key:
				return self.item_added[key]
			return "No such Item"	

	def item_list_by_id(self, idd):
		for key in self.item_added:
			return [value for value in self.item_added.values() if idd == key]

rose = ToDo()

print rose.todo_create('Books to read')
print rose.todo_open("Books to read")
print rose.item_add("Java Script: the Good parts")
print rose.todo_list()
print rose.item_list_by_name("Books")
print rose.item_list_by_id(1)








 	