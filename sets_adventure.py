def compare_routes(our_routes, competitor_routes):
    common_destinations = our_routes.intersection(competitor_routes)

    unique_to_us = our_routes.difference(competitor_routes)

    unique_to_competitor = competitor_routes.difference(our_routes)

    neither_shared = our_routes.symmetric_difference(competitor_routes)

    return common_destinations, unique_to_us, unique_to_competitor, neither_shared

def print_results(common_destinations, unique_to_us, unique_to_competitor, neither_shared):
    print("Destinations that both airlines fly to:", common_destinations)
    print("Destinations unique to our airline:", unique_to_us)
    print("Destinations unique to competitor's airline:", unique_to_competitor)
    print("Destinations that neither airline shares:", neither_shared)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations, unique_to_us, unique_to_competitor, neither_shared = compare_routes(our_routes, competitor_routes)

print_results(common_destinations, unique_to_us, unique_to_competitor, neither_shared)

while True:
    add_more = input("\nDo you want to add another destination for your airline? (yes/no): ").lower()
    if add_more != 'yes':
        break
    new_destination = input("Enter new destination: ").strip().upper()
    our_routes.add(new_destination)

    common_destinations, unique_to_us, unique_to_competitor, neither_shared = compare_routes(our_routes, competitor_routes)
    print("\nUpdated Results:")
    print_results(common_destinations, unique_to_us, unique_to_competitor, neither_shared)
