current_movies = {'The Grinch': '11:00am',
                  'Rudoplh' : '1:00pm',
                  'Frosty the Snowman' : '3:00pm',
                  'Christmas Vacation' : '5:00pm'}

print("We are showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie do you wabt the showtime for?')

showtime = current_movies.get(movie)

if showtime == None:
    print("The requested movie isn't playing.")
else:
    print(movie , 'is showing at ', showtime)