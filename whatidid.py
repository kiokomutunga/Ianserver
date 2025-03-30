import os

FILE_NAME = "notes.txt"

def add_note():
    # create my first note
    date = input("enter the date of the event in the format (YYYY-MM-DD)")
    Topic = input("Title of The movie") 
    body = input("what you think about the movie")
    Targetperson = input("Target audience for example children,girls , boys , couples, business")
    Year_of_publication = input("enter the year the movie was produced")
    morals_in_movie = input("please enter the morals and social issues should be addressed before the movie starts eg. Sex ,Murder,Nudity, Drugs,Violence, Racism, Technology")

    #save this in a file
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{Topic},{body},{Targetperson},{Year_of_publication},{morals_in_movie}\n")
    print("note added Successfully")
    # access notes
def view_note():
    if not os.path.exists(FILE_NAME):
        print("note not yet added in the system")
        return
    
    with open(FILE_NAME,"r") as file:
        print("\ndate       | Topic      |body    | Targetperson        | year_of_publication      | morals_in_movie")
        print("........................................")
        for line in file:
            date, Topic, Targetperson,Year_of_publication,morals_in_movie = line.strip().split(",") 
            print(f"{date:10}| {Topic} | {Targetperson} | {Year_of_publication} | {morals_in_movie}")

def database_store():
    pass


def 