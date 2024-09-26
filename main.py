print('''==================================================\n\t\tWelcome to RIKU library.
==================================================''')
bk=["PHYSICS\t","CHEMISTRY","MATHEMATICS","ENGLISH","COMPUTER"]
auth=["HC VERMA","DINESH","RD SHARMA","RUSKIN BOND","SUMITA ARRORA"]
bk_id=['0000','1111','2222','3333','4444']
p=["0001","0002","0003","0004","0005"]
re=['0000','1111','2222','3333','4444']
name=["KUNAL","ROHIT","UTKARSH","ASHU","VIVEK"]
q="Thank You, Have a Nice Day."
le_li=[];le_bk=[]
dt_le=[];le_id=[]

pw='lib1234'

con=True

while con==True:
     print("""(1).Display books in lib.\t\t(2).Lend a book\n(3).Addition of book\t\t\t(4).Returning book\n(5).Search book in lib. \t\t(6).Delete a Book\n(7).Register a Person\t\t\t(8).Remove registered person\n(9).Display list of registry\t\t(10).Lender's list\n(11).Change password""")

     user_input=(input("Enter your choice:"))
     if user_input=='1':                                             #Displaying Books
          print('Book ID\t\tBooks\t\t\tAuthor\t\t')
          ad=0
          for i in bk:
               print(bk_id[ad],'\t\t',bk[ad],'\t\t',auth[ad],)
               ad+=1
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
               print(q)
               break
          elif user_choice=='c':
               continue
     elif user_input=='2':                                            #Lending Book
          print("Administrator Password is required for this action")
          password=''
          while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")
          reg=input("Enter the registration no. to be searched:")
          reg=reg.upper()
          if reg in p :
               idp=p.index(reg,0,len(p))
               print(dict(regno=reg,idp=name[idp]),"is found")
               lend_id=input("Enter the Book ID:")
               lend_bk=input("Enter the name of the book that you want to lend:")
               lb=lend_bk.upper()
               lend_auth=input("Enter the name of the author of the book:")
               la=lend_auth.upper()
               lend_nm=input("Enter your name:");lend_nm=lend_nm.upper()
               rtrn_date=input("Enter the date of returning the book(dd/mm/yyyy):")
               if lb in bk and la in auth and lend_id in bk_id:
                   print(lend_nm,"has lended",lend_bk,",and will return it by,",rtrn_date)
                   bk_id.remove(lend_id)
                   bk.remove(lb)
                   auth.remove(la)
                   le_li.append(lend_nm)
                   dt_le.append(rtrn_date)
                   le_bk.append(lb)
                   le_id.append(lend_id)
               else:
                   print("This book is not avilable in the library.")
          else:
             print("Registration number not found")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
               print(q)
               break
          elif user_choice=='c':
               continue
     elif user_input=='3':                                                  #Adding Book
          print("Administrator Password is required for this action:")
          password=''
          while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")    
          qnt=int(input("Enter no. of books to be added:"))
          for i in range(qnt):
               new_id=input("Enter the Book id:")
               new_bk=input("Enter the name of the new book:");nb=new_bk.upper()
               new_auth=input("Enter the name of the author of new book:");na=new_auth.upper()
               bk_id.append(new_id)
               re.append(new_id)
               bk.append(nb)
               auth.append(na)
               print("The book has been added successfully!")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
               print(q)
               break
          elif user_choice=='c':
               continue
     elif user_input=='4':                                                       #Return Book
         qnt=int(input("Enter no. of books you want to return:"))
         for i in range(qnt):
               rtrn_id=input("Enter Book id:")
               if rtrn_id in re:
                    rtrn_reg=input("Enter registration number:")
                    rtrn_nm=input("Enter your name:");rtrn_nm=rtrn_nm.upper()
                    rtrn_bk=input("Enter the name of the book:");rtrn_bk=rtrn_bk.upper()
                    rtrn_auth=input("Enter the name of the author of book:");ra=rtrn_auth.upper()
                    bk_id.append(rtrn_id)
                    bk.append(rtrn_bk)
                    auth.append(ra)
                    ix=le_id.index(rtrn_id,0,len(le_id))
                    dt_le.remove(dt_le[ix])
                    le_id.remove(rtrn_id)
                    le_bk.remove(rtrn_bk)
                    le_li.remove(rtrn_nm)
                    print("You returned the book successfully!")
               else:
                    print("This book does not belog to this library,")
         user_choice=input("Enter any key to Continue or q to Quit:")
         if user_choice=="q":
               print(q)
               break
         elif user_choice=='c':
               continue
     elif user_input=='5':                                                 #Searching of a book
          sbk=input("Enter the book name to be searched:")
          sbk=sbk.upper()
          if sbk in bk :
               idx=bk.index(sbk,0,len(bk))
               print(dict(Book_ID=bk_id[idx],Book=sbk,Author=auth[idx]),"is available in the library.")
          else:
               print("This doesn't match with any of our books")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
               print(q)
               break
          elif user_choice=='c':
               continue
     elif user_input=='6':                                                     #Deletion of a book
          print("Administrator Password is required for this action")
          password=''
          while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")
          dlt=int(input("Enter the no.of books you want to delete:"))
          for i in range(dlt):
               del_id=input("Enter the book id:")
               if del_id in bk_id:
                    del_bk=input("Enter the name of the book:");del_bk=del_bk.upper()
                    del_auth=input("Enter the name of the author of book:");del_auth=del_auth.upper()
                    bk_id.remove(del_id)
                    re.remove(del_id)
                    bk.remove(del_bk)
                    auth.remove(del_auth)
                    print("Books deleted sucessfully !")
               else:
                    print("Book not found!")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
               print(q)
               break
          elif user_choice=='c':
               continue
     elif user_input=='7':                                                   #Registeration of a person
          print("Administrator Password is required for this action!")
          password=''
          while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")
          test=int(input("Enter no. of person to be registered"))
          for i in range(test):
              new_reg=input("Enter the new reg.no. :")
              new_name=input("Enter the name of person:")
              new_name=new_name.upper() 
              p.append(new_reg)
              name.append(new_name)
              print(new_name,'registered successfully!')
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
              print(q)
              break
          elif user_choice=='c':
              continue
     elif user_input=='8':                                                 #Removing registory
          print("Administrator Password is required for this action!")
          password=''
          while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")
          rev=int(input("Enter the no.of registry to be removed:"))
          for i in range(rev):
               del_p=input("Enter the Registration no. :")
               if del_p in p:
                    del_name=input("Enter the name of the Registered person:")
                    del_name=del_name.upper()
                    p.remove(del_p)
                    name.remove(del_name)
               else:
                    print(del_p,"has not registered yet!")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
              print(q)
              break
          elif user_choice=='c':
              continue
     elif user_input=='9':                                                 #List of registry
         print("Administrator Password is required for this action!")
         password=''
         while password!=pw:
               password=input("Enter password:")
               if password==pw:
                    break
               else:
                    print("wrong password")
         print('Reg no.\t\t\tName')
         ln=0
         for i in p:
             print(i,name[ln],sep="\t\t\t")                          #Error
             ln+=1
         user_choice=input("Enter any key to Continue or q to Quit:")
         if user_choice=="q":
             print(q)
             break
         elif user_choice=='c':
             continue
     elif user_input=='10':                                                   #Lender's list
          print("Here is the lender's list:")
          print("Reg no.\t\tName\t\tDate of returning\t\tBook lended\t\tBook id")
          le=0
          for i in le_li:
               print(p[le],i,dt_le[le],le_bk[le],le_id[le],sep="\t\t")
               le+=1
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
             print(q)
             break
          elif user_choice=='c':
             continue
     elif user_input=='11':                                                #Change password
          o_pw=input("Enter the old password:")
          n_pw=''
          if o_pw==pw:
               n_pw=input("Enter new password:")
               pw=n_pw
               print("New password updated, successfuly!")
          else:
               print("Sorry!,wrong paasword.")
          user_choice=input("Enter any key to Continue or q to Quit:")
          if user_choice=="q":
             print(q)
             break
          elif user_choice=='c':
             continue
     elif user_input>'11' or user_input<'1':                                 #wrong input
          print("Wrong choice.Please choose the option from below")
          continue