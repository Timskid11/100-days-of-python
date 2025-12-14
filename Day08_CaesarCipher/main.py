

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text,shift,direction):    
    if direction.lower() == "encode":
        def encrypt(text,shift):
           shifted_letter = ""
           for eachletter in text:
               if eachletter not in letters:
                   shifted_letter += eachletter
               else:
                  
                   eachlettershift = ((letters.index(eachletter)) + shift)
                   if eachlettershift >= 26:
                           eachlettershift -= 26
                           shifted_letter += letters[eachlettershift]                           
                           shifted_letter += letters[eachlettershift]
                   else:          
                       shifted_letter += letters[eachlettershift]
                       
           print(f"Here is the encoded result: {shifted_letter}")
               
        encrypt(text,shift)   
    elif direction.lower() == "decode":        
        def decrypt(text,shift):
            
                       
           shifted_letter = ""
           for eachletter in text:
               if eachletter not in letters:
                   shifted_letter += eachletter
               else:
                   
                   eachlettershift = (letters.index(eachletter)) - shift 
                   if eachlettershift <= 0:
                           eachlettershift += 25
                           shifted_letter += letters[eachlettershift]
                   else:          
                       shifted_letter += letters[eachlettershift]
                       
           print(f"Here is the decoded result: {shifted_letter}")       
        decrypt(text,shift)
    
    
        

