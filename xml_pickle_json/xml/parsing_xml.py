import xml.etree.ElementTree as ET

xml_data = """
<library>
    <book id="1">
        <title>The lord of the Rings</title>
        <author>J.R.R. Tolkien</author>
        <year>1954</year>
    </book>
    <book id="1">
        <title>The Hobbit</title>
        <author>J.R.R. Tolkien</author>
        <year>1937</year>
    </book>
</library>
"""

# Парсинг из строки
root = ET.fromstring(xml_data)

for book in root.findall('book'):
    book_id = book.get('id')
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")

