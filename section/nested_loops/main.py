# List of trips
trips = [['france', 'germany', 'italy', 'spain', 'netherlands', 'sweden', 'norway', 'switzerland', 'austria', 'portugal', 'belgium'],
         ['japan', 'china', 'thailand', 'vietnam', 'ndonesia', 'india', 'malaysia', 'philippines', 'singapore', 'mongolia'],
         ['usa', 'canada', 'mexico', 'brazil', 'argentina', 'colombia', 'peru', 'chile', 'ecuador'],
         ['egypt', 'morocco', 'south africa', 'tunisia', 'algeria', 'kenya', 'nigeria', 'ethiopia'],
         ['australia', 'new zealand', 'fiji', 'papua new guinea', 'samoa']]

# List of all countries 
countries = []

for place in trips:
    for j in place :
       j =j.capitalize()
       countries.append(j)

# Testing
print('List of Countries:', countries)