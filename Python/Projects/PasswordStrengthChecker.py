# Define character types by their ASCII value

characters = [chr(c) for c in range(33,127)]
numbers = [chr(c) for c in range(48,58)]
uppers = [chr(c) for c in range(65,91)]
lowers = [chr(c) for c in range(97,123)]
symbols = [c for c in characters if c not in numbers + uppers + lowers]

pw = input("Enter an 8-32 character password.\n\n")

if 8 > len(pw) or 32 < len(pw):
    print("Must be between 8 and 32 characters long.")
    quit()

if any(c for c in pw if c not in characters):
    print("Only printable ASCII characters allowed.")
    quit()

def rate_password(pw):
    """Rate password strength.
    A password with 25-32 characters including at least one number, one upper case letter, one lower case letter and one symbol scores 10/10.
    """

    #Initialize score
    score = 0

    #Set flags for numbers, upper case letters, lower case letters, symbols and length.
    nu, uc, lc, sy, le = 1, 1, 1, 1, 0

    #Check password for character types, increase the score and change the flag for each character type in the password.
    if any(c for c in pw if c in numbers):
        score += 1
        nu = 0

    if any(c for c in pw if c  in uppers):
        score += 1
        uc = 0

    if any(c for c in pw if c in lowers):
        score += 1
        lc = 0

    if any(c for c in pw if c in symbols):
        score += 1
        sy = 0

    #Add 2 to the score if length is 8-16.
    if len(pw) < 17:
        score += 2
        le = 1

    #Add 4 to the score if length is 17-24.
    elif len(pw) < 25:
        score += 4
        le = 1

    #Add 6 to the score if length is 25-32.
    else:
        score += 6
    return score, nu, uc, lc, sy, le

#Call the function and assign the returned values.
score, nu, uc, lc, sy, le = rate_password(pw)

print(f"Your password '{pw}' scored {score} out of 10.")

if score < 10:
    #If flag is 0, the corresponding text and new line are not printed.
    print()
    print("To score higher, your password needs:")
    print(f"{nu * 'Numbers'}", end="\n" if nu else "")
    print(f"{uc * 'Upper case characters'}", end="\n" if uc else "")
    print(f"{lc * 'Lower case characters'}", end="\n" if lc else "")
    print(f"{sy * 'Symbols'}", end="\n" if sy else "")
    print(f"{le * 'More characters'}")
