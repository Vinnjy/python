## Шаблон проектирования - Порождающие - Фабричный

1. import abc:
   * Использовалась модуль для создания абстрактных классов

2. Document:
   * Создавался класс Документ, который является интерфейсом для всех видов документа.
   * В нём прописаны 2 абстрактных метода для открытия и сохранения файла.
```
class Document:
    @abc.abstractmethod
    def open(self):
        pass
    def save(self):
        pass
```
3. TextDocument, ImageDocument, PDFDocument:
   * Cоздавались классы разных видов документов.
   * Все классы наследовались от класса родителя, реализовывали его абстрактные методы.
```
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
```
4. DocumentFactory:
   * Создавлася класс для объявления фабричного метода. Метод является абстрактным.
   * Если его задействовать в классах наследниках DocumentFactory, то можно возвращать объекты типа Document или его наследниках(->).
```
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
```
5. TextDocumentFactory, ImageDocumentFactory, PDFDocumentFactory:
   * Создаются наследники фабрики, в которых задействуем фабричный метод для создания различных видов документа (вызов конструктора) и возвращается свой тип документа.
```
    def create_document(self) -> Document:
        return TextDocument()

class ImageDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return ImageDocument()

class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()
```
Далее реализации клиентского метода: через создателя (DocumentFactory) (не зависит от конкретных создателей (TextDocumentFactory, ...) и конкретных продуктов (TextDocument, ...))
```
def client_code(creator: DocumentFactory):
    print(f"Клиент: Я не знаю, какая это фабрика для открытия файла, но она работает с: {creator.plan_open()}")
    print(f"Клиент: Я не знаю, какая это фабрика для сохранения файла, но она работает с: {creator.plan_save()}")
```
Создания различных фабрик
```
print("Запуск текстовой фабрики для текстовыых документов")
textDocumentFactory = TextDocumentFactory()
client_code(textDocumentFactory)

print("Запуск фабрики изображений для документов с изображениями")
imageDocumentFactory = ImageDocumentFactory()
client_code(imageDocumentFactory)

print("Запуск pdf фабрики для pdf документов")
pdfDocumentFactory = PDFDocumentFactory()
client_code(pdfDocumentFactory)
```
