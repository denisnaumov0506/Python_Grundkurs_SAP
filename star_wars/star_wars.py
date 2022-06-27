star_wars_movies = [  
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],  
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],   
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

try:
    trilogy = int(input("What trilogy do you want to select (1,2 or 3): "))
    movie = int(input("What movie of selected trilogy do you wish to select (1, 2 or 3): "))
except ValueError:
    message = "Please enter an integer value of 1, 2 or 3!"
else:
    try:
        if trilogy != 0 and movie != 0:
            message = 'You wish to see the movie "' + star_wars_movies[trilogy-1][movie-1] + '", correct?'
        else:
            message = "Selection is out of bounds! Please enter a value of 1, 2, or 3!"
    except IndexError:
        message = "Selection is out of bounds! Please enter a value of 1, 2, or 3!"
    
print(message)