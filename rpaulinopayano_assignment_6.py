# rpaulinopayano_assignment_6.py 
# Student: Rayner Paulino-Payano
# Assignment 6: Contact Information Formatter 
# Demonstrates mastery of string methods for data cleaning and formatting
print("enter contact information (format: name|phone|email|address): ")

cleaned_contacts_list = []
contact_count = 0

# loop to take multiple inputs
while True:
    user_input = input().strip()
    
    # check for stopping condition
    if not user_input or user_input.upper() == "DONE":
        break
    
    # check for correct field count
    if user_input.count("|") == 3:
        contact_count += 1
        separated_contact_info = user_input.split("|")

        # name cleaning
        name_full = separated_contact_info[0].strip().title()
        name_parts = name_full.split()
        
        # separate first and last name
        if len(name_parts) >= 2:
            # combine all words except the last into the first name
            first_name = " ".join(name_parts[:-1]) 
            # the last word is the last name
            last_name = name_parts[-1]
        else:
            first_name = name_parts[0] if name_parts else "n/a"
            last_name = "n/a"

        # address cleaning
        raw_address = separated_contact_info[3].strip()
        # use title and split
        separated_address = raw_address.title().split()
        final_address = []
        
        # smart state abbreviation handling
        for part in separated_address:
            # check length is 2 and is alpha then use upper
            if len(part) == 2 and part.isalpha():
                final_address.append(part.upper())
            else:
                final_address.append(part)
        # reassemble address using join
        address = " ".join(final_address)

# start printing output sections
if cleaned_contacts_list:
    
    # contact directory section
    print("\n=== CONTACT DIRECTORY ===")
    
    for contact in cleaned_contacts_list:
        print(f"\nCONTACT {contact['count']}:")
        print(f"Name:     {contact['full_name']}")
        print(f"Phone:    {contact['phone']}")
        print(f"Email:    {contact['email']}")
        print(f"Address:  {contact['address']}")

    # directory summary section
    print("\n=== DIRECTORY SUMMARY ===")
    print(f"total contacts processed: {contact_count}")

    # formatted for printing section with alignment
    print("\n=== FORMATTED FOR PRINTING ===")
    
    for contact in cleaned_contacts_list:
        # format name as last first
        directory_name = f"{contact['last_name']}, {contact['first_name']}"
        # use f-string alignment
        print(f"{directory_name:<30}{contact['phone']:<20}{contact['email']}")

# case for no contacts entered
else:
    print("\n=== CONTACT DIRECTORY ===")
    print("\n=== DIRECTORY SUMMARY ===")
    print("total contacts processed: 0")
    print("\n=== FORMATTED FOR PRINTING ===")