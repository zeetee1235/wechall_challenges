# 	Training: Crypto - Caesar I by Gizmore

code = input("Enter the code:")
abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
decrypted_messages  =  []

key = 1 #해독할때 사용할 key값

def decrypt(data):
    global key
    global abc
    global decrypted_messages
    decrypted_message = ""
    data_length = len(data)
    
    for i in range(0, data_length):
        if data[i] in abc:
            chr_num = abc.index(data[i]) + key
            if chr_num > 25:
                chr_num -= 26
            decrypted_message += abc[chr_num]
        else:
            decrypted_message += " "
            
    decrypted_messages.append(decrypted_message)
    key += 1
            
for i in range(0 , 25):
    decrypt(code)

#결과출력
for i in range(0, len(decrypted_messages)):
    print(decrypted_messages[i])

