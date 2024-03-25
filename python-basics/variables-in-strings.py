#VARIABLES IN STRINGS
#f-strings: f is for format

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)