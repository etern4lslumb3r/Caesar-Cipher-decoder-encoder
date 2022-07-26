# Caesar cipher
from typing import List
from colorama import Style, Fore
import replit


replit.clear()

class CaesarCipher:
    
    def __init__(self, alphabet:str):
        self.alphabet_set = set()
        self.alphabet_new = ""
        self.duplicates = []
        for char in alphabet:
            if char not in self.alphabet_set:
                self.alphabet_set.add(char)
                self.alphabet_new += char.strip()
            elif char in self.alphabet_set:
                self.duplicates.append(char)
        self.characters_lower = self.alphabet_new.lower()
        self.characters_upper = self.alphabet_new.upper()

    def encode_text(self,s: str, shift: int) -> str:
        output = ""
        for current_letter in s:
            if current_letter not in self.characters_lower + self.characters_upper:
                output += current_letter

            elif current_letter in self.characters_lower:
                for char_index in range(len(self.characters_lower)):
                    if current_letter == self.characters_lower[char_index]:
                        shift_amount = (char_index + shift) % len(self.characters_lower)
                        new_char = self.characters_lower[shift_amount]
                        output += new_char

            elif current_letter in self.characters_upper:
                for char_index in range(len(self.characters_upper)):
                    if current_letter == self.characters_upper[char_index]:
                        shift_amount = (char_index + shift) % len(self.characters_upper)
                        new_char = self.characters_upper[shift_amount]
                        output += new_char

        return output


    def decode_text(self, s: str) -> List[str]:
        outputs = []
        for shift in reversed(range(len(self.characters_lower))):
            output = self.encode_text(s, shift)
            outputs.append(output)
        return outputs


if __name__ == "__main__":
    alphabet = input("Type in the alphabet being used in the plaintext: ")
    cs = CaesarCipher(alphabet=alphabet)
    for duplicate in cs.duplicates:
        print(Fore.RED + "Duplicate removed: {}".format(duplicate) +Style.RESET_ALL)
    print(Fore.CYAN + "Current Alphabet: " + cs.alphabet_new + Style.RESET_ALL +"\n")

    while True:
        try:
            print("What would you like to do?")
            print(Fore.CYAN + "1. Encode" + Style.RESET_ALL)
            print(Fore.YELLOW + "2. Decode" + Style.RESET_ALL)
            print(Fore.RED + "3. Quit" + Style.RESET_ALL)
            mode = int(input("\nInput: "))
        except:
            print(Fore.RED + "Input valid input." + Style.RESET_ALL)
            continue

        if mode == 1:
            while True:
                input_text = input(Fore.CYAN + '\nEncode text:  ' +
                                   Style.RESET_ALL)
                if len(input_text) == 0:
                    print(Fore.RED + "Input valid input." + Style.RESET_ALL)
                    continue
                break
            while True:
                try:
                    shift = int(
                        input(Fore.CYAN + "Shift text by: " + Style.RESET_ALL))
                    break
                except:
                    print(Fore.RED + "Input valid input" + Style.RESET_ALL)
                    continue
            print(Fore.CYAN + "Encoded text: " + Style.RESET_ALL +
                  Fore.YELLOW + cs.encode_text(input_text, shift) +
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
            for index, i in enumerate(cs.decode_text(input_text)):
                if index+1 == len(cs.characters_lower):
                    continue
                print(Fore.YELLOW+f"[Shift: {index+1}]:  "+Style.RESET_ALL + i +"\n"+ Style.RESET_ALL)
            input("\n[Press Enter to continue]")
        elif mode == 3:
            quit(Fore.RED+"\nEnded\n"+Style.RESET_ALL)

        if mode != 1 or mode != 2 or mode != 3:
            continue
