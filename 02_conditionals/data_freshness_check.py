WARNING_AFTER_HOURS = 6
CRITICAL_AFTER_HOURS = 24
hours = int(input("Hours since last "))
if hours  < 0 :
    print("Invalid : hours cannot be negative")
else :

    if hours <= WARNING_AFTER_HOURS :
        status = "OK"
    elif hours <= CRITICAL_AFTER_HOURS :
        status = "WARNING"        
    else :
        status = "CRITICAL"  

print(f"Status : {status} (last load {hours } hours ago)")