#/usr/bin/bash python3

import operator
from faker import Faker
from random import randint

import pizza_order

fake= Faker()

orders = []              # initialize a list to hold the simulated pizza orders


# Simulate 10 pizza orders
for i in range(10):  
  
    # generate one fake pizza order at a time 
    order = pizza_order.PizzaOrder(        \
        fake.first_name(),       \
        fake.last_name(),      \
        fake.date(),      \
        randint(10,200)   \
    )
    
    orders.append(order)   

# sort the orders by the order amount
orders_sorted  = sorted(orders, key=operator.attrgetter("order_amount"))

for order in orders_sorted:
    print("Order: "     \
          + " " + order.retrieve_customer_name()[0]  \
          + " " + order.retrieve_customer_name()[1]  \
          + " " + str(order.retrieve_order_date())         \
          + " " + str(order.retrieve_order_amount())      \
        )

