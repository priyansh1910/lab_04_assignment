flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

def find_flight_by_id(flight_id):
    for flight in flight_data:
        if flight["Flight ID"] == flight_id:
            return flight
    return None

def find_flights_by_source(source):
    flights = []
    for flight in flight_data:
        if flight["From"] == source:
            flights.append(flight)
    return flights

def find_flights_by_destination(destination):
    flights = []
    for flight in flight_data:
        if flight["To"] == destination:
            flights.append(flight)
    return flights

while True:
    print("Select an option:")
    print("1. Search by Flight ID")
    print("2. Search by Source City")
    print("3. Search by Destination City")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        flight_id = input("Enter Flight ID: ")
        flight = find_flight_by_id(flight_id)
        if flight:
            print("Flight Details:")
            print("Flight ID:", flight["Flight ID"])
            print("From:", flight["From"])
            print("To:", flight["To"])
            print("Price:", flight["Price"])
        else:
            print("Flight not found.")

    elif choice == "2":
        source = input("Enter Source City: ")
        flights = find_flights_by_source(source)
        if flights:
            print("Flights from", source, ":")
            for flight in flights:
                print("Flight ID:", flight["Flight ID"])
                print("To:", flight["To"])
                print("Price:", flight["Price"])
        else:
            print("No flights found from", source)

    elif choice == "3":
        destination = input("Enter Destination City: ")
        flights = find_flights_by_destination(destination)
        if flights:
            print("Flights to", destination, ":")
            for flight in flights:
                print("Flight ID:", flight["Flight ID"])
                print("From:", flight["From"])
                print("Price:", flight["Price"])
        else:
            print("No flights found to", destination)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
