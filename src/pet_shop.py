# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_searched):
    breed_total = []
    for pet in pet_shop["pets"]:
        if breed_searched == pet["breed"]:
            breed_total.append(breed_searched)
    return breed_total
    

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {}
    pet_shop["pets"].append(new_pet)
    return len(pet_shop["pets"])
#this test passed BUT wouldn't add any information to the new dictionary
#below is an example of a test that I THINK would fulfil this secondary function

# def add_pet_to_stock(pet_shop, new_pet_name):
#     new_pet = {"name" : str(new_pet_name)}
#     pet_shop["pets"].append(new_pet)
#     return len(pet_shop["pets"])

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

#same as above but should add this new pet as a dictionary so it can hold more data
# def add_pet_to_customer(customer, new_pet_name):
#     new_pet = {"name" : str(new_pet_name)}
#     customer["pets"].append(new_pet)
#     return len(customer["pets"])
#only problem with this one is that it doesn't remove this pet from the pet shop, as it presumably has been taken from there.

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False



