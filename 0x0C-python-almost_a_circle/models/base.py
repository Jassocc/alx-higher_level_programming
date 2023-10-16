#!/usr/bin/python3
"""
Classs known as base with different
Attributes and a class constructor
"""
import csv
import json
"""import turtle"""


class Base:
    """
    class definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initiaizer of class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string to rep of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes he json string rep to a file
        """
        filename = cls.__name__ + ".json"
        obj_dict = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dict.append(obj.to_dictionary())
        with open(filename, mode='w', encoding='UTF-8') as file:
            file.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of json string rep
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns attribuets already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                cont = file.read()
                dict_list = cls.from_json_string(cont)
                inst = [cls.create(**d) for d in dict_list]
                return inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        csv serializer
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        deserialize a csv file
        """
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = {"id": int(row[0]), "width": int(row[1]),
                           "height": int(row[2]), "x": int(row[3]),
                           "y": int(row[4])}
                elif cls.__name__ == "Square":
                    obj = {"id": int(row[0]), "size": int(row[1]),
                           "x": int(row[2]), "y": int(row[3])}
                dc = cls.create(**obj)
                objs.append(dc)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws rectangles and squares
        """
        screen = turtle.Screen()
        screen.bgcolor("lightblue")
        screen.title("Shapes Drawer")

        pen = turtle.Turtle()
        pen.pensize(3)
        pen.speed(2)

        for rect in list_rectangle:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for b in range(4):
                pen.forward(square.size)
                pen.left(90)
        turtle.done()
