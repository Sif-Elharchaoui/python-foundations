PLATFORM_FEE_RATE = 0.10
RATE_PER_LESSON = 260 
lessons = int(input("Number of lessons "))
gross_earnings = RATE_PER_LESSON * lessons 
platform_fee = gross_earnings * 0.10 
net_earnings = gross_earnings - platform_fee 
print(f"Gross earnings: {gross_earnings:.2f} RMB")
print(f"Platform fee: {platform_fee:.2f} RMB")
print(f"Net earnings: {net_earnings:.2f} RMB")

