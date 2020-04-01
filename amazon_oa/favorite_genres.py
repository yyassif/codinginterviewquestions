#discussion https://leetcode.com/discuss/interview-question/373006/Amazon-or-OA-2019-or-Favorite-Genres/391841
#problem : https://aonecode.com/amazon-online-assessment-questions#g
#leetcode playground solution https://leetcode.com/playground/KCLirPgs
#solution 1
def initialize():
    userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
    songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
    
    # userSongs = {  
    #  "David": ["song1", "song2"],
    #  "Emma":  ["song3", "song4"]
    # }
    # songGenres = {}
    
    # converting given input to sets
    for user in userSongs:
        userSongs[user] = set(userSongs[user])
        
    for genre in songGenres:
        songGenres[genre] = set(songGenres[genre])
    
    return userSongs, songGenres

def favGenres(users, genres):
    res = {}
    for user in users.keys():
        user_songs = users[user]
        user_fav = []
        max_song_count = 0
        for genre in genres.keys():
            genre_songs = genres[genre]
            song_count = len(user_songs.intersection(genre_songs))
            if song_count:
                if song_count > max_song_count:
                    max_song_count = song_count
                    user_fav = [genre]
                elif song_count == max_song_count:
                    user_fav.append(genre)
        res[user] = user_fav
    return res
            
        

if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favGenres(userSongs, songGenres))
    
#####################END OF SOL 1

#solution 2
def favorite_genres(userSongs, songGenres):
    song2genres, output = {}, {}
    for genre in songGenres:
        for song in songGenres[genre]:
            song2genres[song] = genre
    
    for user in userSongs:
        user_genres_list = []
        for song in userSongs[user]:
            user_genres_list.append(song2genres[song])
        genre_counter = Counter(user_genres_list)
        most_common_number = max(genre_counter.values())
        favorite_genres = [genre for genre in genre_counter if genre_counter[genre] == most_common_number]
        output[user] = favorite_genres
    return output
