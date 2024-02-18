#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Stephen Ancona"
__version__ = "0.1.0"
__license__ = "MIT"


import xml.etree.ElementTree as ET

header = '<?xml version="1.0"?>\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">\n'


def main():
    """ Main entry point of the app """
    try:
        tree = ET.parse("Nintendo - Nintendo 64.dat")
    except:
        print("Error opening Nintendo - Nintendo 64.dat")
        exit(1)
    root = tree.getroot()
    for child in root:
        if child.tag == "header":
            for sub in child:
                if sub.tag == "version":
                    sub.text = sub.text + " Ludo Custom"
                if sub.tag == "author":
                    sub.text = "Ludo Nintendo 64 Customizer"
        if child.tag == "game":
            children = []
            for tag in child:
                if tag.tag == "rom":
                    children.append(tag.attrib["name"])
            combo = "\t".join(children)
            if ".n64" not in combo:
                original_name = children[0]
                updated_name = original_name.split(".")
                updated_name.pop()
                updated_name.append("n64")
                updated_name = ".".join(updated_name)
                new_element = ET.Element("rom")
                new_element.set("name", updated_name)
                child.insert(1,new_element)
            if ".z64" not in combo:
                original_name = children[0]
                updated_name = original_name.split(".")
                updated_name.pop()
                updated_name.append("z64")
                updated_name = ".".join(updated_name)
                new_element = ET.Element("rom")
                new_element.set("name", updated_name)
                child.insert(1,new_element)
    ET.indent(tree, "\t")
    tree.write("Nintendo - Nintendo 64.dat")
    with open("Nintendo - Nintendo 64.dat") as file_raw:
        file_dat = file_raw.read()
    file_dat = header + file_dat
    with open("Nintendo - Nintendo 64.dat", "w") as file_raw:
        file_raw.write(file_dat)


def main2():
    """ Main entry point of the app """
    try:
        tree = ET.parse("Nintendo - Nintendo 64.dat")
    except:
        print("Error opening Nintendo - Nintendo 64.dat")
        exit(1)
    root = tree.getroot()
    for child in root:
        if child.tag == "header":
            for sub in child:
                if sub.tag == "version":
                    sub.text = sub.text + " Ludo Custom"
                if sub.tag == "author":
                    sub.text = "Ludo Nintendo 64 Customizer"
        if child.tag == "game":
            if ".n64" not in child[2].attrib["name"]:
                original_name = child[2].attrib["name"]
                updated_name = original_name.split(".")
                updated_name.pop()
                updated_name.append("n64")
                updated_name = ".".join(updated_name)
                new_element = ET.Element("rom")
                new_element.set("name", updated_name)
                child.insert(2,new_element)
    ET.indent(tree, "\t")
    tree.write("Nintendo - Nintendo 64.dat")
    with open("Nintendo - Nintendo 64.dat") as file_raw:
        file_dat = file_raw.read()
    file_dat = header + file_dat
    with open("Nintendo - Nintendo 64.dat", "w") as file_raw:
        file_raw.write(file_dat)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()