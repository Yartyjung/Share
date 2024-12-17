def update_shopping_cart(cart, action):

    product_id = action.get("product_id")

    if action["type"] == "add":
        if product_id not in cart:
            cart[product_id] = action["quantity"]
            return cart
        else:
            cart[product_id] += action["quantity"]
            return cart
    
    elif action["type"] == "remove":
        if product_id not in cart : return "this Product is not in your Cart"
        else : del cart[product_id]
        return cart
    
    elif action["type"] == "change" :  
        if product_id  in cart:
            cart.update({product_id : action["quantity"]})
            return cart  
        elif product_id not in cart : return "this Product is not in your Cart"
    

# do not modify the values below
# print(update_shopping_cart({ "product_A": 4, "product_B": 3, "product_C": 1 }, { "type": "change", "product_id": "product_B", "quantity": 2 }))
print(update_shopping_cart({ "product_A": 4, "product_B": 3, "product_C": 1 }, { "type": "change", "product_id": "product_D", "quantity": 2 }))