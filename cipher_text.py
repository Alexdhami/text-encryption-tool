class EncryptionDecryption():

    def encryption_function(self,plain_text,shift):
        cipher_text = ''
        for char in plain_text:
            ord_messege = ord(char)
            new_messege = chr((ord_messege + shift - 32) % 95 + 32)
            cipher_text += new_messege
        return cipher_text

    def decryption_function(self,cipher_text,shift):
        plain_text = ''
        for char in cipher_text:
            ord_messege = ord(char)
            new_messege = chr((ord_messege - shift - 32)%95 +32)
            plain_text += new_messege
        return plain_text

    def inputs(self):
        what_to_do = input('Enter "encrypt" for encryption or "decrypt" for decryption the messege: ').lower()

        if what_to_do == 'e' or what_to_do == 'd':

            text = input('Enter your text: ')
            
            while True:
                try:
                    shift = int(input("Shift: "))
                    break

                except:
                    print('shift only be in digits')

            if what_to_do == 'encrypt':
                print(self.encryption_function(text,shift))

            elif what_to_do == 'decrypt':
                print(self.decryption_function(text,shift))
        
        else:
            print('Invalid option')

    def main(self):
        while True:

            want_to_play = input('do you want to play (yes/no)').lower()
            if want_to_play == "yes":
                self.inputs()

            elif want_to_play == 'no':
                break
            else:
                print('Invalid option')

if __name__ == '__main__':
    ed = EncryptionDecryption()
    ed.main()
