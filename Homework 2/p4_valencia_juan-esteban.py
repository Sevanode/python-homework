import csv 

def display_top_collaborations():
    top_rated_collaborations={}
    top_rated_movies=csv.reader(open("imdb-top-rated.csv","r",newline=""))
    f = open("imdb-top-casts.csv", newline="")
    reader = csv.reader(f)
    top_casts = list(reader) 

    for movie_row in top_rated_movies:          ##Sorts through
        movie=movie_row[1]
        for cast_row in top_casts:
            print("Checking:", movie, cast_row[0])
            if movie in cast_row:
                print("movie found")
                director, actor = cast_row[2], cast_row[3]          
                key = f"{director}:{actor}"
                if key in top_rated_collaborations:         ##When a collab is found it puts it in using the names combined as a key
                    top_rated_collaborations[key] += 1
                else:
                    top_rated_collaborations[key] = 1

    top_rated_collaborations=dict(sorted(top_rated_collaborations.items(), key=lambda item: item[1], reverse=True)) 
    for key, value in top_rated_collaborations.items():
        director, actor = key.split(":")
        tup = (director, actor, value)
        print(tuple(tup))

    
    

def display_top_directors():
    director_gross = {}
    with open("imdb-top-grossing.csv", newline="") as gross_file:
        reader = csv.reader(gross_file)
        next(reader)  # Skip header
        for row in reader:
            title = row[1]
            year = row[2]
            box_office = int(row[3])
            # Find director from imdb-top-casts.csv
            with open("imdb-top-casts.csv", newline="") as cast_file:
                cast_reader = csv.reader(cast_file)
                for cast_row in cast_reader:
                    if title == cast_row[0] and year == cast_row[1]:
                        director = cast_row[2]
                        if director in director_gross:
                            director_gross[director] += box_office
                        else:
                            director_gross[director] = box_office
                        break
    # Sort directors by total gross descending
    director_gross = dict(sorted(director_gross.items(), key=lambda item: item[1], reverse=True))
    for rank, (director, total_gross) in enumerate(director_gross.items(), 1):
        print(f"{rank}. {director}: ${total_gross:,}")


def main():
    print("Top Collaborations:")
    result = display_top_collaborations()
    print(result)
    print("\nTop Directors:")


if __name__ == "__main__":
    main()
