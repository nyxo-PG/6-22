total_seats = 40
seats_booked = 0
successful_bookings = 0

while seats_booked < total_seats:
    requested = int(input("Enter seats required (0 to stop): "))
    
    if requested == 0:
        break
        
    remaining = total_seats - seats_booked
    
    if requested > remaining:
        print(f"Rejected! Only {remaining} seats left.\n")
    else:
        seats_booked += requested
        successful_bookings += 1
        print(f"Successful! Remaining seats: {total_seats - seats_booked}\n")

print("\n--- Summary ---")
print(f"Total seats booked: {seats_booked}")
print(f"Remaining seats: {total_seats - seats_booked}")
print(f"Number of successful bookings: {successful_bookings}")