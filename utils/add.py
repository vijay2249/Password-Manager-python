from utils.dbconfig import dbconfig
import utils.aesutil
from getpass import getpass

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

import random
import string

from rich import print as printc
from rich.console import Console

def generatePassword (passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
    #generating characters, numbers and letters for password
    passwordList = []
    #password list is for putting all the selected password units into a string and show them to user
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)

    finalOutput = "".join(passwordList)
    return finalOutput

def computeMasterKey(mp,ds):
	password = mp.encode()
	salt = ds.encode()
	key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key


def checkEntry(sitename, siteurl, email, username):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM pm.entries WHERE sitename = '{sitename}' AND siteurl = '{siteurl}' AND email = '{email}' AND username = '{username}'"
	cursor.execute(query)
	results = cursor.fetchall()

	if len(results)!=0:
		return True
	return False


def addEntry(mp, ds, sitename, siteurl, email, username):
	# Check if the entry already exists
	if checkEntry(sitename, siteurl, email, username):
		printc("[yellow][-][/yellow] Entry with these details already exists")
		return

	Yass = input("Do you want me to generate Password! \nType y/N: ")
	# Input Password
	if(Yass == "N"):
		password = getpass("Password: ")
	
	else:
		print('hello, Welcome to Password generator!')
		length = int(input('\nEnter the length of password: '))
		password = generatePassword(length)

	# compute master key
	mk = computeMasterKey(mp,ds)

	# encrypt password with mk
	encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")

	# Add to db
	db = dbconfig()
	cursor = db.cursor()
	query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
	val = (sitename,siteurl,email,username,encrypted)
	cursor.execute(query, val)
	db.commit()

	printc("[green][+][/green] Added entry ")
