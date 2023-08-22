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
   
name_list = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace"]
badges_messages =  batch_badge_creator(name_list)

for message in badges_messages:
    print(message)

   

def assign_rooms(names):
    return None

def printer(names):
    return None
