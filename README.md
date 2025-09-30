## Задание

Разработайте систему обработки заказов, где к базовому заказу можно применять
различные скидки, а расчет скидки может быть выполнен разными алгоритмами.

1. Декоратор для скидок:
    * Создайте базовый класс Order (Компонент) с методами get_total_cost() и get_description().
    * Реализуйте BasicOrder (Конкретный Компонент).
    * Создайте базовый класс OrderDiscountDecorator (Декоратор) и несколько конкретных декораторов скидок, например:
        * PercentageDiscount (скидка в процентах)
        * FixedAmountDiscount (фиксированная сумма скидки)
        * LoyaltyDiscount (скидка для лояльных клиентов)
Каждый декоратор должен изменять get_total_cost() и get_description().

2. Стратегия для расчета:
    * Создайте интерфейс DeliveryCostStrategy (Стратегия) с методом calculate_cost(distance: float, weight: float).
    * Реализуйте несколько конкретных стратегий:
    * StandardDelivery (стандартная стоимость)
    * ExpressDelivery (экспресс-получение, дороже)
    * FreeDeliveryThreshold (бесплатное получение при определенной сумме заказа, если это применимо к контексту)
    * Добавьте в BasicOrder (или в отдельный класс OrderProcessor ) ссылку на
    * DeliveryCostStrategy и метод для расчета стоимости получения.

3. Интеграция: Продемонстрируйте создание заказа, применение к нему нескольких скидок и расчет стоимости получения с использованием разных стратегий.

## Реализация
1. abc
   * Использовалcя модуль для создания абстрактных классов
```
import abc
```
2. Order (Компонент)
```
class Order(abc.ABC):
    @abc.abstractmethod
    def get_total_cost(self) -> float:
        pass
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
```
2. Order (конкретный компонент)
```
class BasicOrder(Order):
    def get_total_cost(self) -> str:
        return 788778.78
    def get_description(self):
        return "покупка сервера"
```
3. OrderDiscountDecorator - декоратор
```
class OrderDiscountDecorator(Order, abc.ABC):
    def __init__(self, decorated_order: Order):
        self._decorated_order = decorated_order
    @abc.abstractmethod
    def get_total_cost(self) -> float:
        pass
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
```
4. PercentageDiscount, FixedAmountDiscount, LoyaltyDiscount - конкретные декораторы
```
class PercentageDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        return self._decorated_order.get_total_cost() + self._decorated_order.get_total_cost()*0.05

    def get_description(self) -> str:
        return self._decorated_order.get_description() + ", применена скидка 5%"

class FixedAmountDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        return self._decorated_order.get_total_cost() + self._decorated_order.get_total_cost()*0.1

    def get_description(self) -> str:
        return self._decorated_order.get_description() + ", применяем фиксированную скидку"

class LoyaltyDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        return self._decorated_order.get_total_cost() + self._decorated_order.get_total_cost()*0.15
    def get_description(self) -> str:
        return self._decorated_order.get_description() + ", применяем скидку для лояльных клиентов"
```
5. Стратегия
```
class DeliveryCostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self, distance : int, weight : int):
        pass
```
6. Конкретные стратегии
```
class StandardDelivery(DeliveryCostStrategy):
    def __init__(self):
        self.standard = "Стандартно: "
    def calculate_cost(self, distance : int, weight : int):
        print(f"{self.standard}{self.distance * self.weight}")

class ExpressDelivery(DeliveryCostStrategy):
    def __init__(self):
        self.express = "Экспресс: "
    def calculate_cost(self, distance : float, weight : float):
        print(f"{self.express}{self.distance * self.weight * 10}")

class FreeDeliveryThreshold(DeliveryCostStrategy):
    def __init__(self):
        self.free = "Бесплатно: "
    def calculate_cost(self, distance : float, weight : float):
        print(f"{self.free}{0}")
```
7. Контекст
```
class OrderProcessor:
    def __init__(self, basicOrder : BasicOrder):
        self.basicOrder = basicOrder
        self._strategy = None
        self.distance = 0.0
        self.weight = 0.0
    def set_strategy(self, strategy: DeliveryCostStrategy, distance: float, weight: float):
        self._strategy = strategy
        self.distance = distance
        self.weight = weight
        print(f"Установлен способ получения: {strategy.__class__.__name__}")
    def checkout(self):
        if not self._strategy:
            print("Ошибка: Способ получения не выбран.")
            return
        self._strategy.calculate_cost(self.distance, self.weight)
```
8. Клиентская релизация:
```
server = BasicOrder()
print(f"Заказ: стоимость = {server.get_total_cost()}, описание - {server.get_description()}")

server_with_percent_discount = PercentageDiscount(BasicOrder())
print(f"Заказ: стоимость {server_with_percent_discount.get_total_cost()}, описание - {server_with_percent_discount.get_description()}")

server_with_percent_fixed_discount = FixedAmountDiscount(PercentageDiscount(BasicOrder()))
print(f"Заказ: стоимость {server_with_percent_fixed_discount.get_total_cost()}, описание - {server_with_percent_fixed_discount.get_description()}")

server_with_percent_fixed_loyal_discount = LoyaltyDiscount(FixedAmountDiscount(PercentageDiscount(BasicOrder())))
print(f"Заказ: стоимость {server_with_percent_fixed_loyal_discount.get_total_cost()}, описание - {server_with_percent_fixed_loyal_discount.get_description()}")

orderServer = OrderProcessor(server)
if orderServer.basicOrder.get_total_cost() > 100000.0:
    orderServer.set_strategy(FreeDeliveryThreshold(),100, 5)
    orderServer.checkout()
else:
    orderServer.set_strategy(StandardDelivery(), 100, 5)
    orderServer.checkout()
    orderServer.set_strategy(ExpressDelivery(), 100, 5)
    orderServer.checkout()
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a444643-f674-48d3-a593-bb71a0debc9f" />

<img width="1266" height="203" alt="image" src="https://github.com/user-attachments/assets/37c93da7-1d6c-4d94-8791-321ce5ca295e" />


