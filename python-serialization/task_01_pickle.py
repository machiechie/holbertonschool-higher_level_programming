#!/usr/bin/python3
"""A module that defines a custom class with serialization and deserialization methods using pickle."""

import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            # Если возникла ошибка при сохранении
            return None

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError):
            # Возвращаем None, если файл не существует, повреждён или пустой
            return None

