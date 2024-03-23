user_details = {
    "name": "test user",
    "email": "test@example.com",
    "password": "123456",
    "password_confirmation": "123456",
    "phone": 123456,
    "tax": 12.4,
    "favorite-colors": ["red", "green", "yellow", "blue"],
    "address": {
        "present_address": {
            "house_address": "dhaka",
            "street_address": 123,
            "postal_code": 1200

        },
        "permanent_address": {
            "house_address": "rajshahi",
            "street_address": 2111,
            "postal_code": 1000
        }
    }
}

post_code_permanent = user_details["address"]["permanent_address"]["postal_code"]
print(post_code_permanent)  # 1000

main_key_length = len(user_details)
sub_key_length = len(user_details["address"])
sub_sub_key_length = len(user_details["address"]["present_address"])
sub_sub_key_length2 = len(user_details["address"]["permanent_address"])

total = main_key_length + sub_key_length + sub_sub_key_length + sub_sub_key_length2
print(total)

user_details["language"] = "Python"
user_details["address"]["permanent_address"]["ward_number"] = 20
print(user_details["address"]["permanent_address"]["ward_number"])

sub_sub_key_length3 = len(user_details["address"]["permanent_address"])
print(sub_sub_key_length3)

del user_details["tax"]
print(user_details)
