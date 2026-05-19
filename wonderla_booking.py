rides = {
    "Wonder Splash": {
        "10:00 AM": 5,
        "12:00 PM": 5,
        "2:00 PM": 5,
        "4:00 PM": 5
    },

    "Recoil": {
        "10:00 AM": 5,
        "12:00 PM": 5,
        "2:00 PM": 5,
        "4:00 PM": 5
    },

    "Maverick": {
        "10:00 AM": 5,
        "12:00 PM": 5,
        "2:00 PM": 5,
        "4:00 PM": 5
    },

    "Equinox": {
        "10:00 AM": 5,
        "12:00 PM": 5,
        "2:00 PM": 5,
        "4:00 PM": 5
    }
}

bookings = []


def show_rides():
    print("\nAvailable Rides:")

    for i, ride in enumerate(rides.keys(), start=1):
        print(f"{i}. {ride}")


def show_slots(ride_name):
    print(f"\nSlots for {ride_name}:")

    for time_slot, seats in rides[ride_name].items():
        print(f"{time_slot} - {seats} seats left")


def book_slot():
    show_rides()

    try:
        ride_choice = int(input("\nEnter ride number to book: "))
        ride_name = list(rides.keys())[ride_choice - 1]

    except:
        print("Invalid ride choice.")
        return

    show_slots(ride_name)

    slot_time = input(
        "Enter slot time exactly (Example: 10:00 AM): "
    )

    if slot_time in rides[ride_name] and rides[ride_name][slot_time] > 0:

        name = input("Enter your name: ")

        rides[ride_name][slot_time] -= 1

        bookings.append({
            "name": name,
            "ride": ride_name,
            "time": slot_time
        })

        print(f"\nBooking confirmed for {name} on {ride_name} at {slot_time}.")

    else:
        print("Slot not available.")


def cancel_booking():
    name = input("\nEnter your name to cancel booking: ")

    for booking in bookings:

        if booking["name"].lower() == name.lower():

            rides[booking["ride"]][booking["time"]] += 1

            bookings.remove(booking)

            print("Booking cancelled successfully.")
            return

    print("No booking found.")


def view_bookings():

    if not bookings:
        print("\nNo current bookings.")

    else:
        print("\nAll Bookings:")

        for b in bookings:
            print(f"{b['name']} - {b['ride']} at {b['time']}")


def main():

    while True:

        print("\n--- Wonderla Ride Slot Booking System ---")

        print("1. Show available rides")
        print("2. Book a slot")
        print("3. Cancel a booking")
        print("4. View all bookings")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_rides()

        elif choice == "2":
            book_slot()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            print("\nThank you for visiting Wonderla!")
            break

        else:
            print("Invalid choice. Try again.")


main()