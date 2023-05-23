import os
Vendor_or_customer = int(input("Press 1 if you are a vendor and press 2 if you are the customer:\n"))
#vendor signup and login
if Vendor_or_customer==1:
   decision = int(input("Press 1 to signup and 2 to login:\n"))
   if decision==1:
       Namevendor = input("Enter your name:\n")
       vendor_email = input("Enter your email:\n")
       national_id = input("Enter your national ID:\n")
       # checker if it's a real phone number containning 11 digits
       vendor_number = input("Enter your phone number:\n")
       # A program for a password generator should be here
       vendor_password = input("Enter a strong password:\n")
       vendor_data = open(r"C:\Users\Aya\pythonProject2\Vendor"+r"\\"+Namevendor+".txt", "w+")
       vendor_data_list = [Namevendor, " - ", vendor_email, " - ", vendor_number, " - ", national_id, " - ", vendor_password]
       vendor_data.writelines(vendor_data_list)
       vendor_data.close()
   else:
       vendor_name = input("Enter your name:")
       vendor_data = open(r"C:\Users\Aya\pythonProject2\Vendor"+r"\\"+vendor_name+".txt", "r+")
       email_v = input("Enter your email")
       password_v = input("Enter your password")
       if (email_v in open(r"C:\Users\Aya\pythonProject2\Vendor"+r"\\"+vendor_name+".txt").read()) and (password_v in open(r"C:\Users\Aya\pythonProject2\Vendor"+r"\\"+vendor_name+".txt").read()):
           print("You've logged in successfully")
      Add_remove_see=int(input("to add movies press 1, to remove movies press 0, to see customer who booked the movies press 2"))# Vendor adding movies
   if (Add_remove_see==1):
      print("to add movie")
      number_of_movies = int(input("enter the number of movies you wants to add:"))
      x = 1
      while x <= number_of_movies:
         title = input("enter movie's title:")
         movie_id = input("enter movie's id:")
         movie_des = input("enter movie's describtion:")
         available_seats_num = int(input("enter the number of available seats:"))
         customers_booked1 = open(r"C:\Users\Aya\pythonProject2\customers who booked movies"+r"\\"+title + "customer file.txt", "w+")
         customers_booked1.write(str(0))
         customers_booked1.close()
         booked_seats = open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+title + "booked seats.txt", "w+")-
         for x in range(1,2):
            if x ==1:
              booked_seats.write(str(0))
              break
         booked_seats.close()
         seats_num_file=open(title+"seats_num.txt","w")
         titles_only_title = open(r"C:\Users\Aya\pythonProject2\Titles"+r"\\"+title + "title.txt", "w")
         titles_only_title.write(title)
         seats_num_file.write(str(available_seats_num))
         seats_num_file.close()
         movie_file_details = open(title + ".txt", "w")
         movie_file_details.writelines("the movie's id :" + movie_id + "\n" + "the movie's description: " + movie_des + "\n" + "available seats:")
         movie_file_details.close()
         movie_file_details.close()
         titles_only_title.close()
         x+=1
      else:
         print("This data doesn't exist; you maybe need to sign up first")
         vendor_data.close()
   elif (Add_remove_see == 0):
      directory = r'C:\Users\Aya\pythonProject2\Titles'
      for filename in os.scandir(directory):
         if filename.is_file():
            title_n = open(filename.path, "r+")
            read_title = title_n.readline()
            seats_num_file = open(read_title+"seats_num"+".txt","r+")
            seats = seats_num_file.readline()
            seats_int = int(seats)
            booked = open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+read_title+"booked seats"+".txt", "r+")
            length_booked = len(booked.readlines())
            title_n.close()
            if ((seats_int+1)==length_booked):
               print("You should remove this movie\t"+read_title)
               remove = int(input("Enter 1 to remove it or 0 to exit"))
               if remove == 1:
                  title = input("Enter movie title:")
                  os.remove(r'C:\Users\Aya\pythonProject2\Titles'+r"\\"+title+ "title.txt")
               else:
                  break
   else:
       booked_search = int(input("Enter 1 if you want to see all customer booked list and press 2 if you want to search about only one movie's list:\n"))
       if booked_search ==1:
         customers_directory = r'C:\Users\Aya\pythonProject2\customers who booked movies'
         for filename in os.scandir(customers_directory):
          if filename.is_file():
           customer_name = open(filename.path,"r+")
           print(customer_name.readline())       
           customer_name.close()
       else:
         booked_name = input("Enter the movie title")
         booked_name_file = open(r"C:\Users\Aya\pythonProject2\customers who booked movies"+r"\\"+booked_name+"customer file"+".txt","r+")
         print(booked_name_file.readlines())
