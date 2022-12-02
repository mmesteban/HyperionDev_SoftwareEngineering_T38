import spacy
nlp = spacy.load('en_core_web_md')

# read movies.txt and save into dict
movies = {}
with open ("movies.txt", "r") as f:
    for line in f:
        parts = line.split(" :")
        movies[parts[0]] = parts[1]

# method to return the most matching movie
def recommend(description):
    description_nlp = nlp(description)
    closest = ""
    sim = 0
    # loop through the dict
    for key in movies:
        similarity = nlp(movies[key]).similarity(description_nlp)
        print(similarity)
        if similarity>sim:
            sim = similarity
            closest = key
        else:
            continue
    
    print(f"The closest film I can recommend is {closest}.\nIts sinopsis is: {movies[closest]}")
    return





# CODE _____________________________________________________________________
description = input("Please enter a sinopsis for a movie. I will return you the closest one on my database.\nInput nothing for the base sinopsis given in the exercise")

if description == "":
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# call the method
recommend(description)


