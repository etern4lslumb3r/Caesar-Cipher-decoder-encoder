# Caesar cipher
import string
from typing import List
from colorama import Style, Fore
import replit

replit.clear()
characters_lower = string.ascii_lowercase
characters_upper = string.ascii_uppercase


def encode_text(s: str, shift: int) -> str:
    output = ""
    for current_letter in s:
        if current_letter not in characters_lower + characters_upper:
            output += current_letter

        elif current_letter in characters_lower:
            for char_index in range(len(characters_lower)):
                if current_letter == characters_lower[char_index]:
                    shift_amount = char_index + shift
                    if shift_amount > len(characters_lower) - 1:
                        shift_amount = shift_amount - len(characters_lower)
                    new_char = characters_lower[shift_amount]
                    output += new_char

        elif current_letter in characters_upper:
            for char_index in range(len(characters_upper)):
                if current_letter == characters_upper[char_index]:
                    shift_amount = char_index + shift
                    if shift_amount > len(characters_lower) - 1:
                        shift_amount = shift_amount - len(characters_lower)
                    new_char = characters_upper[shift_amount]
                    output += new_char

    return output


def decode_text(s: str) -> List[str]:
    outputs = []
    for shift in range(26):
      output = encode_text(s, shift)
      outputs.append(output)
    return outputs

if __name__ == "__main__":
    while True:
        try:
            mode = int(
                input("""
What would you like to do?
1. Encode
2. Decode
3. Quit

Input: """))
        except:
            print(Fore.RED + "Input valid input." + Style.RESET_ALL)
            continue

        if mode == 1:
            while True:
                input_text = input(Fore.CYAN + '\nEncode text: ' +
                                   Style.RESET_ALL)
                if len(input_text) == 0:
                    print(Fore.RED + "Input valid input." + Style.RESET_ALL)
                    continue
                break
            while True:
                try:
                    shift = int(
                        input(Fore.CYAN + "Shift text by: " + Style.RESET_ALL))
                    if shift > 26:
                        print(Fore.RED + "\nInput a number less than 26\n" + Style.RESET_ALL)
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Input valid input" + Style.RESET_ALL)
                    continue
            print(Fore.CYAN + "Encoded text: " + Style.RESET_ALL +
                  Fore.YELLOW + encode_text(input_text, shift) +
                  Style.RESET_ALL)
            input("\n[Press Enter to continue]\n")

        elif mode == 2:
            while True:
                input_text = input(Fore.YELLOW + "Decode text: " +
                                   Style.RESET_ALL)
                if len(input_text) == 0:
                    print(Fore.RED + "Input valid input." + Style.RESET_ALL)
                    continue
                break
            print("\nPossibilities: \n")
            for index, i in enumerate(decode_text(input_text)):
                print(Fore.YELLOW+f"[Shift: {index}]:  "+Style.RESET_ALL + i +"\n"+ Style.RESET_ALL)
            input("\n[Press Enter to continue]")
        elif mode == 3:
            quit("Ended")

        if mode != 1 or mode != 2 or mode != 3:
            continue
