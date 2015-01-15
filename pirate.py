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


def find_preferences():
  preferences = questions
  for i in questions:
    preferences[i] = raw_input(questions[i]).lower() in ["y","yes"]
  print preferences
  return preferences 
  
def make_drink(preferences):
  for j in preferences:
    if preferences[j] == True:
      preferences[j] = random.choice(ingredients[j])
  print preferences    
  return preferences
  
  
if __name__ == '__main__':
  preferences = find_preferences()
  drink = make_drink(preferences)
  print "Here's your ingredients:"
  for component in drink:
    if drink[component]:
      print "A {}".format(drink[component])
  
  
