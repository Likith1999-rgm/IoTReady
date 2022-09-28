import json
from json2html import *
from jinja2 import Environment, FileSystemLoader
import webbrowser

with open("d.json", "r") as d:
    data = json.load(d)

fileLoader = FileSystemLoader("templates")
env = Environment(loader=fileLoader)

input = data
json2html.convert(json = input)

webbrowser.open_new_tab('d.html')
