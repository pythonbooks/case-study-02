#!/usr/bin/bash python3

class PizzaOrder:

    def __init__(self, first_name, last_name, order_date, order_amount):
        self.first_name = first_name
        self.last_name =last_name
        self.order_date = order_date
        self.order_amount = order_amount


    def store_customer_Name(first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def retrieve_customer_name(self):
        return (self.first_name, self.last_name)

    def store_order_date(order_date):
        self.order_date = order_date

    def retrieve_order_date(self):
        return self.order_date

    def store_order_amount(order_amount):
        self.order_amount = order_amount

    def retrieve_order_amount(self):
        return self.order_amount
