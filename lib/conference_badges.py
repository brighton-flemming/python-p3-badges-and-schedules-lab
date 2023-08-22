def badge_maker(name):
    greeting = f'Hello, my name is {name}.'
    print(greeting)
    return greeting

def batch_badge_creator(names):
 badges=[]
 for name in names:
   message = badge_maker(name)
   badges.append(message)
 return badges
   
name_list = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Matz"]
badges_messages =  batch_badge_creator(name_list)

for message in badges_messages:
    print(message)


def assign_rooms(names):
 list = []
 
 for index,name in enumerate (names):
    if index < len(room_num):
     welcoming = f"Hello, {name}! You'll be assigned to room {room_num[index]}!"
     list.append(welcoming)
    else:
       welcoming = f"Hello {name}! Room number is not available!"
       print(welcoming)

 return list

room_num = [1, 2, 3, 4 , 5, 6, 7, 8]
name_list = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace","Frankie", "Matz" ]
list = assign_rooms(name_list)

for welcoming in list:
    print (welcoming)
 




def printer(names):
    return None
