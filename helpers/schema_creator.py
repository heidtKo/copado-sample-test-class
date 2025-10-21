import os
import re
import xml.etree.ElementTree as ET
import json

def extract_api_name(filename):
    return re.sub(r'\..*-meta\.xml$', '', filename)

def extract_references(xml_file):
    references = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag == '{http://soap.sforce.com/2006/04/metadata}referenceTo':
                references.append(elem.text)
    except ET.ParseError:
        pass  # Ignore parsing errors
    return references

def parse_sfdx_objects(base_path):
    sfdx_data = {"objects": []}
    objects_path = os.path.join(base_path, "objects")
    
    if not os.path.exists(objects_path):
        print("Objects folder not found.")
        return sfdx_data
    
    for obj_folder in os.listdir(objects_path):
        obj_path = os.path.join(objects_path, obj_folder)
        if os.path.isdir(obj_path):
            obj_data = {"API Name": obj_folder, "fields": [], "validationRules": [], "listViews": [], "references": {}}
            
            for sub_folder in os.listdir(obj_path):
                sub_path = os.path.join(obj_path, sub_folder)
                
                if os.path.isdir(sub_path):
                    for file in os.listdir(sub_path):
                        if file.endswith("-meta.xml"):
                            api_name = extract_api_name(file)
                            
                            if sub_folder == "fields":
                                obj_data["fields"].append(api_name)
                                ref_path = os.path.join(sub_path, file)
                                references = extract_references(ref_path)
                                if references:
                                    obj_data["references"][api_name] = references
                            elif sub_folder == "validationRules":
                                obj_data["validationRules"].append(api_name)
                            elif sub_folder == "listViews":
                                obj_data["listViews"].append(api_name)
                
            sfdx_data["objects"].append(obj_data)
    
    return sfdx_data

if __name__ == "__main__":
    base_directory = "force-app/main/default"  # Adjust this to your actual project path
    result = parse_sfdx_objects(base_directory)
    with open("copado_object_schema.json", "w") as outfile:
        json.dump(result, outfile, indent=4)
