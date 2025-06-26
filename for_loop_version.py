def get_starting_number():
    while True:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit():
            number = int(user_input)
            if number >= 1:
                return number

def sing(start):
    for bottles in range(start, 0, -1):
        if bottles > 1:
            next_bottles = bottles - 1
            bottle_word = "bottles"
            next_word = "bottles"
            if next_bottles == 1:
                next_word = "bottle"
            print(f"{bottles} {bottle_word} of beer on the wall, {bottles} {bottle_word} of beer.")
            print(f"Take one down, pass it around, {next_bottles} {next_word} of beer on the wall.")
            print()
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            print()
