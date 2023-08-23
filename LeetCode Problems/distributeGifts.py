def distribute_gifts(kids, gifts, initial_kid1, initial_kid2):
    direction = "Clockwise"
    gift_counts = {kid: 0 for kid in kids}
    current_kid = initial_kid2    
    while gifts > 0:
        gift_counts[current_kid] += 1
        gifts -= 1
        next_kid = kids[(kids.index(current_kid) + 2) % len(kids)]
        current_kid = next_kid
        if next_kid == initial_kid1:
            direction = "Anti-Clockwise"
    max_gift_count = max(gift_counts.values())
    kids_with_max_gifts = [kid for kid, count in gift_counts.items() if count == max_gift_count]
    print(direction)
    for kid in kids_with_max_gifts:
        print(f"{kid}-{gift_counts[kid]}")
    print(f"{current_kid}-{gift_counts[current_kid]}")
kids = ["Nick", "Joe", "John", "Noah", "Damon"]
total_gifts = 13
initial_kid1 = "Damon"
initial_kid2 = "John"
distribute_gifts(kids, total_gifts, initial_kid1, initial_kid2)