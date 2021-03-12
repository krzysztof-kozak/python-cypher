def get_user_input():

    valid_choices = ["encode", "decode"]
    direction = "default"
    while direction not in valid_choices:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = "default"

    while not shift.isdigit():
        shift = input("Type the shift number (integer), e.g 5:\n")

    shift = int(shift)

    return text, shift, direction
