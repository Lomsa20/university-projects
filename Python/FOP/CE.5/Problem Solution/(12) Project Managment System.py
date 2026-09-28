class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
class Manager(Person):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f'Manager: {self.name}'
class Developer(Person):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f'Developer: {self.name}'
class Task:
    def __init__(self, title):
        self._title = title
        self._assigned_to = None
    @property
    def title(self):
        return self._title
    def __str__(self):
        assigned = self._assigned_to._name if self._assigned_to else "Unassigned"
        return f'Task: {self._title} assigned to {assigned}'
class Project:
    def __init__(self,name,manager):
        self._name = name
        self._manager = manager
        self._tasks = []
    @property
    def tasks(self):
        return self._tasks
    @property
    def manager(self):
        return self._manager
    @property
    def name(self):
        return self._name
    def add_task(self, task):
        self._tasks.append(task)
    def __str__(self):
        tasks_str = '\n '.join(str(t) for t in self._tasks)
        return f'Project: {self._name}\nManager: {self._manager}\nTasks: {tasks_str}'
m = Manager("Alice")
d1 = Developer("Bob")
d2 = Developer("Charlie")

t1 = Task("Design system")
t2 = Task("Implement backend")
t3 = Task("Write tests")

t1._assigned_to = d1
t2._assigned_to = d2

project = Project("Website", m)
project.add_task(t1)
project.add_task(t2)
project.add_task(t3)

print(project)