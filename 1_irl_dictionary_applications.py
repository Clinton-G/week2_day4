#   Task 1:

#   new key      #dictionary[new_key] = new_value
#   update key   #dictionary[existing_key] = new_value

#   Original Menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
#   Adding Beverages
restaurant_menu['Beverages'] = 'Coke: 2.99', 'Sprite: 2.99'
#   Changing 'Steak' from 15.99 - 17.99
restaurant_menu['Main Course'] = {"Steak": 17.99, "Salmon": 13.99}
#   Remvoing 'Bruschetta' from 'Starters'
restaurant_menu['Starters'] = {"Soup":5.99}

print(restaurant_menu)





