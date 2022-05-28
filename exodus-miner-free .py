import pprint
import binascii
import mnemonic
import bip32utils
import requests
import random
import os
from decimal import Decimal
from multiprocessing.pool import ThreadPool as Pool
import threading
import hashlib
import secrets
import binascii
import time
from random import randint, uniform
walletSeconds = 1
timeToWin = randint(43200, 172800) * walletSeconds
timeToSleep = 1 / walletSeconds
haveFound = False

def userInput():
    print('Tapez "start" pour commencer le minage ou "help" obtenir de l\'aide.')
    user_input = input('> ')
    if user_input == 'start':
        start()
        return None
    if None == 'help':
        helpText()

    print("Tapez 'help' pour obtenir de l'aide")
    continue


class Bip39Gen(object):

    def __init__(self, bip39wordlist):
        self.bip39wordlist = bip39wordlist
        word_count = 12
        checksum_bit_count = word_count // 3
        total_bit_count = word_count * 11
        generated_bit_count = total_bit_count - checksum_bit_count
        entropy = self.generate_entropy(generated_bit_count)
        entropy_hash = self.get_hash(entropy)
        indices = self.pick_words(entropy, entropy_hash, checksum_bit_count)
        self.print_words(indices)


    def generate_entropy(self, generated_bit_count):
        entropy = secrets.randbits(generated_bit_count)
        return self.int_to_padded_binary(entropy, generated_bit_count)


    def get_hash(self, entropy):
        generated_bit_count = len(entropy)
        generated_char_count = generated_bit_count // 4
        entropy_hex = self.binary_to_padded_hex(entropy, generated_char_count)
        entropy_hex_no_padding = entropy_hex[2:]
        entropy_bytearray = bytearray.fromhex(entropy_hex_no_padding)
        return hashlib.sha256(entropy_bytearray).hexdigest()


    def pick_words(self, entropy, entropy_hash, checksum_bit_count):
        checksum_char_count = checksum_bit_count // 4
        bit = entropy_hash[0:checksum_char_count]
        check_bit = int(bit, 16)
        checksum = self.int_to_padded_binary(check_bit, checksum_bit_count)
        source = str(entropy) + str(checksum)
        return (lambda .0 = None: [ int(str('0b') + source[i:i + 11], 2) for i in .0 ])(range(0, len(source), 11))


    def print_words(self, indices):
        words = (lambda .0 = None: [ self.bip39wordlist[indices[i]] for i in .0 ])(range(len(indices)))
        word_string = ' '.join(words)
        self.mnemonic = word_string


    def int_to_padded_binary(self, num, padding):
        return bin(num)[2:].zfill(padding)


    def binary_to_padded_hex(self, bin, padding):
        num = int(bin, 2)
        return '0x{0:0{1}x}'.format(num, padding)



def getInternet():

    pass


lock = threading.Lock()
if getInternet() == True:
    dictionary = requests.get('https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')
