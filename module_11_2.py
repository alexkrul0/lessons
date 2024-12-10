import inspect
from inspect import ismethod


def introspection_info(obj):
    methods = dir(obj)
    type_ = type(obj)
    module = inspect.getmodule(obj)

    print(f'Тип объекта: {type_}, \nатрибуты объекта: {obj}, \nметоды объекта: {methods}, \n'
          f'модуль объекта: {module}, \nадрес объекта: {id(obj)}\n\n')


introspection_info(int)
introspection_info(42)
introspection_info(inspect)
