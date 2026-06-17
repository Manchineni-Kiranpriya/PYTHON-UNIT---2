ticket_id = input("Enter Ticket ID: ")
name = input("Enter Passenger Name: ")
status = input("Enter Ticket Status (Booked/Confirmed): ")

if (ticket_id.startswith("TKT") and
    len(ticket_id) == 7 and
    name != "" and
    status in ["Booked", "Confirmed"]):
    print("Valid Ticket")
else:
    print("Invalid Ticket")
