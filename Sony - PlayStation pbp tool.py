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
        tree = ET.parse("Sony - PlayStation.dat")
    except:
        print("Error opening Sony - PlayStation.dat")
        exit(1)
    root = tree.getroot()
    for child in root:
        if child.tag == "header":
            for sub in child:
                if sub.tag == "version":
                    sub.text = sub.text + " Ludo Custom"
                if sub.tag == "author":
                    sub.text = "Ludo PlayStation Customizer"
        if child.tag == "game":
            if "(Disc" in child.attrib["name"]:
                if "(Disc 1)" in child.attrib["name"]:
                    updated_name = child.attrib["name"].replace(" (Disc 1)", "")
                    new_element = ET.SubElement(root, "game")
                    new_element.set("name", updated_name)
                    ET.SubElement(new_element, "category")
                    new_element[0].text = "Games"
                    ET.SubElement(new_element, "description")
                    new_element[1].text = updated_name
                    ET.SubElement(new_element, "rom")
                    new_element[2].set("name", updated_name + ".pbp")
                    # I'll add these two lines back when I figure out how to get ludo detecting m3u files.
                    ET.SubElement(new_element, "rom")
                    new_element[3].set("name", updated_name + ".m3u")
                else:
                    pass
            else:
                if ".pbp" not in child[2].attrib["name"]:
                    original_name = child[2].attrib["name"]
                    updated_name = original_name.split(".")
                    updated_name.pop()
                    updated_name.append("pbp")
                    updated_name = ".".join(updated_name)
                    new_element = ET.Element("rom")
                    new_element.set("name", updated_name)
                    child.insert(2,new_element)
    ET.indent(tree, "\t")
    tree.write("Sony - PlayStation.dat")
    with open("Sony - PlayStation.dat") as file_raw:
        file_dat = file_raw.read()
    file_dat = header + file_dat
    with open("Sony - PlayStation.dat", "w") as file_raw:
        file_raw.write(file_dat)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()