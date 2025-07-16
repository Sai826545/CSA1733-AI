import itertools

def solve_cryptarithm():
    # Unique letters in the equation SEND + MORE = MONEY
    letters = 'SENDMORY'
    
    # Ensure all letters are unique
    assert len(set(letters)) == len(letters)

    # Generate all possible digit assignments (0-9) for 8 letters
    for perm in itertools.permutations(range(10), len(letters)):
        letter_digit = dict(zip(letters, perm))

        # Skip if 'S' or 'M' is 0 (no leading zero allowed)
        if letter_digit['S'] == 0 or letter_digit['M'] == 0:
            continue

        # Form actual numbers
        send = (letter_digit['S'] * 1000 +
                letter_digit['E'] * 100 +
                letter_digit['N'] * 10 +
                letter_digit['D'])

        more = (letter_digit['M'] * 1000 +
                letter_digit['O'] * 100 +
                letter_digit['R'] * 10 +
                letter_digit['E'])

        money = (letter_digit['M'] * 10000 +
                 letter_digit['O'] * 1000 +
                 letter_digit['N'] * 100 +
                 letter_digit['E'] * 10 +
                 letter_digit['Y'])

        # Check if equation holds
        if send + more == money:
            print("Solution Found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            print(f"Mapping: {letter_digit}")
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithm()
