import abc

class Document:
    @abc.abstractmethod
    def open(self):
        pass
    def save(self):
        pass

class TextDocument(Document):
    def open(self):
        return "Открывает текстовый документ"
    def save(self):
        return "Сохраняет текстовый документ"

class ImageDocument(Document):
    def open(self):
        return "Открывает документ изображений"
    def save(self):
        return "Сохраняет документ изображений"

class PDFDocument(Document):
    def open(self):
        return "Открывает pdf документ"
    def save(self):
        return "Сохраняет pdf документ"

class DocumentFactory(abc.ABC):
    def plan_open(self):
        document = self.create_document()
        result = f"с поиском документа:  {document.open()}."
        return result
    def plan_save(self):
        document = self.create_document()
        result = f"с закрываем документа: {document.save()}."
        return result
    @abc.abstractmethod
    def create_document(self) -> Document:
        pass

class TextDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return TextDocument()

class ImageDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return ImageDocument()

class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()


def client_code(creator: DocumentFactory):
    print(f"Клиент: Я не знаю, какая это фабрика для открытия файла, но она работает с: {creator.plan_open()}")
    print(f"Клиент: Я не знаю, какая это фабрика для сохранения файла, но она работает с: {creator.plan_save()}")

print("Запуск текстовой фабрики для текстовыых документов")
textDocumentFactory = TextDocumentFactory()
client_code(textDocumentFactory)

print("Запуск фабрики изображений для документов с изображениями")
imageDocumentFactory = ImageDocumentFactory()
client_code(imageDocumentFactory)

print("Запуск pdf фабрики для pdf документов")
pdfDocumentFactory = PDFDocumentFactory()
client_code(pdfDocumentFactory)

