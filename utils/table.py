class Seat:
    def __init__(self,  free=True , occupant=""):
        self.free= free 
        self.occupant=occupant 

    def seat_occupant(self, name):
        if self.free:
           self.occupant=name 
           self.free=False
           print(f'this seat is occupied by : {name}')
        else :
            print(' this seat is occupied before ')
    def remove_occupant(self):
         if not self.free :
             before=self.occupant
             self.occupant= " " 
             self.free=True
             print (f'this seat occupied by  {before} now it is free now ')
             return before
         else:
             print ('This seat is already free')
             return 
class Table:
    def __init__(self, capacity:int ):
        self.capacity=capacity
        self.seats = []
        for  i  in range(capacity):
            self.seats.append(Seat())  # that means if the capacit is 4 so it creat list with 4 seat class self.seats=[Seat(),Seat(),Seat(),Seat()]
        

    def has_free_spot(self ) -> bool : #that returns a boolean (True if a spot is available)
        for s_spot  in self.seats:     # s_spot is a seat in  list seats 
            if s_spot.free :           # for the seat look if the attribute free is true or false 
              return True 
        return False 

    def assign_seat(self , name): #that places someone at the table
        if self.has_free_spot( ):   # checks if there is at least one free seat in the table
           for s_spot in self.seats:   # this loop to find the specific seat is free to put the person there.
               if s_spot.free:
                  s_spot.seat_occupant(name) #put the person there and mark the seat as occupied
                  return True
        else: 
            print ("no more free seats on the table ")
            return False

    def left_capacity(self ) -> int :# Go through the list of seats (self.seats)Check if each seat is free Count how many are free , returns an integer
       free_s_count=0
       for s_spot in  self.seats:
           if s_spot.free:
                free_s_count+=1
       return free_s_count 
