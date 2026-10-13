REQUESTS_PER_HOUR = 5000
repositories = int(input("Enter the repos"))
requests_per_repository = int(input("requests per repo"))
total_requests = repositories * requests_per_repository
if total_requests == 0 :
    print("No requets to make")
else :
    full_windows = total_requests // REQUESTS_PER_HOUR
    leftover = total_requests % REQUESTS_PER_HOUR    
    windows_needed = full_windows
    if leftover > 0:
        windows_needed += 1
    if leftover > 0:
        requests_in_last_window = leftover
    else:
        requests_in_last_window = REQUESTS_PER_HOUR   

    print(f"Total requests: {total_requests}")
    print(f"Windows needed: {windows_needed}")
    print(f"Requests in the last window: {requests_in_last_window}")     