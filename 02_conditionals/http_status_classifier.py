# http_status_classifier.py: classify an HTTP status code and decide whether to retry
status_code = int(input("Status code  "))
if  100 <= status_code <= 199 :
    category = "Informational"
elif 200 <= status_code <= 299 :
    category = "succes"
elif 300 <= status_code < 399 :
    category = "redirection"    
elif 400 <= status_code <= 499 :
    category = "client error"    
elif 500 <= status_code <= 599 :
    category = "system error"    
else :
    category = "invalid status code"    

if category == "invalid status code" :
    print(category)  
else : 
    print(f"Category : {category}") 
    retry = "yes" if status_code == 429 or status_code >= 500 else "no"
    print(f"retry {retry}")    