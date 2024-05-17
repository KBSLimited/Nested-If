#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Venue Selection
attendees = int(input("Enter number of attendees: ")) 
venue = "large hall" if attendees > 100 else "conference room"
additional_facilities = []

if attendees > 50:
    additional_facilities.append("audio system")
if attendees > 80:
    additional_facilities.append("projector")

print("Venue:", venue)
if additional_facilities:
    print("Additional facilities recommended:", ", ".join(additional_facilities))

#Task 3: Catering Choices
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
additional_facilities = []

if attendees > 50:
    additional_facilities.append("audio system")
if attendees > 80:
    additional_facilities.append("projector")

print("Venue:", venue)
if additional_facilities:
    print("Additional facilities recommended:", ", ".join(additional_facilities))

vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")

if vegetarian_choice.lower() == "yes":
    print("We recommend Veggie Delight Caterers for vegetarian food.")
else:
    print("We recommend Gourmet Meals Caterers for non-vegetarian food.")
