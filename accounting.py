
def melons_count(orders_by_type):
    """Returns count of melons by melon type."""

    count = {"Musk": 0,
            "Hybrid": 0,
            "Watermelon": 0,
            "Winter": 0}
    
    orders = open('orders-by-type.txt')

    for order in orders:

        data = order.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        count[melon_type] = count[melon_type] + melon_count

    orders.close()

    return count

def revenue(count): 
    """Return revenue from total melon sales."""

    MELON_PRICES = {"Musk": 1.15,
                    "Hybrid": 1.30,
                    "Watermelon": 1.75,
                    "Winter": 4.00}

    total_revenue = 0

    print('TOTAL REVENUE')

    for melon_type in count:
        price = MELON_PRICES[melon_type]
        melon_revenue = price * count[melon_type]
        total_revenue = total_revenue + melon_revenue

        print(f"We sold {count[melon_type]:,} {melon_type} melons for ${price:.2f} each. Total revenue from {melon_type} melons was ${melon_revenue:,.2f}")

    return total_revenue


def sales_comparison(ordes_with_sales):
    """Compares online sales VS salesperson generated sales."""

    orders = open('orders-with-sales.txt')

    online_sales = 0
    salesperson_sales = 0

    for order in orders:
        data = order.split("|")

        if data[2] == "ONLINE":
            online_sales = online_sales + float(data[3])

        else:
            salesperson_sales = salesperson_sales + float(data[3])
        
    print("SALES DATA")
    print(f"Salespeole made ${salesperson_sales:,.2f} in revenue.")
    print(f"Online sales made ${online_sales:,.2f} in revenue.")

    if salesperson_sales > online_sales:
        print("Sales people made more revenue than online sales.")
    
    else:
        print("Online sales made more revenue than salespoeple.")

    orders.close()


melon_tallies = melons_count('orders-by-type.txt')

revenue(melon_tallies)

print()

sales_comparison('orders-with-sales.txt')




