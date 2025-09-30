import abc

class Order(abc.ABC):
    @abc.abstractmethod
    def get_total_cost(self) -> float:
        pass
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
class BasicOrder(Order):
    def get_total_cost(self) -> str:
        return 788778.78
    def get_description(self):
        return "покупка сервера"

class OrderDiscountDecorator(Order, abc.ABC):
    def __init__(self, decorated_order: Order):
        self._decorated_order = decorated_order
    @abc.abstractmethod
    def get_total_cost(self) -> float:
        pass
    @abc.abstractmethod
    def get_description(self) -> str:
        pass

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

class DeliveryCostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self, distance : int, weight : int):
        pass

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