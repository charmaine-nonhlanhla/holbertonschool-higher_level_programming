import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to the given filename.
    
    :param dictionary: A Python dictionary to be serialized
    :param filename: The filename of the output XML file
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Serialization error: {e}")

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename into a Python dictionary.
    
    :param filename: The filename of the input XML file
    :return: A Python dictionary with the deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None

# Sample Test
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    if deserialized_data:
        print("\nDeserialized Data:")
        print(deserialized_data)
    else:
        print("Failed to deserialize the XML data.")

