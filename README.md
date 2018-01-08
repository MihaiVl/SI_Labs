## Laboratory Work nr.3 for Informational Security
## Breaking Shift Cipher

A shift cipher is an encryption technique used even by the great, glorious, heroic, remarkable, talented, and noble Caesar (the Julius one) in his private correspondence.
So the message THE GREAT FAF OF THE ROMAN EMPIRE, if encrypted with a right shift of 3 becomes: WKH JUHDW IDI RI WKH URPDQ HPSLUH.

Example:

>    GUR EBZNA RZCVER JNF GUR CBFG-EBZNA ERCHOYVP CREVBQ BS GUR NAPVRAG EBZNA PVIVYVMNGVBA, PUNENPGREVMRQ OL TBIREAZRAG URNQRQ OL   > RZCREBEF NAQ YNETR GREEVGBEVNY UBYQVATF NEBHAQ GUR ZRQVGREENARNA FRN VA RHEBCR, NSEVPN NAQ NFVN.

Making a frequency analysis on the above text you can conclude that the most used character is R. Assuming that the text is in English and knowing that the most used letter in the English language is E you can make the (wild) guess (that is not that wild, really) that E has been substituted by R, thus concluding that right shift of 13 has been used. Applying this rule on the above text, the following result ensues:

> THE ROMAN EMPIRE WAS THE POST-ROMAN REPUBLIC PERIOD OF THE ANCIENT ROMAN CIVILIZATION, CHARACTERIZED BY GOVERNMENT HEADED BY     > EMPERORS AND LARGE TERRITORIAL HOLDINGS AROUND THE MEDITERRANEAN SEA IN EUROPE, AFRICA AND ASIA.


## My approach:

For this laboratory work I selected two sets of frequency set of letters from two different languages, english and latin.


> engDictionary = *"EARIOTNSLCUDPMHGBFYWKVXZJQ"*

> latinDictionary = *"eituasrnomcpldqbgvfhxykzjw"*

First of all when we run the following program, we are asked for the message to decript.

> /usr/bin/python3.5 /home/izaya_orihara/PycharmProjects/ShiftCipher/Decipher.py
> Enter your message to decript: 

Then we are asked for our Dictionary to be either english or latin.
After we select our dictionary, the program will parse the message, search for the most common letter in our message and assume that this letter was the first letter in our dictionary but encrypted with shift.
At the end we see the result displayed on the screen with our decrypted message and we are asked if it was translated well enough, if we don't like the output we got, we just tell the program to run another  round of decryption but now the key will be the second symbol in our dictionaries, so the key will be again changed following the value of the next letter.
