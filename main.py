#Encoding
st = input("Enter message: ") #input from the user
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      #if the length of the string is greater than or equal to 3 shift the first alphabet of the string in end and add random 3 alphabets at start and end of the string
      r1 = "zgh"
      r2 = "oph"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    #if the length of the word is less than 3 reverse the word
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
#Decoding
else:
  nwords = []
  for word in words:
    #if the length of the string is greater than or equal to 3 shift the last alphabet of the string at start and remove random 3 alphabets from the  start and end of the string
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))



