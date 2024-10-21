# PROBLEM 3 - Combo Deal

all_food_orders = [] # 2-d array where each row is a group order, and each element being amount of each food item.

# Key is index of food item and value is cost of that food item. 
# dictionary for menu 1, 'Checker McSonic's. 
cms_map = {
    0: 3, # small burger $3
    1: 6, # large burger $6
    2: 10, # specialty burger $10
    3: 3, # fries $3
    4: 2, # drink $2
    5: 4 # dessert $4
}

# dictionary for menu 2, 'WendCastle King'.
wck_map = {
    0: 2, # small burger $2
    1: 7, # large burger $7
    2: 9, # specialty burger $9
    3: 3, # fries $3
    4: 3, # drink $3
    5: 3 # dessert $3
}

# final constants of combo prices that will be used for final calculations, if any combos exist.
CMS_COMBO_1_PRICE = 11
CMS_COMBO_2_PRICE = 4
WCK_COMBO_1_PRICE = 9

orders_to_be_taken = 0 # first line of input tells us how many orders we will have.
current_order_num = 0 # current order we are on.


while True:
    user_input = input()
    if current_order_num == 0:
        orders_to_be_taken = int(user_input) # first input that tells us all group orders to be taken.
        current_order_num += 1
        continue

    current_group_order = user_input.split(' ')
    current_group_order = [int(food_item) for food_item in current_group_order] # cast amount of each food item into integer type
    all_food_orders.append(current_group_order)
    if orders_to_be_taken == current_order_num: break # we have taken all group orders
    current_order_num += 1


# will find any available combos for cms. returns an array of size 2, first element is combo 1 and second is combo 2.
def find_cms_combos(group_order):
    small_burger = group_order[0]
    specialty_burger = group_order[2]
    fries = group_order[3]
    dessert = group_order[5]

    combo_1 = True
    combo_2 = True
    combo_1_count = 0
    combo_2_count = 0

    while combo_1 or combo_2:
        # checking for combo #1 for cms
        if specialty_burger > 0 and dessert > 0: combo_1_count += 1
        else: combo_1 = False

        # checking for combo #2 for cms
        if small_burger > 0 and fries > 0: combo_2_count += 1
        else: combo_2 = False

        small_burger -= 1
        specialty_burger -= 1
        fries -= 1
        dessert -= 1
    
    return [combo_1_count, combo_2_count] # total combos if any are found for cms


# will find any available combos for wck. returns an integer of total combo 1's.
def find_wck_combos(group_order):
    large_burger = group_order[1]
    fries = group_order[3]
    drink = group_order[4]
    combo_1_count = 0

    while True:
        # checking for combo #1 for cms
        if large_burger > 0 and fries > 0 and drink > 0:
            combo_1_count += 1
            large_burger -= 1
            fries -= 1
            drink -= 1
        else: break
    
    return combo_1_count # total combos if any are found for wck


# adjust our orders based on any combos are found for either menu. We make a copy of the original order, then adjust number of items
# based on combos found. Returns a list w/ two sub-lists. First one is updated order with cms combos, and second is updated order
# with wck combos applied. Of course if no combos exist, the group order remains the same.
def adjust_order_based_on_combos(group_order, cms_combos, wck_combo):
    cms_combo_1 = cms_combos[0]
    cms_combo_2 = cms_combos[1]
    wck_combo_1 = wck_combo

    # making copies of original order
    updated_cms_group_order = group_order[:]
    updated_wck_group_order = group_order[:]

    while cms_combo_1 > 0:
        updated_cms_group_order[2] -= 1
        updated_cms_group_order[5] -= 1
        cms_combo_1 -= 1
    
    while cms_combo_2 > 0:
        updated_cms_group_order[0] -= 1
        updated_cms_group_order[3] -= 1
        cms_combo_2 -= 1
    
    while wck_combo_1 > 0:
        updated_wck_group_order[1] -= 1
        updated_wck_group_order[3] -= 1
        updated_wck_group_order[4] -= 1
        wck_combo_1 -= 1
    
    return [updated_cms_group_order, updated_wck_group_order] # adjusted orders with combos applied if any are found.


# We find total price with combos. Then add the combo total to our updated group order to find final total amount for the group order
# If we find that prices are the same, by default we order from WendyCastle King as there menu overall is cheaper.
def make_calculations_on_better_price(updated_cms_order, updated_wck_order, cms_combo_1, cms_combo_2, wck_combo_1):
    cms_combo_total = (cms_combo_1 * CMS_COMBO_1_PRICE) + (cms_combo_2 * CMS_COMBO_2_PRICE)
    wck_combo_total = wck_combo_1 * WCK_COMBO_1_PRICE
    
    final_cms_total = ((cms_map[0] * updated_cms_order[0]) + (cms_map[1] * updated_wck_order[1]) + 
                        (cms_map[2] * updated_cms_order[2]) + (cms_map[3] * updated_cms_order[3]) + 
                        (cms_map[4] * updated_cms_order[4]) + (cms_map[5] * updated_cms_order[5])) + cms_combo_total
    
    final_wck_total = ((wck_map[0] * updated_wck_order[0]) + (wck_map[1] * updated_wck_order[1]) + 
                        (wck_map[2] * updated_wck_order[2]) + (wck_map[3] * updated_wck_order[3]) + 
                        (wck_map[4] * updated_wck_order[4]) + (wck_map[5] * updated_wck_order[5])) + wck_combo_total
    
    if final_cms_total < final_wck_total:
        return f'CMS {final_cms_total}'
    else: return f'WCK {final_wck_total}'


# iterate through each group order, find the amount of combos available for the order from both menus, then
# we adjust those orders based on the combos found. Lastly we do the calculations once we have the updated orders and total combos.
for group_order in all_food_orders:
    # finding amount of combos available for cms.
    cms_combos = find_cms_combos(group_order)
    cms_combo_1 = cms_combos[0]
    cms_combo_2 = cms_combos[1]

    # finding amount of combos available for wck.
    wck_combo = find_wck_combos(group_order)

    # adjusting orders based on combos found.
    adjusted_orders = adjust_order_based_on_combos(group_order, cms_combos, wck_combo)
    updated_cms_order = adjusted_orders[0]
    updated_wck_order = adjusted_orders[1]

    # doing the calculations to get the final result.
    print(make_calculations_on_better_price(updated_cms_order, updated_wck_order, cms_combo_1, cms_combo_2, wck_combo))
