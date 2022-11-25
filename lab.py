""" 
          Star Cinema Hall Online Ticket Sell Management System
          Created By : Saif Tasnim Chowdhury
          Phitron Lab Mid Assignment Project
          Completed Date : 25 November, 2022
                  Stored In GitHub
             
 """

class Star_Cinema:
    _hall_list = []     # protected
    
    def entry_hall(self,rows,cols,hall_no) -> None:
    #   self.seats = {}
    #   self.show_list = list()
    #   self.rows = rows
    #   self.cols = cols
    #   self.hall_no = hall_no

     self._hall_list.append(rows)
     self._hall_list.append(cols)
     self._hall_list.append(hall_no)
  
    
    def print_Hall(self):
       print(self._hall_list)
    
    

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
      self.seats = {}
      self.show_list = list()
      self.rows = rows
      self.cols = cols
      self.hall_no = hall_no
      super().entry_hall(rows,cols,hall_no)
    

    def entry_show(self,id,movie_name,time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        self.tupple = self.id,self.movie_name,self.time
        self.show_list.append(self.tupple)
                                                           # self.total_seats = [[False]*self.cols]*self.rows
        
        self.total_seats =  [[False for i in range(self.cols)] for j in range(self.rows)]

        self.dict = {self.id : self.total_seats}
        self.seats.update(self.dict)
        # self.seats[self.id].append(self.total_seats)
        

      
    
    def book_seats(self,name,phone,show_id,seat_list):
        self.cus_show_id = show_id
        self.cus_name = name
        self.phone = phone
        self.seat_list = seat_list
        found = 0 
        flag = 0
        count = 0
        error_seat=[]
        for key,value in self.seats.items():
          if key == show_id:
            found = 1
            for i,j in enumerate(seat_list):
               row_n = j[0]
               col_n = j[1]
               try:
                 if value[row_n][col_n] == False:
                   flag = 1
                   count+=1
                   value[row_n][col_n] = True
                  
                 else:
                    # print(f'{row_n}{col_n} seat is already booked')
                    flag = 0 
                    tup = row_n,col_n
                    error_seat.append(tup)
               except:
                 print("\t\tInvalid Seats No\n")
        
        if len(error_seat) != 0:
          
           print(f'\t\tYour Selected seat {error_seat} are already booked for other customer. Please select empty seats\n\n') 
        
        elif flag > 0:
          print("\t\tCongratulations !!! You have booked " , count ," available tickets\n\n")    

        elif found==0:
          print("\t\t Invalid Show Id\n\n") 

                 
              
                


    def view_show_list(self):
      print("\n\n---------------------------------------------------------------------------------------------------------------------")
      print("\t\t\t\tWELCOME TO STAR CINEMA HALL NO -:  ",self.hall_no,"\n")
      print("\t\t\t\t\tRUNNING SHOWS ARE : \n\n")
      for i in range (3):
        print(f'\nSHOW ID  :  {self.show_list[i][0]}\t\tSHOW NAME  :  {self.show_list[i][1]}\t\tTIME :  {self.show_list[i][2]}\t\t')
    
      print("\n---------------------------------------------------------------------------------------------------------------------\n\n")


    
    def avalable_seats(self,show_id):
      found = 0
      print("\n---------------------------------------------------------------------------------------------------------------------")
      print("\t\t\t\tWELCOME TO STAR CINEMA HALL NO -:  ",self.hall_no,"\n\n")
      for i in range (3):
        if show_id == self.show_list[i][0]:
          print("MOVIE NAME : " , self.show_list[i][1] , "\t\t TIME :  ",self.show_list[i][2], "\nX for already booked seats\n")
    
          for key,value in self.seats.items():
             if key == show_id:
               found = 1
               for i in range(self.rows):
                 for j in range(self.cols):
                   if value[i][j] == False:
                     print(f'{i}{j}',end="\t")
                   else:
                      print('X',end="\t")
                 print();                
            
        if found == 0 :
         print("\tShow Id is incorrect. Enter correct Id\n")

     

    
      print("\n---------------------------------------------------------------------------------------------------------------------\n\n")






hall_1 = Hall(4,5,1)

# hall_1.print_Hall()
hall_1.entry_show("st101" , "The Jungle Book","12th June 2022 , 10:30 AM")
hall_1.entry_show("st102" , "Hawa\t","13th June 2022 , 12:00 PM") 
hall_1.entry_show("st103" , "Mission Sundarban","14th June 2022 , 4:00 PM")
print("\n\n\t\t\t\tWELCOME TO STAR CINEMA\n")
print('\t\t\t\t\tHALL NO : 1\n\n')

a = 1
while a != 0:
    print('1. VIEW ALL SHOWS')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK SEATS\n')
    print('ENTER OPTION : ')
    a = int(input())
    if a ==1:
       hall_1.view_show_list()
    
    elif a == 2:

       hall_1.avalable_seats(input('ENTER SHOW ID : '))

    elif a == 3:
        seat_list=[]
        seat_tupple=()
        show_id = input('Enter Show Id :  ')
        name = input('Enter Customer Name :  ')   
        phone = input('Enter Phone Number :  ')
        seat = int(input('Enter Number Of Tickets :  '))
        for i in range(seat):
          n = input('Enter Seat No :  ')
          numbers = [int(i) for i in n]
          row = numbers[0]
          col = numbers[1]
          # row,col = input('Enter Seat No  (Please Select this format -> row no colum no) :  ').split("")
          seat_tupple = row,col
        
          seat_list.append(seat_tupple)
        
        

        hall_1.book_seats(name,phone,show_id,seat_list)
      


    else:
        print("WRONG CHOICE !!")
        print("ENTER YOUR CHOICE AGAIN :")








