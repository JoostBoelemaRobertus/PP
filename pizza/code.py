class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name
    

    #The repr function will define what we return when we call the class such as:
        #Topping("Cheese", 1) -> "Cheese"

    def __repr__(self):
        return self.name



class Pizza:
    base_price = 2
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def price(self):
        topping_price = 0
        for t in self.toppings:
            topping_price += t.price
        return Pizza.base_price  + topping_price

    def __str__(self):
        return "Pizza " + self.name + " with: " + str(self.toppings)
    

p = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)])
print(p)
print(p.price())
print(p.toppings)


class Order:

    def __init__(self, pizzas, address, message = ''):

        self.pizzas = pizzas 
        self.address = address
        self.message = message

    def price(self):
        current_price = 0
        for pizza in self.pizzas:
            current_price += pizza.price()
        if current_price < 10:
            current_price += 3
        return current_price

    def delivery(self):
        
        order_price = self.price()
        print(f'{self.message} Delivering {len(self.pizzas)} pizzas for {order_price} euros to {self.address}.')

    

p = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)])
p2 = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)])
p3 = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)]) 

order = Order([p, p2, p3], 'Some German street 91', 'Hello mister pizza man!')
order.delivery()