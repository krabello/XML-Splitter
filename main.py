import os, sys
from xml.etree import ElementTree as ET

def split_file(filename):
    base_name, extension = filename.rsplit('.', 1)
    tree = ET.parse(filename)
    root = tree.getroot()
    middle_idx = len(root) // 2

    write_file(f'{base_name}_1.{extension}', root[:middle_idx + 1])
    write_file(f'{base_name}_2.{extension}', root[middle_idx + 1:])

def write_file(filename, elements):
    with open(filename, 'wb') as file:
        file.write(b'<?xml version="1.0" encoding="UTF-8"?><events>')
        for element in elements:
            file.write(ET.tostring(element, encoding='utf-8').strip())
        file.write(b'</events>')
    
    validate_and_info(filename)

def validate_and_info(file_name):
    try:
        tree = ET.parse(file_name)
        print(f"{file_name} is a valid XML file.")
        events_count = len(tree.findall('.//event'))
        print(f"Number of events in {file_name}: {events_count}")
        file_size_MB = os.path.getsize(file_name) / (1024 * 1024)
        print(f"File size of {file_name}: {file_size_MB:.2f} MB\n")
    except ET.ParseError:
        print(f"{file_name} is not a valid XML file.")

if __name__ == "__main__":
    filename = sys.argv[1]
    split_file(filename)
