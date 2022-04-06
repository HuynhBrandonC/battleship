#random module for ai
import random

#pieces that you are able to place
valid_pieces = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']

#directions you are able to go
valid_dir = ['down', 'up', 'right', 'left']

#how many spaces each ship can take
ship_length = {'carrier_length' : 5,
'battleship_length' : 4,
'cruiser_length' : 3,
'submarine_length' : 3,
'destroyer_length' : 2}

#how many of each ship you have
ship_amount = {'carrier_amount': 1,
'battleship_amount': 1,
'cruiser_amount': 0,
'submarine_amount': 0,
'destroyer_amount': 0}



#place holder for hits_needed
hits_needed = 0

#loops through keys in ship_length dictionary
for key in ship_length:
    #gets the type of ship by splitting by _
    ship_type = key.split('_')
    #gets length of the ship
    length = ship_length.get(key)
    #gets amount of the ships and multiplies by the length in case you want to change the amount of ships you have later
    length = length * ship_amount.get(ship_type[0]+'_amount')
    #adds the amount of spaces by all ships to the amount of hits you need to win
    hits_needed += length

#class to create 2 sep grids that are independent
class grids():
    #setting up the grid for each player, their personal amount of ships they have, how many they have placed, and if they have all placed down



    '''Program Code Data Collection Start'''


    def __init__(self):
        #base grid for the battleship
        self.grid = [[' ','1','2','3','4','5','6','7','8','9','10']
,['1','_','_','_','_','_','_','_','_','_','_']
,['2','_','_','_','_','_','_','_','_','_','_']
,['3','_','_','_','_','_','_','_','_','_','_']
,['4','_','_','_','_','_','_','_','_','_','_']
,['5','_','_','_','_','_','_','_','_','_','_']
,['6','_','_','_','_','_','_','_','_','_','_']
,['7','_','_','_','_','_','_','_','_','_','_']
,['8','_','_','_','_','_','_','_','_','_','_']
,['9','_','_','_','_','_','_','_','_','_','_']
,['10','_','_','_','_','_','_','_','_','_','_']]



        '''Program Code Data Collection End'''



        #how many of each ship you have
        self.ship_amount = {'carrier_amount': 1,
'battleship_amount': 1,
'cruiser_amount': 0,
'submarine_amount': 0,
'destroyer_amount': 0}
        #how many ships placed
        self.how_many_placed = 0
        #if all ships are placed
        self.all_placed = False
        #how many battleships have been hit
        self.battleships_hit = 0
        #if the game is over or not
        self.game_over = False


    '''Program Code Output Start'''


    #doesn't really update the grid just prints it out
    def update_grids(self) -> int:
        print('')
        
        if self == p1:
            print('player 1 grid:')
        elif self == p2:
            print('player 2 grid:')
        for n in self.grid:
            print(n)

        print('')

        return 0 #some trouble with pylance, had to add a return type to solve it
    

    '''Program Code Output End'''




    '''Program Code Procedure Start'''


    #method to place a piece
    def place_piece(self, piece):
        global carrier_length
        global battleship_length
        global cruiser_length
        global submarine_length
        global destroyer_length
        global valid_dir
        global valid_pieces

        #reset the valid directions each time it runs 
        valid_dir = ['down', 'up', 'right', 'left']


        '''Program Code input Start'''

        if self == p1:
        #loop for data validation
            while True:
                #first question that asks where you want to place the beginning of the piece, reloops to this if data validation fails
                first_spot = input('\nWhere do you want to place the beginning of the {0}? (State the row first and column second ex. "4 6")\n'.format(piece))
                #splits the answer into 2 sep pieces, the x and y coordinates
                first_spot_list = first_spot.split()

                '''Program Code input End'''


                #tests to see if the numbers put in are numbers, and if there are two numbers put in, if not reloops
                if first_spot_list[0].isnumeric() == True and first_spot_list[1].isnumeric() == True and len(first_spot_list) == 2:
                    #checks to see if the two numbers are inside the grid, if not reloops
                    if (int(first_spot_list[0]) < 11 and int(first_spot_list[0]) > 0 and int(first_spot_list[1]) < 11 and int(first_spot_list[1]) > 0):
                        #checks to see if where you are placing the beginning is already taken, if it is, reloop
                        if self.grid[int(first_spot_list[0])][int(first_spot_list[1])] != 'X':
                            break
        
        if self == p2:
            while True:
                first_spot_list = [str(random.randint(1,10)), str(random.randint(1,10))]
                if first_spot_list[0].isnumeric() == True and first_spot_list[1].isnumeric() == True and len(first_spot_list) == 2:
                        #checks to see if the two numbers are inside the grid, if not reloops
                    if (int(first_spot_list[0]) < 11 and int(first_spot_list[0]) > 0 and int(first_spot_list[1]) < 11 and int(first_spot_list[1]) > 0):
                        #checks to see if where you are placing the beginning is already taken, if it is, reloop
                        if self.grid[int(first_spot_list[0])][int(first_spot_list[1])] != 'X':
                            break



        '''Program Code Algorithm Start'''


        while True:
            #checks to see if a piece can not go a certain direction based on the grid border
            if int(first_spot_list[1]) > 11 - ship_length.get(piece+'_length'):
                valid_dir.pop(valid_dir.index('right'))
            if int(first_spot_list[1]) < 0 + ship_length.get(piece+'_length'):
                valid_dir.pop(valid_dir.index('left'))
            if int(first_spot_list[0]) < 0 + ship_length.get(piece+'_length'):
                valid_dir.pop(valid_dir.index('up'))
            if int(first_spot_list[0]) > 11 - ship_length.get(piece+'_length'):
                valid_dir.pop(valid_dir.index('down'))
            #checks to see if a piece can not go a certain direction base on if a spot is already taken
            for i in range(0, ship_length.get(piece+'_length'), 1):
                if 'up' in valid_dir:                
                    if self.grid[int(first_spot_list[0]) - i][int(first_spot_list[1])] == 'X':
                        valid_dir.pop(valid_dir.index('up'))
                if 'down' in valid_dir:
                    if self.grid[int(first_spot_list[0]) + i][int(first_spot_list[1])] == 'X':
                        valid_dir.pop(valid_dir.index('down'))
                if 'left' in valid_dir:
                    if self.grid[int(first_spot_list[0])][int(first_spot_list[1]) - i] == 'X':
                        valid_dir.pop(valid_dir.index('left'))
                if 'right' in valid_dir:
                    if self.grid[int(first_spot_list[0])][int(first_spot_list[1]) + i] == 'X':
                        valid_dir.pop(valid_dir.index('right'))
            #if the place checks through the direction checks then you can pick a direction
            if self == p1:
                dir = input('\nWhich direction do you want to place the {0} ({1})\n'.format(piece, valid_dir))
                # only can put it in a certain direction that is available, if invalid direction it reloops
                if dir in valid_dir:
                    break
            if self == p2:
                dir = random.choice(valid_dir)
                if dir in valid_dir:
                    break


                '''Program Code Algoirthm End'''



        #if statements that check which direction you picked and places the corresponding amounbt of spaces of the piece you picked in that direction
        if dir == 'up':
            for i in range(0, ship_length.get(piece+'_length'), 1):
                self.grid[int(first_spot_list[0]) - i][int(first_spot_list[1])] = 'X'
        if dir == 'down':
            for i in range(0, ship_length.get(piece+'_length'), 1):
                self.grid[int(first_spot_list[0]) + i][int(first_spot_list[1])] = 'X'
        if dir == 'left':
            for i in range(0, ship_length.get(piece+'_length'), 1):
                self.grid[int(first_spot_list[0])][int(first_spot_list[1]) - i] = 'X'
        if dir == 'right':
            for i in range(0, ship_length.get(piece+'_length'), 1):
                self.grid[int(first_spot_list[0])][int(first_spot_list[1]) + i] = 'X'






                
        #sets whatever ship you picked to 1 less
        self.ship_amount[piece+'_amount'] -= 1


        '''Program Code Procedure End'''


    def test(self):
        print(self.grid)

    #method that places all pieces
    def place_pieces(self):
        global carrier_length
        global battleship_length
        global cruiser_length
        global submarine_length
        global destroyer_length
        global valid_dir
        global valid_pieces

        #loop
        while True:
            #asks you which piece you want to place, how many you have left, and how many spaces it takes up
            if self == p1:
                self.piece = input('Do you want to place a carrier ({0} left) (5 spaces), battleship ({1} left) (4 spaces), cruiser ({2} left) (3 spaces), submarine ({3} left) (3 spaces), or destroyer ({4} left) (2 spaces)?\n\n'.format(self.ship_amount.get('carrier_amount'), self.ship_amount.get('battleship_amount'), self.ship_amount.get('cruiser_amount'), self.ship_amount.get('submarine_amount'), self.ship_amount.get('destroyer_amount')))
            if self == p2:
                self.piece = random.choice(valid_pieces)
            #if the piece you are placing is in the list then it goes to next if, if not it reasks question
            if self.piece in valid_pieces:
                #if you still have pieces then it lets you go to next part
                if self.ship_amount.get(self.piece+'_amount') > 0:
                    break



        '''Program Code Call Start'''


        #places the piece with the piece you picked
        self.place_piece(self.piece)


        '''Program Code Call End'''

    
    #method to check if you have placed all your pieces, to go to the next phase
    def check_if_all_placed(self):
        #sets it to 0 pieces
        self.how_many_placed = 0
        #loops through the keys in the dictionary of how many ships you have
        for key in self.ship_amount:
            #placeholder variable for the value of the key, which is the amount of that ship you have
            placed = self.ship_amount.get(key)
            #if you have 0 of that ship left
            if placed == 0:
                #it adds to 1 of how many ships you have placed
                self.how_many_placed += 1
        #once you have placed all your ships
        if self.how_many_placed == 5:
            #all_placed is set to true so you can go to next phase of the game
            self.all_placed = True
    
    def shoot_place(self):
        if self == p1:
            targeted_grid = p2.grid

        if self == p2:
            targeted_grid = p1.grid

        while True:
            if self == p1:
                shot_area = input('\nwhere do you want to shoot (State the row first and column second ex. "4 6")?\n')
                shot_area_list = shot_area.split()
            if self == p2:
                shot_area_list = [str(random.randint(1,10)), str(random.randint(1,10))]
            #tests to see if the numbers put in are numbers, and if there are two numbers put in, if not reloops
            if shot_area_list[0].isnumeric() == True and shot_area_list[1].isnumeric() == True and len(shot_area_list) == 2:
                #checks to see if the two numbers are inside the grid, if not reloops
                if (int(shot_area_list[0]) < 11 and int(shot_area_list[0]) > 0 and int(shot_area_list[1]) < 11 and int(shot_area_list[1]) > 0):
                    if targeted_grid[int(shot_area_list[0])][int(shot_area_list[1])] == 'X':
                        targeted_grid[int(shot_area_list[0])][int(shot_area_list[1])] = 'O'
                        self.battleships_hit += 1
                        break
                    elif targeted_grid[int(shot_area_list[0])][int(shot_area_list[1])] =='_':
                        targeted_grid[int(shot_area_list[0])][int(shot_area_list[1])] = '+'
                        break
    
    def check_win_condition(self):
        global hits_needed
        self.game_over = False
        if self.battleships_hit == hits_needed:
            self.game_over = True
        if self.game_over == True:
            if self == p2:
                print('player 2 won')
            if self == p1:
                print('player 1 won')







        

        
            
#initiates player 1 and 2 with battleship grids, starting ship amounts  0 ships placed, and all ships placed as False, how many battleships you have hit as 0 and the game_over is False
p1 = grids()
p2 = grids()

#main function that runs all the other methods for each class
def main():
    p1.update_grids()
    p2.update_grids()

    #runs while all ships haven't been placed
    while p1.all_placed == False and p2.all_placed == False:
        #updates each players grid
        #places pieces  for each player
        p2.place_pieces()
        p2.update_grids()
        p1.update_grids()
        p1.place_pieces()
        p1.update_grids()
        #checks if both players have placed all their pieces
        p1.check_if_all_placed()
        p2.check_if_all_placed()

    while p1.game_over == False and p2.game_over == False:
        p1.shoot_place()
        p2.update_grids()
        p2.shoot_place()
        p1.update_grids()
        p1.check_win_condition()
        p2.check_win_condition()

main()



