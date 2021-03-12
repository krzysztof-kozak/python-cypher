from alphabet import alphabet

def cypher(direction, text, shift):
    end_message = ""
    action = "default_action"

    for letter in text:
        if letter not in alphabet:
            end_message += letter
            continue

        if direction == "decode":
            action = "decoded"
            print("decoding in progress...")

            shifted_index = alphabet.index(letter) - shift
            end_message += alphabet[shifted_index]

        elif direction == "encode":
            action = "encoded"
            print("encoding in progress...")

            index_bound = len(alphabet) - 1
            shifted_index = alphabet.index(letter) + shift

            if shifted_index >= index_bound:
                end_message += alphabet[shifted_index % index_bound - 1]

            else:
                end_message += alphabet[shifted_index]

    print(f"Your {action} message is {end_message}")
