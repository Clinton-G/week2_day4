ticket_submit = input("Would you like to open a new ticket? ")


service_tickets = {
"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
"Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


while ticket_submit != 'no':
    new_tik_number = input("Ticket Number: ")
    new_tik_name = input("Customer: ")
    new_tik_issue = input("Issue: ")
    new_tik_status = input("Status: ")
    service_tickets[new_tik_number] = {new_tik_name, new_tik_issue, new_tik_status}
    print(service_tickets)
    ticket_submit = input("Would you like to open another ticket? ")
    if ticket_submit == "no":
        ticket_status = input("Would you like to update the status of any of the tickets? ")
        while ticket_status != "no":
            ticket_status = input("Which ticket status would you like to change? ")
            pass
        #Cant figure out how to change status
print(service_tickets)

