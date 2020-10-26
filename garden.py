class Garden():
    def __init__(self):
        self.bed = [None,None,None,None]
        self.plants = {
            "plant_1": None,
            "plant_2": None,
            "plant_3": None,
            "plant_4": None
        }
    def print_bed(self):
       return (self.bed)
    def plant_bed(self, slot, plant):
        self.bed[slot] = plant
        pass
    def remove_plant(self, slot, plant):
        self.bed[slot] = None
        pass
class Plant():
    def __init__(self,kind,display,bloom_days,water_added,water_level,price,index =None):
        self.kind = kind
        self.index = index
        self.display = display
        self.bloom_days = bloom_days
        self.water_added = water_added
        self.water_level =water_level
        self.price = price
Lily = Plant("Lily","Lily",4,10,40,10)
Orchid = Plant("Orchild","Orchild",2,20,40,7)
sweetpea = Plant("sweetpea","sweetpea",1,20,30,8)
rose = Plant("rose","rose",3,20,30,5)
new_garden = Garden()
def print_plants(garden):
    for plant in garden.bed:
        print (plant)
flowers = {}
flowers['1']="Lily"
flowers['2']="roses"
flowers['3']="Orchid"
flowers['4']="sweetpea"
menu = {}
menu['1']="Display plants in Garden"
menu['2']="Add a plant to the Garden"
menu['3']="Water plant"
menu['4']="Remove plant"
menu['5']="Go to next day"
menu['6']="Quit"
while True:
    for key in menu.keys():
        print (f"{key}: {menu[key]}")
    selection= int(input("What would you like to do?:"))
    if selection == 1:
        print_plants(new_garden)
    elif selection == 2:
        flower = input("Which flower?")
        if flower == "1":
            new_garden.plant_bed(0,"Lily")
            print ("Lily")
        elif flower == "2":
            new_garden.plant_bed(1,"roses")
            print("roses")
        elif flower == "3":
            new_garden.plant_bed(2,"Orchid")
            print("Orchid")
        elif flower == "4":
            new_garden.plant_bed(3,"sweetpea")
            print("sweetpea")
        else:
            print("Try again")
        print("New plant added")
    elif selection == 3:
        print("Plant is now watered")
    elif selection == 4:
        flower = input("Which flower?")
        if flower == "1":
            new_garden.remove_plant(0,"Lily")
            print ("Lily")
        elif flower == "2":
            new_garden.remove_plant(1,"roses")
            print("roses")
        elif flower == "3":
            new_garden.remove_plant(2,"Orchid")
            print("Orchid")
        elif flower == "4":
            new_garden.remove_plant(3,"sweetpea")
            print("sweetpea")
        else:
            print("Try again")
    elif selection == 5:
        print("Next Day")
    elif  selection == 6:
        break
    else:
        print("Not Valid Choice Try again")



# while True:
#     user_input = input("Would you like to plant a flower?")
#     if user_input == "x":
#         break 
#     if user_input == "yes":
#         print(Garden.kind)


# new_garden.plant_bed()
# new_garden.print_bed()




# class tree:
#     def __init__(self,name,rain = 5,disappearing =5):
#         self.name = name
#         self.rain = rain
#         self.disappearing = disappearing

#     def weather(self):
#         self.rain +=5%

#     def missing(self):
#         self.disappearing +=5%

# gnome = tree("gnome")
# gnome.weather()
# print(gnome.rain)

