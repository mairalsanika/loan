def book_flight(flight, passenger, passenger_type, seat_class,
                available_seats, baggage, booking_days):

    
    if passenger == "":
        return "Invalid passenger"


    if available_seats <= 0:
        return "Flight is fully booked"

    
    if seat_class == "Economy":
        fare = 500
    elif seat_class == "Business":
        fare = 1000
    elif seat_class == "First":
        fare = 2000
    else:
        return "Invalid class"

    
    if available_seats <= 5:
        fare += 300

    if booking_days <= 7:
        fare += 200

    
    if passenger_type == "Student":
        fare *= 0.90
    elif passenger_type == "Senior":
        fare *= 0.85
    if baggage <= 15:
        baggage_charge = 0
    else:
        baggage_charge = (baggage - 15) * 20

    total = fare + baggage_charge

    print("--------------------------")
    print("Flight:", flight)
    print("Passenger:", passenger)
    print("Class:", seat_class)
    print("Fare:", fare)
    print("Baggage Charge:", baggage_charge)
    print("Total Fare:", total)
    print("Booking Successful")
    print("--------------------------")

    return total


def cancel_booking(fare):
    refund = fare * 0.80

    print("Booking Cancelled")
    print("Refund:", refund)

    return refund


# Examples - No input required

fare1 = book_flight(
    "AI101", "Rahul", "Student",
    "Economy", 10, 10, 20
)

fare2 = book_flight(
    "AI102", "Priya", "Adult",
    "Business", 4, 20, 5
)

cancel_booking(fare1)