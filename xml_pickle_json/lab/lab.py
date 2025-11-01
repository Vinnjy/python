import csv
import xml.etree.ElementTree as ET

try:
    with open("students.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        root = ET.Element("students")
        for i, row in enumerate(reader):
            alex = ET.SubElement(root, "student", id=f"{i + 1}")
            ET.SubElement(alex, "id").text = row["id"]
            ET.SubElement(alex, "name").text = row["name"]
            ET.SubElement(alex, "major").text = row["major"]
        tree = ET.ElementTree(root)
        tree.write("students.xml", encoding="utf-8", xml_declaration=True)
except FileNotFoundError:
    print("Добавьте файл для считывания")
