#boredlessTourist.py
#Online application helping
#users to find the parts of 
#the city that fit their 
#lifestyles.
# part of Codecademy/CS Track

destinations = ["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil","Cairo, Egypt"]

test_traveler = ['Erin Wilkes','Shanghai,China',['historical site','art']]

def get_destination_index(destination):
  destination_index = destination.index(destination)
  return destination_index

print(get_destination_index("Los Angeles, USA") )

def get_traveler_location(traveler):
 traveler_destination = traveler[1]
 traveler_destination_index = get_destination_index(traveler_destination)
 return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[] for des in destinations]

def add_attraction(destination,attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = destination_index(attractions)
  attractions_for_destination.append(attraction)
  return attractions_for_destination

add_attraction("Los Angeles, USA",['Venice Beach',['beach']])
print(attractions)

dd_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
 destination_index = get_destination_index(destination)
 attractions_in_city = attractions[destination_index]
 attractions_with_interest = []
 for tem in attractions_in_city:
  possible_attraction = tem
 for tem in destinations:
  attraction_tags = item[1]
  for tem2 in interests:
    if interest in attraction_tags:
    attractions_with_interest.append(possible_attraction[0])
  return(attractions_with_interest)

la_arts = find_attractions("Los Angeles,USA",['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  
interests_string = "Hi"+traveler[0]+",we think you'll like these places around "
for tem in traveler_attractions:
 interests_string = interests_string+" "+tem
return(interests_string)


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 

  

  
 

  
  
  
  
  
  
  
  

    