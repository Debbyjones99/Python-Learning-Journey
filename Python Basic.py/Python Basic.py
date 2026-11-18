# 1.Business question

# An order can only be approved when:
# 1. The product is available.
# 2. The customer has paid or has approved credit.
# 3. The order value is at least ₦50,000.

```python
product_available = True
payment_received = False
credit_approved = True
order_value = 65000

if (product_available and (payment_received or credit_approved)) and (order_value >= 50000):
    print("Order approved")
else:
    print("Order rejected")
```
# 2. A business has the following order approval rules:
# - Product must be available.
# - Customer must have paid.
# - Order value must be at least ₦100,000.
# - Alternatively, a customer with approved credit can proceed without payment, provided the product is available and order value is at least ₦150,000.

product_available = True
payment_received = False
credit_approved = True
order_value = 160000

if (
    (product_available and payment_received and order_value >=100000)
    or
    (credit_approved and product_available and order_value >=150000)):
    print("Order approved")
else:
    print("Order rejected")

# 3. A retail business classifies customers based on their total purchases:
# Total purchases	Customer category
# ₦500,000 and above	Premium
# ₦200,000–₦499,999	Gold
# ₦50,000–₦199,999	Silver
# Below ₦50,000	Regular


total_purchase = 350000

if (total_purchase >=500000):
    print("Premium")
elif (total_purchase >=200000):
    print("Gold")
elif (total_purchase >= 50000 ):
    print("Silver")
else:
    print("Regular")

print(total_purchase)

# still using the example above
# A customer qualifies for free delivery if:
# - They have purchased at least ₦200,000 AND are a loyalty member.
# OR
# - They have purchased at least ₦500,000, regardless of loyalty membership.
# Your tasks
# Question 1. Write an if, elif and else statement to classify the customer.
# Question 2. Write another if/else statement to determine whether the customer qualifies for free delivery. Use the appropriate logical operators.

total_purchase = 350000
loyalty_member = True

if (total_purchase >=500000):
    print("Premium")
elif (total_purchase >=200000):
    print("Gold")
elif (total_purchase >=50000):
    print("Silver")
else:
    print("Regular")
if (
    (total_purchase >=200000 and loyalty_member ==True)
    or
    (total_purchase >=500000 and loyalty_member != True)
):
    print("free delivery")
else:
    print("no free delivery")


# default parameter 

def calculate_total(price, quantity, discount=500):
    total = (price * quantity) - discount
    return total
result1= calculate_total (5000,10)
result2 = calculate_total(5000, 10,2000)
print(result1, result2)

# Create a function called sales_performance that accepts:
# - selling_price
# - purchase_price
# - quantity
# The function should calculate and return:
# - Total revenue.
# - Total purchase cost.
# - Total profit.
# sales_performance(12000, 8000, 30)

def sales_performance(selling_price, purchase_price, quantity):
    total_revenue= selling_price*quantity
    total_purchase_cost= purchase_price*quantity
    total_profit = (selling_price-purchase_price) *quantity
    
    return total_revenue, total_purchase_cost, total_profit
    
total_revenue, total_purchase_cost, total_profit =sales_performance(12000,8000,30)
print(total_revenue)
print(total_purchase_cost)
print(total_profit)











