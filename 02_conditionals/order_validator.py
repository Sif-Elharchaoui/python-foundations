ALLOWED_STATUSES = ("paid", "pending", "cancelled")
MAX_AMOUNT = 10000

order_id = input("Order id: ").strip()
amount = float(input("Amount: "))
status = input("Status: ").strip().lower()

problems = ""
if not order_id.isdigit():
    problems += "- order id must contain digits only\n"
if not (amount > 0 and amount <= MAX_AMOUNT):
    problems += "- amount must be above 0 and at most 10000\n"
if status not in ALLOWED_STATUSES:
    problems += "- status must be paid, pending, or cancelled\n"
if problems:
    print("INVALID")
    print(problems, end="")
else:
    print("VALID")