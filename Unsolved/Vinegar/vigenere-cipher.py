# Vigenere Cipher program

class Vigenere:
    """Vigenere Cipher program."""

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def __str__(self):
        print("Vigenere Cipher program.")

    def __encrypt(self):
        encrypted = ""
        i = 0
        for letter in self.message:
            if ord(letter) + self.key[i] > 90:
                new_key = ord(letter) + self.key[i] - 90
                new_letter = chr(64 + new_key)
                encrypted += new_letter
                i += 1
                if len(self.key) == i:
                    i = 0
            else:
                encrypted += (chr(ord(letter) + self.key[i]))
                i += 1
                if len(self.key) == i:
                    i = 0
        return encrypted

    def __decrypt(self):
        decrypted = ""
        i = 0
        for letter in self.message:
            if ord(letter) - self.key[i] < 65:
                new_key = 65 - (ord(letter) - self.key[i])
                new_letter = chr(91 - new_key)
                decrypted += new_letter
                i += 1
                if len(self.key) == i:
                    i = 0
            else:
                decrypted += chr(ord(letter) - self.key[i])
                i += 1
                if len(self.key) == i:
                    i = 0
        return decrypted

def get_message():
    userMessage = ""
    final_message = ""
    flag = True
    while flag:
        userMessage = input("\nYour message: ")
        if len(userMessage) < 1:
            print("\nYou must enter something!")
            continue
        userMessage = userMessage.replace(" ", "")
        for i in range(len(userMessage)):
            if not userMessage[i].isalpha():
                continue
            else:
                final_message += userMessage[i]
        if len(final_message) < 1:
            continue
        else:
            flag = False
    return final_message.upper()

def get_key():
    userKey = ""
    keys = []
    final_keys = []
    flag = True
    while flag:
        userKey = input("\nYour key: ")
        if len(userKey) < 1:
            print("You must enter something!")
            continue
        userKey = userKey.replace(" ", "")
        for i in range(len(userKey)):
            if not userKey[i].isalpha():
                continue
            else:
                keys.append(ord(userKey[i].upper()))
                final_keys.append(keys[i] - 64)
        if len(final_keys) < 1:
            continue
        flag = False
    return final_keys

def encrypt_or_decrypt():
    userChoice = ""
    flag = True
    while flag:
        userChoice = input("\nEncrypt or decrypt? (E/D): ")
        if userChoice not in ("e", "E", "d", "D"):
            continue
        else:
            flag = False
    return userChoice

if __name__ == "__main__":
    flag = True
    while flag:
        userChoice = encrypt_or_decrypt()
        message = get_message()
        key = get_key()
        cipher = Vigenere(message, key)
        if userChoice in ("e", "E"):
            encrypted = cipher._Vigenere__encrypt()
            print(encrypted)
        else:
            decrypted = cipher._Vigenere__decrypt()
            print(decrypted)
        userInput = input("\nAgain? (Y/N): ")
        while userInput not in ("y", "Y", "n", "N"):
            userInput = input("\nAgain? (Y/N): ")
        if userInput in ("y", "Y"):
            continue
        elif userInput in ("n", "N"):
            print("Exiting.")
            flag = False
    input("\n\nPress the enter key to exit.")