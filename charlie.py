import zipfile

zip_file = 'enc.zip'

wordlist = 'rockyou.txt'

with open(wordlist, 'r', encoding='latin-1') as file:
    passwords = file.readlines()

zip = zipfile.ZipFile(zip_file)

for password in passwords:
    try:
        zip.extractall(pwd=bytes(password.strip(), 'utf-8'))
        print(f'Password found: {password.strip()}')
        break
    except:
        continue

print('Password not found in wordlist.')
