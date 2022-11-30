def list_operations(films):
    print("The length of the list is: " + str(len(films)))
    print("The last film is: " + films[-1])
    films.reverse()
    print("List reversed " + str(films))
    print("The movie is " + str("Memento" in films) + " in the film")
    print("Adding movie...")
    films.append("Memento")
    print("Removing movie...")
    films.remove("The Godfather")

def loop_operations(films):
    for movie in films:
        print("Movie name " + movie)

    for movie in films:
        print("First letter is : " + movie[0])

    for movie in films:
        print("Movie in upper case case " + movie.upper())

    all_films = ""
    for movie in films:
        all_films += movie
        all_films += " , "

    print("List in a string: " + all_films[:-2])

    longest_name = ""
    longest_length = 0

    for movie in films:
        if len(movie) > longest_length:
            longest_name = movie
            longest_length = len(movie)

    print("The longest movie is: " + longest_name)

def main():
    films = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather: Part II", "Pulp Fiction",
             "Schindler's List"]

    list_operations(films)
    loop_operations(films)


main()