#Email varification using string fuction
email= input("Enter your email address:")
k,j,d=0,0,0
#check email length
if len(email) >= 6:
    if email[0].isalpha(): #check 1st letter is alpha
       if ("@" in email) and (email.count("@")==1):#@ in email at first position
           if (email[-4]==".") ^ (email[-3]=="."): #check the "." position 
              for i in email:
                  if i== i.isspace(): #check space in email
                      k=1
                  elif i.isalpha(): #check latter is alpha
                      if i== i.upper(): #check 1st letter is upper case
                          j=1 
                  elif i.isdigit(): #check digit ,it is continue
                      continue
                  elif  i=="_" or i=="." or i=="@":
                      continue
                  else:
                      d=1 
              if k==1 or j==1 or d==1:
                          print("wrong email address 5")         
           else:
               print("wrong email address 4")
       else:
           print("wrong email address 3")

    else:
        print("wrong email address 2")

else:
    print("Wrong email address 1")