def process_user_at_entry(user_name: str, user_weight: float, user_age: int) -> str:
    result = f"User {user_name}, with weight: {user_weight} and age: {user_age} has been correctly stored in database"

    return result

# User 1
bellotas_name = "Bellota"
bellotas_weight = 10.4
bellotas_age = 3

# User 2
bombons_name = "Bombon"
bombons_weight = 20.4
bombons_age = 2

# User 3
burbujas_name = "Burbuja"
burbujas_weight = 25.0
burbujas_age = 5

user_1_entry = process_user_at_entry(
    user_name=bellotas_name,
    user_weight=bellotas_weight,
    user_age=bellotas_age
)

user_2_entry = process_user_at_entry(
    user_name=bombons_name,
    user_weight=bombons_weight,
    user_age=bombons_age
)
user_3_entry = process_user_at_entry(
    user_name=burbujas_name,
    user_weight=burbujas_weight,
    user_age=burbujas_age
)

print(user_1_entry)
print("-------------------------")
print(user_2_entry)
print("-------------------------")
print(user_3_entry)
print("-------------------------")