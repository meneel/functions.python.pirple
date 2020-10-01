Name = "Ed Sheeran"
Age = 29
Song = "Perfect"


def ArtistName():
    global Name;
    return Name;


print("Artist Name:", ArtistName())


def ArtistAge():
    global Age;
    return Age;


print("Artist Age:", ArtistAge())


def SongName():
    global Song;
    return Song;


print("SongName:", SongName())


def MoreThan():
    if (Age > 1000):
        return False
    else:
        return True


print("Ed Sheeran is 29 years old:", MoreThan())
