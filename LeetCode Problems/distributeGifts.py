# def distribute_gifts(kids, gifts, initial_kid1, initial_kid2):
#     direction = "Clockwise"
#     gift_counts = {kid: 0 for kid in kids}
#     current_kid = initial_kid2    
#     while gifts > 0:
#         gift_counts[current_kid] += 1
#         gifts -= 1
#         next_kid = kids[(kids.index(current_kid) + 2) % len(kids)]
#         current_kid = next_kid
#         if next_kid == initial_kid1:
#             direction = "Anti-Clockwise"
#     max_gift_count = max(gift_counts.values())
#     kids_with_max_gifts = [kid for kid, count in gift_counts.items() if count == max_gift_count]
#     print(direction)
#     for kid in kids_with_max_gifts:
#         print(f"{kid}-{gift_counts[kid]}")
#     print(f"{current_kid}-{gift_counts[current_kid]}")
# kids = ["Nick", "Joe", "John", "Noah", "Damon"]
# total_gifts = 13
# initial_kid1 = "Damon"
# initial_kid2 = "John"
# distribute_gifts(kids, total_gifts, initial_kid1, initial_kid2)



def find_kids_who_got_highest_number_of_gifts(number_of_kids, kids_list, number_of_gifts, gift_distributed_list):
    gift_counts = {}
    for kid in kids_list:
        gift_counts[kid] = 0

  # Initialize the current kid to the first kid in the list.
    current_kid = kids_list[0]

  # Iterate over the number of gifts.
    for i in range(gift_count):
    # Skip the immediate next kid.
        current_kid = kids_list[(current_kid + 1) % n]

    # Increment the number of gifts the current kid has received, unless the current kid is one of the initial two receivers.
    if current_kid not in gift_distributed_list:
        gift_counts[current_kid] += 1

  # Find the kid with the highest number of gifts.
    max_gift_count = 0
    max_gift_receiver = None
    for kid, gift_count in gift_counts.items():
        if gift_count > max_gift_count:
            max_gift_count = gift_count
            max_gift_receiver = kid

  # Return a list of the names of the kids who received the highest number of gifts, along with the number of gifts they received.
    return [
      (kid, gift_count)
      for kid, gift_count in gift_counts.items()
      if gift_count == max_gift_count
    ]

number_of_kids = int(input())
kids_list = []
for _ in range(number_of_kids):
    kid_name = input()
    kids_list.append(kid_name)
number_of_gifts = int(input())
gift_distributed_list = []
first_gift_distributed_to = input()
second_gift_distributed_to = input()
gift_distributed_list.append(first_gift_distributed_to)
gift_distributed_list.append(second_gift_distributed_to)
find_kids_who_got_highest_number_of_gifts(number_of_kids, kids_list, number_of_gifts, gift_distributed_list)
