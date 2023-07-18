#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    knowledge = []
    
    def learn(self, new_knowledge=""):
        if type(new_knowledge) == str:
            self.knowledge.append(new_knowledge)
        