
REQUEST_LIMIT = 100
requests = int(input("Enter number of requests: "))
complete_groups = requests // REQUEST_LIMIT
remaining_requests = requests % REQUEST_LIMIT
total_groups = (requests + REQUEST_LIMIT - 1) // REQUEST_LIMIT
print(f"Complete groups: {complete_groups}")
print(f"Remaining requests: {remaining_requests}")
print(f"Total groups needed: {total_groups}")
