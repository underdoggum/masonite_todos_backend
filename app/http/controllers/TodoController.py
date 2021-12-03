""" A TodoController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Todo import Todo


class TodoController(Controller):
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Todo.find(id)

    def index(self):
        return Todo.all()

    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        todo = Todo.create({"subject": subject, "details": details})
        return todo

    def update(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        id = self.request.param("id")
        Todo.where("id", id).update({"subject": subject, "details": details})
        # note: could also use .find() here
        return Todo.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        todo = Todo.where("id", id).get()
        Todo.where("id", id).delete()
        return todo