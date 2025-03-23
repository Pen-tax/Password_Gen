### allows user to input some paramiters in order to create a unique password

import random
## some general strings that will be included in the password
number = "1234567890"
symbols = "!<>?*()&^$£#@"

def password(number,symbols):
  ## Character sets for the languages
  english = "abcdefghijklmnopqrstuvwxyz"
  german = str(english) + "ÄÖÜß"
  arabic = "ﺍﺏﺕﺙﺝﺡﺥﺩﺫﺭﺯﺱﺵﺹﺽﻁﻅﻉﻍﻑﻕﻙﻝﻡﻥﻩﻭﻱ"
  japanese = "あいうえおはひふへほかきくけこまみむめもさしすせそやゆよたちつてとらりるれろなにぬねのわゐんゑを"
  enchantment_table = "ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹!¡ᑑ∷ᓭℸ ̣ ⚍⍊∴ ̇/||⨅"

  ## while loop allows user to pick language correctly
  chosen_lang = False
  while chosen_lang == False:
    user_lang = input("Please Enter a Language From Below:\n\nEnglish\nGerman\nArabic\nJapanese\nEnchantment Table\n\nEnter Here: ").lower()
  ## gives an error message if user input is incorrect 
    if user_lang == "english" or user_lang == "german" or user_lang == "arabic" or user_lang == "japanese" or user_lang == "enchantment table":
      print("\nYou Have Chosen {}!\n".format(user_lang))
      chosen_lang = True
    else:
      print("\nPlease Pick From the Languages Above!\n")
      
  ## another while loop for the chosen length
  length_true = False
  while length_true == False:
    try:
      length = int(input("Please Enter a Length For your password\nEnter Here: "))
      if length < 70:
        length_true = True
        print("\nYour Password will be {} Characters long\n".format(length))
      else:
        print("Please Enter a Number that would be more realistic for a password...\n")
    except:
      print("\nPlease Enter a Number!\n")
## this part is basically like making a sandwitch ~ just adding in all the variables you prepared
  user_password = ""
  if user_lang == "english":
    eng = english.upper() + english + number + symbols
    user_password = "".join(random.sample(eng,length))
    print("Your Password is:\n\n{}\n".format(user_password))
  if user_lang == "german":
    ger = german.upper() + german + number + symbols
    user_password = "".join(random.sample(ger,length))
    print("Your Password is:\n\n{}\n".format(user_password))
  if user_lang == "arabic":
    arb = arabic.upper() + arabic + number + symbols
    user_password = "".join(random.sample(arb,length))
    print("Your Password is:\n\n{}\n".format(user_password))
  if user_lang == "japanese":
    jpn = japanese.upper() + japanese + number + symbols
    user_password = "".join(random.sample(jpn,length))
    print("Your Password is:\n\n{}\n".format(user_password))
  if user_lang == "enchantment table":
    ech_tbl = enchantment_table.upper() + enchantment_table + number + symbols
    user_password = "".join(random.sample(ech_tbl,length))
    print("Your Password is:\n\n{}\n".format(user_password))


## main
print(" ___                                  _   __ __                                    _ _  _ \n| . \ ___  ___ ___ _ _ _  ___  _ _  _| | |  \  \ ___ ._ _  ___  ___  ___  _ _     | | |/ |\n|  _/<_> |<_-<<_-<| | | |/ . \| '_>/ . | |     |<_> || ' |<_> |/ . |/ ._>| '_>___ | ' || |\n|_|  <___|/__//__/|__/_/ \___/|_|  \___| |_|_|_|<___||_|_|<___|\_. |\___.|_| |___||__/ |_|\n                                                               <___'                      ")

password(number,symbols)
    
  

  