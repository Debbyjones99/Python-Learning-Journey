# Mini project: Inventory and sales decision system
#Imagine you manage a construction materials business that sells bags of cement.

#You want to create a function called process_sales_order().

#The function should accept four parameters:
#1. selling_price
#2. purchase_price
#3. order_quantity
#4. available_stock
#Business rules
# Your function must follow these rules in this exact order:
# 1. If order_quantity is less than or equal to 0, return "Invalid order quantity".
# 2. If available_stock is 0, return "Stock unavailable".
# 3. If order_quantity is greater than available_stock, return "Insufficient stock".
# 4. Otherwise, calculate and return:
   # - Total revenue
   # - Total purchase cost
   # - Total profit
# test function with tis value 
# process_sales_order(12000, 9000, 10, 50)

def process_sales_order(selling_price, purchase_price, order_quantity, available_stock):

    if order_quantity <= 0:
        return "Invalid order quantity"

    elif available_stock == 0:
        return "Stock unavailable"

    elif order_quantity > available_stock:
        return "Insufficient stock"

    else:
        total_revenue = selling_price * order_quantity
        total_purchase_cost = purchase_price * order_quantity
        total_profit = (selling_price - purchase_price) * order_quantity

        return total_revenue, total_purchase_cost, total_profit


result = process_sales_order(12000, 9000, 10, 50)
print(result)