else: #customer section
   sign = input(r"Have you signed in? (yes\no)")
   if sign =='no':
           print("Please sign up")
           name = input("Enter your name")
           user_email = input("Enter your email: ")
           national_id = input("Enter your national ID: ")
        # checker if it's a real phone number containning 11 digits
           user_number = input("Enter your phone number: ")
        # A program for a password generator should be here
           user_password = input("Enter a strong password: ")
           user_data = [name, " - ", user_email, " - ", user_number, " - ", national_id, " - ", user_password]
           folder=os.mkdir(name) #create folder for each customer
           namefolder_path = r"C:\Users\Aya\pythonProject2\Customers"
           name_name_folder = namefolder_path+r"\\"+name
           name_folder=os.mkdir(name_name_folder)
           file_info = name_name_folder+r"\\"+name+".txt" #create file for each customer in his folder
           file_info_file = open(file_info,"w+") #open the file
           file_info_file.writelines(user_data) #write_seat_num user's data in it
           file_info_file.close()
        #user log in
           print("After you signed up, please log in")
           file_info_file = open(file_info, "r")
           email = input("Enter your email")
           password = input("Enter your password")
           if(email in open(file_info).read() and password in open(file_info).read()):
              print("You've logged in successfully")
              directory = r'C:\Users\Aya\pythonProject2\Titles'
              for filename in os.scandir(directory):
                   if filename.is_file():
                      title_n = open(filename.path,"r+")
                      print(title_n.readline())
                      title_n.close()
           title=input("to search about movie enter his title:")
           movie_file=open(title+".txt","r")
           title=input("please enter the title of movie:")
           seats_num_file = open(title + "seats_num.txt", "r+")
           only_number = seats_num_file.read()
           only_number_int = int(only_number)6
           available_seats=[]
           counter=0
           while (counter<=only_number_int):
             available_seats.append(counter)
             counter+=1
           booked_seats= open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+title+"booked seats.txt", "r+")
           booked_seats.seek(0)
           lines = booked_seats.readlines()
           n=len(lines)
           booked_seats.seek(0)
           for i in range(1, n + 1):
             only_number=booked_seats.readline()
             print(int(only_number))
             available_seats.remove(int(only_number))
           booked_seats.close()
           seats_num_file.close()
           print(movie_file.read())
           print(available_seats)
            # boooking#################################################################################
           print("to send book request")
           customer_name=input("please enter your name:")
           customer_id=input("please enter your id:")
           movie_name=input("please enter movie name:")
           movie_id = input("please enter movie id:")
           seat_number =int(input("please enter seat number:"))
           if(movie_id in open(movie_name+".txt").read()):
               booked_seats_file=open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+movie_name+"booked seats.txt","a+")
               booked_seats_file.write("\n"+str(seat_number))
               booked_seats_file.close()
               customers_booked=open(r"C:\Users\Aya\pythonProject2\customers who booked movies"+r"\\"+movie_name+"customer file.txt","a+")
               customers_booked.write(customer_name+" "+movie_name)
               customers_booked.write("\n")
               customers_booked.close()
               print("you booked successfuly")
               print("Your ticket is:\n")
               print(seat_number,movie_name)
            #movies_list
   elif sign =='yes':
            # user log in
            print("After you've signed in, please log in: ")
            name = input("Enter your name: ")
            email = input("Enter your email")
            password = input("Enter your password")
            namefolder_path = r"C:\Users\Aya\pythonProject2\Customers"
            file_info = namefolder_path + r"\\" + name + r"\\" + name + ".txt"
            file_info_file = open(file_info, "r")
            if (email in open(file_info).read() and password in open(file_info).read()):
               print("You've logged in successfully")
               directory = r'C:\Users\Aya\pythonProject2\Titles'
               for filename in os.scandir(directory):
                 if filename.is_file():
                   title_n = open(filename.path,"r+")
                   print(title_n.readline())
                   title_n.close()
               title=input("to search about movie enter his title:")
               movie_file=open(title+".txt","r")
               title_input=input("please enter the title of movie:")
               seats_num_file = open(title_input + "seats_num.txt", "r+")
               only_number = seats_num_file.read()
               only_number_int = int(only_number)
               available_seats=[]
               counter=0
               while (counter<=only_number_int):
                  available_seats.append(counter)
                  counter+=1
               booked_seats= open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+title+"booked seats.txt", "r+")
               booked_seats.seek(0)
               lines = booked_seats.readlines()
               n=len(lines)
               booked_seats.seek(0)
               for i in range(1, n + 1):
                  only_number=booked_seats.readline()
                  print(int(only_number))
                  available_seats.remove(int(only_number))
               booked_seats.close()
               seats_num_file.close()
               print(movie_file.read())
               print(available_seats)
            # boooking#################################################################################
               print("to send book request")
               customer_name=input("please enter your name:")
               customer_id=input("please enter your id:")
               movie_name=input("please enter movie name:")
               movie_id = input("please enter movie id:")
               seat_number =int(input("please enter seat number:"))
               if(movie_id in open(movie_name+".txt").read()):
                  booked_seats_file=open(r"C:\Users\Aya\pythonProject2\Movies booked seats"+r"\\"+movie_name+"booked seats.txt","a+")
                  booked_seats_file.write("\n"+str(seat_number))
                  booked_seats_file.close()
                  customers_booked=open(r"C:\Users\Aya\pythonProject2\customers who booked movies"+r"\\"+movie_name+"customer file.txt","a+")
                  customers_booked.write(customer_name+" "+movie_name)
                  customers_booked.write("\n")
                  customers_booked.close()
                  print("you booked successfuly")
                  print("Your ticket is:\n")
                  print(seat_number,movie_name)