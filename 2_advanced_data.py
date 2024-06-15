hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print('Room', room_number, 'booked by', customer_name)
        else:
            print('Room', room_number, 'Is Unavailable')
    else:
        print('Room', room_number, 'Does Not Exist')

def checkout_customer(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(customer_name, 'Has Checked Out of Room', room_number)
        else:
            print('No Customer in Room', room_number)
    else:
        print('Room', room_number, 'Does Not Exist.')

def display_room_status():
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        status = details["status"]
        customer = details["customer"]
        if status == "available":
            print('Room', room_number, 'is available')
        else:
            print('Room', room_number, 'was booked by', customer)

while True:
    print('''
1. Book a Room
2. Display Room Status
3. Exit
    ''')
    
    choice = input("Enter Choice: ")
    
    if choice == '1':
        display_room_status()
        room_number = input("Enter Room Number: ")
        customer_name = input("Enter Customer Name: ")
        book_room(room_number, customer_name)

    elif choice == '2':
        display_room_status()
    
    elif choice == '3':
        print("Have a Good Day.")
        break

    else:
        print("Invalid Input, Try Again.")
