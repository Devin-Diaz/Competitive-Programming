# PROBLEM 5 - Top Ten

'''
NOTES

n = number of times a song is played
d = number of different days that the song was played
s = span - the difference between the first day the song was played and the last day the song was played.

formula used to calculate top 10 songs is *nd + s*
'''


song_ids_for_all_days = [] # stores sublists of integers which represent song ids for each day, where days are sublists.


# we are expecting two weeks worth of songs so 14 days, when our list is this size, we are done collecting input.
while True:
    if len(song_ids_for_all_days) == 14: break
    user_input = input()
    current_day_song_ids = user_input.split(' ')
    current_day_song_ids = [int(song_id) for song_id in current_day_song_ids]
    song_ids_for_all_days.append(current_day_song_ids)


# map to keep track of data for each song. 'n' is integer for song count. 
# 'd' is set so we don't have duplicate days when a song is played. same for 's'.
# technically we can use only d or s as they collect the same data for days, but for learning purposes I'll 
# use extra space complexity.
song_data_map = dict()


# iterate through each sublist, then each element of each sublist, while keep track of sublist and elements indices.
for day, current_song_list in enumerate(song_ids_for_all_days):
    for song_index, song_id in enumerate(current_song_list):
        if song_id == -1: continue # means no song was played so we can avoid adding it to our data.
        if song_id not in song_data_map:
            song_data_map[song_id] = {'n': 0, 'd': set(), 's': set()}
        
        # update occurrences, and days song is played. 
        song_data_map[song_id]['n'] += 1
        song_data_map[song_id]['d'].add(day + 1) # we do +1 do we denote actual days instead of indices.
        song_data_map[song_id]['s'].add(day + 1)


# will be used to store song_ids as keys and there rating after use of formula as value. 
all_song_ratings_map = dict()


# used for parsing through our span data for a song.
def unpacking_span_of_song(s: set):
    s_list = list(s)
    if len(s_list) >= 2:
        # if song is played multiple times, we get first element (first time played) and last element (last time played).
        return s_list[-1] - s_list[0] 
    
    return 1 # otherwise it was only played 1 day thus the difference is 1. 


# get rating number of each song
def splotchify_formula(n, d, s):
    return (n * d) + s


# unpacking our song_data_map (dictionary) to begin our calculations for top 10 songs
for song_id, data in song_data_map.items():
    n = data['n']
    d = len(data['d'])
    s = unpacking_span_of_song(data['s'])
    song_rating_calculation = splotchify_formula(n, d, s)
    all_song_ratings_map[song_id] = song_rating_calculation


# sorting items in descending order so we can have the highest ratings first. 
sorted_data_calculations = dict(sorted(all_song_ratings_map.items(), key=lambda item: item[1], reverse = True))


# displaying our final results of the top 10 songs!
for song in list(sorted_data_calculations.keys())[0:10]:
    print(song, end=' ')

