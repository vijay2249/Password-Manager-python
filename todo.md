
## 𝐎𝐮𝐭𝐥𝐢𝐧𝐞 
  - 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐋𝐢𝐧𝐞 𝐈𝐧𝐭𝐞𝐫𝐟𝐚𝐜𝐞
  - Take master password validate and show/save entries 
  - Automatically copy password to clipboard 
  - Generate random password (alphabets, numbers and special chars)

Implementation

## 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞
  - MASTER PASSWORD is first inputted while configuring, and the hash of it is saved in a file  
  - DEVICE SECRET is generated randomly, also stored in a file MASTED PASSWORD DEVICE SECRET is passed 
    into to a hashing function (pbkdf) to create a valid key for AES-256. This is called Master Key.
  - The Master Key is then used to encrypt/decrypt new entries.
  - Encrypted fields : email, username, password 
  - Plain fields : sitename, url

## 𝐀𝐝𝐝 𝐧𝐞𝐰 𝐞𝐧𝐭𝐫𝐢𝐞𝐬
  - Ask for MASTER PASSMORD
  - Validate MASTER PASSWORD by hashing and checking with existing hash
  - Make hash (DEVICE SECRET + MASTER PASSWORD) = Master Key 
  - Input fields of the entry- site name, site url, mail, username, password
  - Encrypt email, username and password with MASTER KEY and save the fields into the database

## 𝐆𝐞𝐭 𝐞𝐧𝐭𝐫𝐲
  - Input the field to search for. Like site name, site url, email, username 
  - Display all the entries that match the search.Password hidden by default.  
  - If user chooses to get the password (with -p flag), then 
  - Ask for MASTER PASSWORD Decrypt the password and copy to the clipboard
  - Validate MASTER PASSWORD by hashing and checking with existing hash Make hash(DEVICE SECRET MASTER PASSMORD) Master Key
  - Make hash (DEVICE SECRET + MASTER PASSWORD) = Master Key
  - Decrypt the password and copy it to clipboard