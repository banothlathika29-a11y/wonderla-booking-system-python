import time
import sys
import os
import random
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# --- Ride and Booking Data ---
rides = {
    "Wonder Splash": {"10:00 AM": 5, "12:00 PM": 5, "2:00 PM": 5, "4:00 PM": 5},
    "Recoil": {"10:00 AM": 5, "12:00 PM": 5, "2:00 PM": 5, "4:00 PM": 5},
    "Maverick": {"10:00 AM": 5, "12:00 PM": 5, "2:00 PM": 5, "4:00 PM": 5},
    "Equinox": {"10:00 AM": 5, "12:00 PM": 5, "2:00 PM": 5, "4:00 PM": 5}
}

bookings = []

# --- Comedy & Life Quotes ---
quotes = [
    "😄 'Life is like a roller coaster — enjoy the ups, scream through the downs!'",
    "🎢 'Don’t take life too seriously, no one gets out alive anyway.'",
    "💡 'Mistakes are proof that you are trying — and maybe not reading the manual.'",
    "😂 'If at first you don’t succeed, ride Recoil again!'",
    "🌞 'Smile today — you paid for this ticket, might as well enjoy the ride!'",
    "🍕 'You can’t buy happiness, but you can buy a Wonderla ticket. Close enough!'",
    "🚀 'Stay weird. Normal is boring — like standing in line instead of riding.'"
]

# --- Fun Facts ---
fun_facts = [
    "🎠 Fun Fact: The longest roller coaster in the world is over 2.4 km long!",
    "🎡 Fun Fact: Recoil is India’s first-ever reverse looping roller coaster!",
    "💦 Fun Fact: Wonder Splash recycles water every 5 minutes for eco-friendliness!",
    "🍿 Fun Fact: The average person screams 4 times on Recoil (minimum)!",
    "🎢 Fun Fact: The speed of Recoil can reach 80 km/h in just 3 seconds!",
]

# --- Helper Functions for Animation ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def loading(message="Loading", duration=1.5, color=Fore.YELLOW):
    slow_print(message, 0.05, color)
    for i in range(3):
        sys.stdout.write(Fore.YELLOW + ".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n" + Style.RESET_ALL)

def random_quote():
    quote = random.choice(quotes)
    slow_print(quote, 0.04, Fore.CYAN)
    print()

def random_fact():
    fact = random.choice(fun_facts)
    slow_print(fact, 0.04, Fore.MAGENTA)
    print()

# --- Core Functions ---
def show_rides():
    clear_screen()
    slow_print("\n🎢 Available Rides:\n", 0.04, Fore.GREEN)
    for i, ride in enumerate(rides.keys(), start=1):
        slow_print(f"{i}. {ride}", 0.03, Fore.WHITE)
    print()
    random_quote()
    random_fact()
    input(Fore.YELLOW + "\nPress Enter to return to menu...")

def show_slots(ride_name):
    clear_screen()
    slow_print(f"\n⏰ Slots for {ride_name}:\n", 0.04, Fore.CYAN)
    for time_slot, seats in rides[ride_name].items():
        color = Fore.GREEN if seats > 0 else Fore.RED
        slow_print(f"  {time_slot} - {seats} slots left", 0.03, color)
    print()

def book_slot():
    clear_screen()
    show_rides()
    try:
        ride_choice = int(input(Fore.YELLOW + "\nEnter ride number to book: ")) - 1
        ride_name = list(rides.keys())[ride_choice]
    except (IndexError, ValueError):
        slow_print("\n❌ Invalid choice. Returning to menu...", 0.03, Fore.RED)
        time.sleep(1)
        return

    show_slots(ride_name)
    slot_time = input(Fore.YELLOW + "Enter slot time (e.g., 10:00 AM): ")

    if slot_time in rides[ride_name] and rides[ride_name][slot_time] > 0:
        name = input(Fore.YELLOW + "Enter your name: ")
        loading("🎡 Processing your booking", 1.5, Fore.YELLOW)
        rides[ride_name][slot_time] -= 1
        bookings.append({"name": name, "ride": ride_name, "time": slot_time})
        slow_print(f"\n✅ Booking confirmed for {name} on {ride_name} at {slot_time}!", 0.03, Fore.GREEN)
        random_quote()
        random_fact()
        time.sleep(2)
    else:
        slow_print("\n❌ Slot not available. Try another time.", 0.03, Fore.RED)
        time.sleep(1)

def cancel_booking():
    clear_screen()
    name = input(Fore.YELLOW + "\nEnter your name to cancel booking: ")
    loading("🧾 Checking records", 1.5, Fore.YELLOW)
    found = False
    for booking in bookings:
        if booking["name"].lower() == name.lower():
            rides[booking["ride"]][booking["time"]] += 1
            bookings.remove(booking)
            found = True
            slow_print(f"🗑️ Booking for {name} canceled successfully.", 0.03, Fore.GREEN)
            random_quote()
            break
    if not found:
        slow_print("❌ No booking found for that name.", 0.03, Fore.RED)
    time.sleep(1.5)

def view_bookings():
    clear_screen()
    if not bookings:
        slow_print("\n📭 No current bookings.", 0.03, Fore.RED)
        random_quote()
        random_fact()
    else:
        slow_print("\n📋 All Bookings:\n", 0.03, Fore.CYAN)
        for b in bookings:
            slow_print(f"  {b['name']} - {b['ride']} at {b['time']}", 0.02, Fore.WHITE)
        print()
        random_quote()
        random_fact()
    input(Fore.YELLOW + "\nPress Enter to return to menu...")

def main():
    clear_screen()
    slow_print(Fore.CYAN + "🎡 Welcome to Wonderla Ride Slot Booking System 🎠", 0.05)
    random_quote()
    random_fact()
    time.sleep(0.5)
    loading("🎉 Initializing Fun Mode", 1.5, Fore.YELLOW)

    while True:
        clear_screen()
        print(Fore.CYAN + "\n--- 🌟 Wonderla Ride Slot Booking System 🌟 ---")
        print(Fore.GREEN + "1. Show available rides")
        print(Fore.GREEN + "2. Book a slot")
        print(Fore.GREEN + "3. Cancel a booking")
        print(Fore.GREEN + "4. View all bookings")
        print(Fore.RED + "5. Exit")

        choice = input(Fore.YELLOW + "\nEnter your choice: ")

        if choice == "1":
            show_rides()
        elif choice == "2":
            book_slot()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            loading("💾 Saving Data and Happiness Levels", 1.5, Fore.YELLOW)
            slow_print("\n👋 Thank you for visiting Wonderla!", 0.04, Fore.GREEN)
            random_quote()
            random_fact()
            break
        else:
            slow_print("❌ Invalid choice. Try again.", 0.03, Fore.RED)
            time.sleep(1)

if __name__ == "__main__":
    main()