#discussion https://leetcode.com/discuss/interview-question/373006/Amazon-or-OA-2019-or-Favorite-Genres/391841
#problem : https://aonecode.com/amazon-online-assessment-questions#g
#solution
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
