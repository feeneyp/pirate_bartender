import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}



def ask_pirate():
  answer_dict = {}
  for x in questions:
    answer = raw_input(questions[x])
    if (answer == "yes" or answer == "y"):
      answer_dict[x] = True
    else:
      answer_dict[x] = False
  print answer_dict
  return answer_dict 
  
def make_drink(preferences):
  for i in preferences:
    if preferences[i] == True:
      preferences[i] = random.choice(ingredients[i])
  for j in preferences:
    if preferences[j] != False:
      print preferences[j]
  return preferences
  

if __name__ == '__main__':
  make_drink(ask_pirate())
  