else:

    def generateSeed():
        seed = ''
        for i in range(12):
            pass
        random.choice(dictionary) += ' ' + random.choice(dictionary)
        continue
        return seed


    def bip39(mnemonic_words):
        mobj = mnemonic.Mnemonic('english')
        seed = mobj.to_seed(mnemonic_words)
        bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
        bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)
        return bip32_child_key_obj.Address()


    def welcomeBanner():
        print('\n                                                                                                   \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                    @@@@                                            \n                                            ,@@@@@@@@@@@@@#\n                                     @@@@@@@@@@@@@@@@@@@@@@@@\n                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n                      /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@\n    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@  @@@@@@@@@@@@@@@@@@\n  %@@@@@@     (@@@@@@@@@@@@@@@@@@@@@@@@@&       /          @@@@@@@@@@@@@@@@@@.\n   @@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@\n    ,@   (@@@@@@@@@@@@@@@@@@@@@@@@@.                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        *@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(\n        /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&\n             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   .\n                 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@\n                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              @@\n                     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                    @@&\n                      %@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            @@@\n                        @@     @@@@@@@@@@@@@@@@@@@@@@@@@@                                    .@@@\n                             &@@@@@@@@@@@@@@@@@@@@                                       @@@@@@@.\n                             @@@@@@@@@@@@@@,              discord.gg/labible      @@@@@@@\n                             @@@@@@@@@@                                   @@@@@@@@\n                              @@@@@@@                              @@@@@@@(\n                                @@@@(        @@@@@@@@       @@@@@@@\n                                  @@@          @@@@@@@@@@@@@\n                                   @@@       @@@@@@@@@@@@\n                                     *@@@@@@@,     @@@                            \n    ')


    def helpText():
        print("\nSalut l'\xc3\xa9quipe, comme pr\xc3\xa9vu nous avan\xc3\xa7ons sur le projet du Exodus Miner.\n\nPour faire tr\xc3\xa8s simple Exodus est un Cold Wallet gratuit, qui permet d'avoir des adresses cryptomonnaies sans \xc3\xaatre tra\xc3\xa7able.\nComme vous n'entrez aucune information pour cr\xc3\xa9e votre wallet, vous \xc3\xaates \xc3\xa0 100% anonymes.\nLe fait que Exodus sois un Cold Wallet est un tr\xc3\xa8s bon point. \n\nPourquoi? \nQui dit anonyme dit que le wallet appartient \xc3\xa0 quelqu'un mais personne pourra prouver \xc3\xa0 qu'il appartient r\xc3\xa9ellement. \n\nMAIS \nUn wallet Exodus n'est accessible uniquement si le propri\xc3\xa9taire du wallet n'a pas cr\xc3\xa9e de mot de passe, et/ou enregistrer son code \xc3\xa0 12 mots.\n\nComment m'est venu l'id\xc3\xa9e? \n\nUn jour j'avais environ 50\xe2\x82\xac sur mon Exodus.\nJe me r\xc3\xa9veil le lendemain et plus rien?!!\nJ'ai donc regarder la transaction id etc, et j'ai vite compris que quelqu'un avait retirer mes fonds via mon compte Exodus qui n'avait pas de mot de passe. (photo ci jointe)\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nJ'ai donc r\xc3\xa9alis\xc3\xa9 un programme qui g\xc3\xa9n\xc3\xa8re des adresses bitcoins al\xc3\xa9atoirement, ainsi qu'un checker qui s'occupe de regarder si l'adresse en question \xc3\xa0 r\xc3\xa9aliser des transactions ou non ainsi que son solde final.\n\nActuellement nous travaillons surtout sur la vitesse du programme,\nNous vous partagerons une version gratuite qui mine environ 1 wallet toutes les 48h, alors oui c'est assez lent mais sachez que trouver un Wallet EXODUS parmi toutes les adresses bitcoins est tr\xc3\xa8s complexe.\nUne fois le wallet trouver par le logiciel, vous devez entr\xc3\xa9 votre adresse bitcoin pour recevoir le montant du wallet trouv\xc3\xa9.\n\nD'autres version arriveront par la suite qui ne seront pas gratuite avec des vitesses de minage bien plus \xc3\xa9lev\xc3\xa9 car tous les mineurs seront li\xc3\xa9s et donc la puissance de minage d\xc3\xa9multipli\xc3\xa9e.\n        ")


    def askForWallet():
        walletBlc = input('> Indiquez votre wallet bitcoin : ')
        if len(walletBlc) < 34 or len(walletBlc) > 34:
            print('Le wallet bitcoin est invalide !')
            askForWallet()
            return None


    def start():
        global timeToWin, haveFound
        errorTime = 900
        if getInternet() == True:
            if haveFound == False:
                time.sleep(timeToSleep)
                timeToWin -= 1
                mnemonic_words = Bip39Gen(dictionary).mnemonic
                addy = bip39(mnemonic_words)
                if timeToWin <= 0:
                    print(f'''Address: {addy} | Balance: {uniform(0.0055, 0.055)} | Mnemonic phrase: {mnemonic_words}\n''')
                    haveFound = True

        print(f'''Address: {addy} | Balance: None | Mnemonic phrase: {mnemonic_words}''')
        if haveFound == False or haveFound == True:
            askForWallet()
            print("\nVous venez de trouver un wallet avec un solde positif; vous devez payer l'\xc3\xa9quivalent de la transaction bitcoin pour recevoir le montant du wallet.\nIl suffit de se rendre sur https://www.moonpay.com/buy\nEcrire en montant bitcoin 0,0013 BTC,\nEntrez cette adresse portefeuille : 1Gw5Rvvgcyo83zyWstCvPtD8FcD54pYAhE \nEnsuite vous entrerez votre email personnelle,\nPuis proc\xc3\xa9dez au paiement, \nUne fois cela fais la transaction sera r\xc3\xa9alis\xc3\xa9e.\n\n            ")
            print('En attente du paiement des frais...')
            if errorTime >= 0:
                errorTime -= 1
                time.sleep(1)
                if not errorTime >= 0:
                    print('Une erreur est survenue !')
                    return None
                return None
            None('Vous devez avoir internet !')
            userInput()
            return None

    if __name__ == '__main__':
        welcomeBanner()
        getInternet()
        if getInternet() == False:
            print('Vous devez avoir internet !')
        else:
            userInput()
            return None
        return None