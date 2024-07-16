def remove_duplicates_and_display_unique(customer_ids):
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def print_unique_customer_ids(unique_customer_ids):
    print("Unique Customer IDs:", unique_customer_ids)

unique_customer_ids = remove_duplicates_and_display_unique(customer_ids)
print_unique_customer_ids(unique_customer_ids)

while True:
    add_more = input("\nDo you want to add another customer ID? (yes/no): ").lower()
    if add_more != 'yes':
        break
    new_customer_id = input("Enter new customer ID: ").strip().upper()
    customer_ids.append(new_customer_id)

    unique_customer_ids = remove_duplicates_and_display_unique(customer_ids)
    print("\nUpdated Unique Customer IDs:")
    print_unique_customer_ids(unique_customer_ids)
