from xml.etree import ElementTree as ET
import os

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

filename = '202415.xml'
base_name, extension = filename.rsplit('.', 1)

tree = ET.parse(filename)
root = tree.getroot()
middle_idx = len(root) // 2

file1_name = f'{base_name}_1.{extension}'
file2_name = f'{base_name}_2.{extension}'

with open(file1_name, 'wb') as file1:
    file1.write(b'<?xml version="1.0" encoding="UTF-8"?>\n<events>\n')
    for event in root[:middle_idx + 1]:
        file1.write(ET.tostring(event, encoding='utf-8').strip())
    file1.write(b'</events>')

with open(file2_name, 'wb') as file2:
    file2.write(b'<?xml version="1.0" encoding="UTF-8"?>\n<events>\n')
    for event in root[middle_idx + 1:]:
        file2.write(ET.tostring(event, encoding='utf-8').strip())
    file2.write(b'</events>')

validate_and_info(file1_name)
validate_and_info(file2_name)
