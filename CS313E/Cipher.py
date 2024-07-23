
import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
        # L = length of str, M = closest square value
        # add M-L asterisks to list
        # fill into into KxK matrix where K^2=M
        L = len(strng)
        M = (math.ceil(math.sqrt(L)))**2
        K = math.ceil(math.sqrt(L))
        
        ast_count = M - L
        asterisks = "*" * ast_count
        tot_string = strng + asterisks

        array = [[0]*K for i in range(K)]
        count = 0
               
        for rows in range(0,K):
                for cols in range(0,K):
                        array[rows][cols] = tot_string[count]
                        count+=1

        flip_array = []
        rot_array = []
        
        #array flip
        for i in range(K-1,-1,-1):
                new_row = array[i]
                flip_array.append(new_row)
                
        for i in range(0,K):
                new_row = [row[i] for row in flip_array]
                rot_array.append(new_row)
      
        #final cipher is a string in the order of rot_array

        flat = list(item for row in rot_array for item in row)
        cipher = str()
        for letter in flat:
                if letter != "*":
                        cipher += str(letter)
                else:
                        continue
        return(cipher)


	#pass

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
        L = len(strng)
        M = (math.ceil(math.sqrt(L)))**2
        K = math.ceil(math.sqrt(L))

        ast_count = M - L
        asterisks = "*" * ast_count
        tot_string = strng + asterisks
        
        coded_array = [[0]*K for i in range(K)]
        count = 0

        for rows in range(0,K):
                for cols in range(0,K):
                        coded_array[rows][cols] = tot_string[count]
                        count+=1
        #switch asterisks from end of last row to front
        switch_row = coded_array[3]
        #remove asterisks and add them back in front
        switch_row = list(asterisks) + [item for item in switch_row if item!="*"]
        coded_array[3] = switch_row

        #rotates and then flips array to decode
        flip_array = []
        rot_array = []

        for i in range(0,K):
                new_row = [row[i] for row in coded_array]
                rot_array.append(new_row)

        for i in range(K-1,-1,-1):
                new_row = rot_array[i]
                flip_array.append(new_row)

        #convert array to string        
        flat = list(item for row in flip_array for item in row)
        decipher = str()
        for letter in flat:
                if letter != "*":
                        decipher += str(letter)
                else:
                        continue
        return(decipher)
                
        
	#pass

def main():
        code = encrypt("gonewiththewind")
        decrypt(code)
  # read the strings P and Q from standard input

  # encrypt the string P

  # decrypt the string Q

  # print the encrypted string of P
  # and the decrypted string of Q
if __name__ == "__main__":
        main()



