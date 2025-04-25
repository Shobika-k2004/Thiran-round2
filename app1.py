# Sample Warehouse Inventory
warehouse_inventory = {
    'P101': 10,
    'P102': 5,
    'P103': 20,
    'P104': 0
    
}
#Sales Orders (Order ID, Product ID, Quantity)
sales_orders = [
    ('SO01', 'P101', 3),
    ('SO02', 'P102', 2),
    ('SO03', 'P103', 7),
    ('SO04', 'P104', 4)
    
]
# List to store failed orders
failed_orders = []
# Process each sales order
for order_id, product_id, quantity in sales_orders:
    if product_id in warehouse_inventory and warehouse_inventory[product_id] >= quantity:
        warehouse_inventory[product_id] -= quantity
        print(f"Order Processed: {order_id}")
    else:
        reason = "Insufficient stock" if product_id in warehouse_inventory else "Product ID not found"
        failed_orders.append((order_id, product_id, quantity, reason))
        print(f"Order Failed: {order_id} - {reason}")

print("\nUpdated Inventory:")
for product_id, remaining_qty in warehouse_inventory.items():
    print(f"{product_id}: {remaining_qty}")

# Display all failed orders
print("\nFailed Orders:")
for order in failed_orders:
    print(f"Order ID: {order[0]}, Product ID: {order[1]}, Quantity: {order[2]}, Reason: {order[3]}")


