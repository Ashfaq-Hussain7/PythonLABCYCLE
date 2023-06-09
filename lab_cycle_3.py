# -*- coding: utf-8 -*-
"""Lab_Cycle_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y62H4TG2DWr16NsQ1J6lia-HP_SboSEu
"""

from itertools import count
from timeit import repeat
import pygame,sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=800
LINE_WIDTH=25
WINDOW_COL=1
WINDOW_ROW=4
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 50
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = 55
RED = (255,0,0)
CIRCLE_COLOUR = (120,120,120)
LINE_COLOUR=(232,232,232)
BG_COLOUR=(200,200,200)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOUR )

board = np.zeros((BOARD_ROWS,BOARD_COLS))
window=np.zeros((WINDOW_ROW,WINDOW_COL))
global win

def draw_lines():
   #horizontal
    pygame.draw.line(screen, LINE_COLOUR, (20,200), (580,200),LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOUR, (20,400), (580,400),LINE_WIDTH )
   #vertical
    pygame.draw.line(screen, LINE_COLOUR, (200,15), (200,590),LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOUR, (400,15), (400,590),LINE_WIDTH )
   #borders
    pygame.draw.line(screen, LINE_COLOUR, (0,10), (600,10),25)
    pygame.draw.line(screen, LINE_COLOUR, (10,0), (10,600),25 )

    pygame.draw.line(screen, LINE_COLOUR, (590,10), (590,600),25)
    pygame.draw.line(screen, LINE_COLOUR, (0,600), (600,600),25)
    rec=pygame.draw.rect(screen, CIRCLE_COLOUR, pygame.Rect(50, 650, 200, 100))
    font = pygame.font.SysFont('Arial', 35)
    screen.blit(font.render('Restart', True, (0,0,0)), ((85,685) ))
    pygame.display.update()

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen,CIRCLE_COLOUR,(int( col*200+100),#
                          int(row*200+110)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen,CIRCLE_COLOUR,(col*200+SPACE,#
                                   row*200+200-SPACE),(col*200+200-SPACE,#
                                   row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line( screen,CIRCLE_COLOUR,(col*200+SPACE,#
                                row*200+SPACE),(col*200+200-SPACE,#
                                 row*200+200-SPACE),CROSS_WIDTH)


def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    #print(board[row][col])
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    #status()
    return True

def check_win(player):
    #vertical check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and #
                                     board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    #horizontal check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and #
                                  board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonla check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc Diagonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col,player):
    posX = col * 200 + 100
    
    if player == 1:
        colour = RED
        print("O WINS")
    elif player == 2:
        colour = RED
        print("X WINS")
    win=1
    pygame.draw.line(screen, CIRCLE_COLOUR,(posX,35),(posX,600-30),10)
    

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100

    if player == 1:
        print("O WINS")
    elif player == 2:
        print("X WINS")
    win=1

    pygame.draw.line(screen,CIRCLE_COLOUR,(35,posY),(600-30,posY),10)



def draw_asc_diagonal(player):
    if player == 1:
        print("O WINS")
    elif player == 2:
        print("X WINS")
    pygame.draw.line(screen,CIRCLE_COLOUR,(35,600-35),(600-35,35),10)
    win=1

def draw_desc_diagonal(player):
    if player == 1:
       print("O WINS")
    elif player == 2:
       print("X WINS")
    pygame.draw.line(screen,CIRCLE_COLOUR,(35,35),(600-35,600-35),10)
    win=1

def status():
    if win == "X":
        print("X WINS")
    elif win == "O":
        print("O WINS")
    


def check_outside(row,col):
    if  (row>=50 and row<=250)and (col>=650 and col<=750):
        #print("Entered2")
        return True
    else:
        return False

def restart():
    screen.fill( BG_COLOUR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS): 
            board[row][col] = 0

draw_lines()



player = 1
win=0
game_over = False



mouseX = 0
mouseY = 0
count = 0
while True:
    for event in pygame.event.get():
    

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY //200)
            clicked_col = int(mouseX // 200)
            #print(clicked_row)
            #print(WINDOW_ROW)
            #print(clicked_row  != WINDOW_ROW-1)

           
            if clicked_row  != WINDOW_ROW-1:
                if available_square(clicked_row,clicked_col):
               
                    if player == 1:
                        mark_square( clicked_row,clicked_col,1)
                        if check_win(player):
                            game_over = True
                        player = 2
                    elif player ==2:
                        mark_square( clicked_row,clicked_col,2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()
                    if game_over == True and count == 0:
                        status()
                 
                
            elif event.type == pygame.MOUSEBUTTONDOWN :
                #print("Entered")
                #print(mouseX," ",mouseY)
                if check_outside(mouseX,mouseY):
                    #print("Get restart")
                    restart()
                    game_over=False

       
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
        
        if event.type == pygame.QUIT:
            sys.exit()
        
    pygame.display.update()

import numpy as np
import pandas as pd
def PCA(X , num_components):
     
    # mean Centering the data  
    X_mean = X - np.mean(X , axis = 0) 
   
    # calculating the covariance matrix of the mean-centered data.
    cov_mat = np.cov(X_mean, rowvar = False)
    print("\nCovarience Matrix :\n",cov_mat)
    print("_"*70)
     
    #Calculating Eigenvalues and Eigenvectors of the covariance matrix
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
    print("\nEigen Value :\n",eigen_values)
    print("\nEigen Vector:\n",eigen_vectors)
    print("_"*70)
    
    #sort the eigenvalues and eigenvectors in descending order
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
     
    # select the first n eigenvectors, n is desired dimension
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]
     #Transform the data 
    X_reduced = np.dot(eigenvector_subset.transpose() ,#
               X_mean.transpose() ).transpose()
     
    return X_reduced
   
r=int(input("Enter the number of rows    : "))
c=int(input("Enter the number of colums : "))
print("\nEnter the values in the form of",r,"*",c,"matrix form :");
a=[(input().split()) for j in range(r)]
matrix=np.array(a,float)
print("_"*70)
print("\nMatrix : \n",matrix)
print("_"*70)
 
mat_reduced = PCA(matrix , 2)

#Creating a Pandas DataFrame of reduced Dataset
principal_df = pd.DataFrame(mat_reduced , columns = ['PC1','PC2'])
print("\nPrincipal Component Analysis : \n")
print(principal_df)
print("_"*70)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def show_bar(file):
    species = file["Species"]
    species_modified = species.drop_duplicates()
    species_frequency = species.value_counts()
    plt.bar(species_modified, species_frequency, width=0.4)
    plt.show()


def scatter_graph(file):
    file_pca = file.drop(columns=["Species"])
    pca = PCA(n_components=2)
    file_PCA = pca.fit_transform(file_pca)
    file_PCA = pd.DataFrame(file_PCA, columns=["pca1", "pca2"])
    colormap = plt.colormaps.get_cmap("jet")
    colors = file["Species"].astype("category").cat.codes
    file_PCA.plot.scatter(x="pca1",
                          y="pca2",
                          c=colors,
                          cmap=colormap)
    plt.xlabel("PCA1")
    plt.ylabel("PCA2")
    plt.show()


def hist_diagram(file):

    sepal_length = file['SepalLengthCm']
    sepal_width = file['SepalWidthCm']
    petal_length = file['PetalLengthCm']
    petal_width = file['PetalWidthCm']

    print("which histogram distribution to show")
    print("1 . sepal length")
    print("2 . sepal width")
    print("3 . petal length")
    print("4 . petal width")

    user_input = int(input("enter what to do : "))

    if user_input == 1:
        plt.hist(sepal_length, bins=10, color="red")
    elif user_input == 2:
        plt.hist(sepal_width, bins=10, color="red")
    elif user_input == 3:
        plt.hist(petal_length, bins=10, color="red")
    elif user_input == 4:
        plt.hist(petal_width, bins=10, color="red")

    plt.show()


file = pd.read_csv("/content/Iris.csv")
running = True
while running == True:
    print(1, " show bar graph of species ")
    print(2, " show scattered graph of PCA ")
    print(3, " show historical diagram 1")
    print(4, "quit\n\n")
    input_user = input("what is your choice : ")
    input_user = int(input_user)
    print("")

    while input_user != 5:

        if input_user == 1:
            show_bar(file)
            break
        elif input_user == 2:
            scatter_graph(file)
            break
        elif input_user == 3:
            hist_diagram(file)
            break
        elif input_user == 4:
            running = False
            print("thank you")
            break

import pickle,tabulate
class vehicleAttributes:
  #list of keys of the attributes of the vehicle.
  _keyList = ["id","ownerName","vendor","model","type","registrationNumber","engineNumber","mileage"]
  #creating a dictionary with the keys and values as None.
  _dataBase = dict.fromkeys(_keyList, None)

class Vehicles(vehicleAttributes):
  #list which will save the dictionary of every vehicles
  __listOfVehicles = list()
  __id = 0
  def addEntries(self):
    option = 1
    while option==1:
      self.__id = self.__id + 1
      entryList = list()
      entryList.append(self.__id)
      entryList.append(input("Owner Name : "))
      entryList.append(input("Vendor Name : "))
      entryList.append(input("Model Name : "))
      entryList.append(input("Type : "))
      entryList.append(int(input("Registration Number : ")))
      entryList.append(int(input("Engine Number : ")))
      entryList.append(float(input("Mileage : ")))
      
      for i,key in zip(entryList,self._dataBase):
        self._dataBase[key] = i
      self.__listOfVehicles.append(self._dataBase.copy())
      option = int(input("Do you want to add more entries\n1.Add\n2.Exit\n"))

  def deleteEntries(self):
    found = False
    searchKey = int(input("Enter your ID : "))
    for i in range(len(self.__listOfVehicles)):
      if self.__listOfVehicles[i]['id']==searchKey:
        found = True
        del self.__listOfVehicles[i]
        break
    if(not found):
      print("Invalid Id")
  
  def modifyEntries(self):
    found = False
    searchKey = int(input("Enter your ID : "))
    for i in self.__listOfVehicles:
      if i['id']==searchKey:
        found = True
        print("Choose the attribute you want to change")
        print("1.Owner Name\n2.Vendor Name\n3.Model Name")
        print("4.Type\n5.Registration Number\n6.Engine Number")
        print("7.Mileage")
        option = int(input())
        if option==1:
          i['ownerName'] = input("Owner Name : ")
        elif option==2:
          i['vendor'] = input("Vendor Name : ")
        elif option==3:
          i['model'] = input("Model Name : ")   
        elif option==4:
          i['type'] = input("Type : ")
        elif option==5:
          i['registrationNumber'] = int(input("Registration Number : "))    
        elif option==6:
          i['engineNumber'] = int(input("Engine Number : "))
        elif option==7:
          i['mileage'] = float(input("Mileage : "))
    if(not found):
      print("Invalid Key")

  def display(self,*args):
    header = ['Id','Owner','Vendor','Model','Type','Registration Number','Engine Number','Mileage']
    if(len(args)==0):
      rows =  [x.values() for x in self.__listOfVehicles]
      print(tabulate.tabulate(rows, header,tablefmt='grid'))
    elif (len(args)==2):
      print("\n",args[0])
      rows = [x.values() for x in args[1]]
      print(tabulate.tabulate(rows, header,tablefmt='grid'))

  def sortMileage(self):
    sortedList = sorted(self.__listOfVehicles,key = lambda i:i['mileage'])
    self.display("Mileage Sorted List",sortedList)

  def createFile(self):
    pickle.dump(self.__listOfVehicles,open("vehicleDetails.pkl","wb"))

  def filterAttributes(self):
    print("Choose the attribute which you want to filter\n1.Owner Name")
    print("2.Vendor\n3.Model Name\n4.Type\n5.Mileage")
    option = int(input("Option : "))
    filteredList = list()
    if(option==1):
      filterKey = (input("Enter the name you want to filter"))
      filteredList = [i for i in self.__listOfVehicles if i['ownerName']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==2):
      filterKey = (input("Enter the name you want to filter"))
      filteredList = [i for i in self.__listOfVehicles if i['vendor']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==3):
      filterKey = (input("Enter the name you want to filter"))
      filteredList = [i for i in self.__listOfVehicles if i['model']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==4):
      filterKey = (input("Enter the name you want to filter"))
      filteredList = [i for i in self.__listOfVehicles if i['type']== filterKey]
      self.display("Filtered List",filteredList)
    elif(option==5):
      filterKey = float(input("Enter the name you want to filter"))
      filteredList = [i for i in self.__listOfVehicles if i['mileage']== filterKey]
      self.display("Filtered List",filteredList)
  def loadFile(self,filePath):
    self.__listOfVehicles = pickle.load(open(filePath,"rb"))
    idList = [self.__listOfVehicles[i]['id'] for i in range(len(self.__listOfVehicles))]
    self.__id = max(idList)

def main():
  vehicleObject = Vehicles()
  if(int(input("1.Add Entries\n2.Load Pickle\n"))==1):
    vehicleObject.addEntries()  
  else:
    filePath = input("Enter the file name : ")
    vehicleObject.loadFile(filePath)
  vehicleObject.display()
  mainLoopOption=1
  while mainLoopOption==1:
    print("1.Add Entries\n2.Modify Attributes\n3.Delete Attributes\n4.Display Entries")
    print("5.Sort According to Mileage\n6.Filter Attributes\n7.Create Pickle File\n8.Exit")
    choice = int(input())
    if choice==1:
      vehicleObject.addEntries()
    elif choice==2:
      vehicleObject.modifyEntries()
    elif choice==3:
      vehicleObject.deleteEntries()
    elif choice==4:
      vehicleObject.display()
    elif choice==5:
      vehicleObject.sortMileage()
    elif choice==6:
      vehicleObject.filterAttributes()
    elif choice==7:
      vehicleObject.createFile()
    elif choice==8:
      break
  mainLoopOption = int(input("\n1.Continue\n2.Exit"))

if __name__=="__main__":
  main()

from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfile
from tkinter.messagebox import showinfo
from tkinter.ttk import Style, Treeview
import pickle

global listOfVehicles
global sortedList
listOfVehicles = list()
vehicle_attributes = ["ownerName","vendor","model","type","registrationNumber","engineNumber","mileage"]
vehicleDetails = dict.fromkeys(vehicle_attributes, None)

def addList():
    global listOfVehicles
    treeList.insert(parent='', index='end', text="", values=(owner.get(), vendor.get(),model.get(),typeClass.get(),regNumber.get(),engNumber.get(),mileage.get()))
    vehicleDetails['ownerName'] = owner.get()
    vehicleDetails['vendor'] = vendor.get()
    vehicleDetails['model'] = model.get()
    vehicleDetails['type'] = typeClass.get()
    vehicleDetails['registrationNumber'] = int(regNumber.get())
    vehicleDetails['engineNumber'] = int(engNumber.get())
    vehicleDetails['mileage'] = float(mileage.get())
    listOfVehicles.append(vehicleDetails.copy())

def filterList():
    global listOfVehicles
    if(owner.get()!="" or vendor.get()!="" or model.get()!="" or typeClass.get()!="" or mileage.get()!=""):
        for item in treeList.get_children():
            treeList.delete(item)
    else:
        showinfo(title="Error",message="Give a Filter Key")
    if(owner.get()!=""):
        filterKey = owner.get()
        for i in listOfVehicles:
            if i['ownerName']==filterKey:
                treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
    elif (vendor.get()!=""):
        filterKey = vendor.get()
        for i in listOfVehicles:
            if i['vendor']==filterKey:
                treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
    elif (model.get()!=""):
        filterKey = model.get()
        for i in listOfVehicles:
            if i['model']==filterKey:
                treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
    elif (typeClass.get()!=""):
        filterKey = typeClass.get()
        for i in listOfVehicles:
            if i['type']==filterKey:
                treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
    elif (mileage.get()!=""):
        filterKey = float(mileage.get())
        for i in listOfVehicles:
            if i['mileage']==filterKey:
                treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
def delete():
   # Get selected item to Delete
    selection=treeList.selection()[0]
    treeList.delete(selection)

def loadFile():
    #Clear the treeview list items
    for item in treeList.get_children():
        treeList.delete(item)
    filetypes = (
        ('Picle files', '*.pkl'),
        ('All files', '*.*')
    )
    global listOfVehicles
    filename = askopenfilename(title="Open Pickle",initialdir='/',filetypes=filetypes)
    listOfVehicles = pickle.load(open(filename,"rb"))
    showinfo(title="Selected File",message=filename)
    for i in listOfVehicles:
        treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))


def sortMileage():
    #Clear the treeview list items
    for item in treeList.get_children():
        treeList.delete(item)
    global listOfVehicles
    global sortedList
    sortedList = sorted(listOfVehicles,key= lambda i:i['mileage'])
    for i in sortedList:
        treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))
    showinfo(title="Sorted",message="Sorted Successfully")

def createPickle():
    fileextensions = [('Pickle File', '*.pkl'),('All Files', '*.*')]
    file = asksaveasfile(filetypes = fileextensions, defaultextension = fileextensions)
    pickle.dump(listOfVehicles,open(file,"wb"))
    showinfo(title="Created File",message="Vehicle Pickle File is Created")

#window configuration.
window = Tk()
window.geometry("750x400")
window.title("Vehicle Data")