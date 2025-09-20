import csv 

def display_top_collaborations():
    top_rated_collaborations={}
    top_rated_movies=csv.reader(open("imdb-top-rated.csv","r",newline=""))
    f = open("imdb-top-casts.csv", newline="")
    reader = csv.reader(f)
    top_casts = list(reader) 

    for movie_row in top_rated_movies:
        movie=movie_row[1]
        for cast_row in top_casts:
            print("Checking:", movie, cast_row[0])
            if movie in cast_row:
                print("movie found")
                director, actor = cast_row[2], cast_row[3]
                key = f"{director}:{actor}"
                if key in top_rated_collaborations:
                    top_rated_collaborations[key] += 1
                else:
                    top_rated_collaborations[key] = 1

    top_rated_collaborations=dict(sorted(top_rated_collaborations.items(), key=lambda item: item[1], reverse=True)) 
    for key, value in top_rated_collaborations.items():
        director, actor = key.split(":")
        tup = (director, actor, value)
        print(tuple(tup))
       
display_top_collaborations()
