import xml.etree.ElementTree as ET
from lxml import etree

# Создание корневого элемента
root = ET.Element("library")

# Создание дочерних элементов
book1 = ET.SubElement(root, "book", id="3")
ET.SubElement(book1, "title").text = "Dune"
ET.SubElement(book1, "author").text = "Frank Herbert"
ET.SubElement(book1, "year").text = "1965"

book2 = ET.SubElement(root, "book", id="4")
ET.SubElement(book2,"title").text = "Foundation"
ET.SubElement(book2, "author").text = "Isaac Asimov"
ET.SubElement(book2, "year").text = "1951"

# Преобразование в строку
xml_string = ET.tostring(root, encoding='unicode')
print(xml_string)

# Сохранение в файл
tree = ET.ElementTree(root)
tree.write("library.xml", encoding="utf-8", xml_declaration=True)