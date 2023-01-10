# lists and strings

# list() function

name = "josh"
string_list = list(name) # --> ['j', 'o', 's', 'h']

print(string_list) # use snake_case when working with python


new_name = "josh gumerove"
string_split = new_name.split() # note what is being converted (do not need to pass argument)
print(string_split)

phone_number = '310-557-2221'
split_number = phone_number.split("-")
print(split_number)

if split_number[0] == "310":
    print("receiving call from Los Angeles")
else:
    print("receiving call from else where")
    
number_formatter = "-"
formatted_phone_number = number_formatter.join(split_number) # method is on the delimiter and pass the list in as an argument
print(formatted_phone_number)