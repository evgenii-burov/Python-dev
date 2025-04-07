class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def cipher(self, original_text, shift):
        cipher_text = ''
        for symbol in original_text:
            symbol_index =ord(symbol)-ord('а')
            if symbol_index+shift>len(self.alphabet)-1:
                cipher_text+=self.alphabet[symbol_index+shift-len(self.alphabet)-1
                                           ]
            cipher_text+=self.alphabet[symbol_index+shift]
        return cipher_text
    
    
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        original_text = ''
        for symbol in cipher_text:
            symbol_index = ord(symbol)-ord('а')
            if symbol_index-shift<0:
                cipher_text+=self.alphabet[len(self.alphabet)-1-(symbol_index-shift)]
            cipher_text+=self.alphabet[symbol_index-shift]
        return original_text


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))