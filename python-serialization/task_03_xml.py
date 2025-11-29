#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries to and from XML files."""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("root")
    
    def build_xml_element(parent, dict_obj):
        for key, value in dict_obj.items():
            elem = ET.SubElement(parent, key)
            if isinstance(value, dict):
                build_xml_element(elem, value)
            else:
                elem.text = str(value)
    
    build_xml_element(root, dictionary)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    def build_dict(element):
        result = {}
        for child in element:
            if len(child):
                result[child.tag] = build_dict(child)
            else:
                result[child.tag] = child.text
        return result
    
    return build_dict(root)
