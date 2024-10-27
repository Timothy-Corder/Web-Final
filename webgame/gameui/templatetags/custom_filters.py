
from django import template

register = template.Library()

def get_item(dictionary, key):
    return dictionary.get(key)
register.filter('get_item', get_item)

def title(string:str):
    return string.title()
register.filter('title', title)

def concat(string1:str,string2:str): return str(string1) + str(string2)
register.filter('concat', concat)

def includes(string:str,substring:str): return (substring in string)
register.filter('includes',includes)