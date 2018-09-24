def song_playlist(songs, max_size):
    
    playlist = []
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
    else:
        return playlist
    song_ascend = sorted(songs, key = lambda x: x[2])
    song_ascend.remove(songs[0])
    rem_space = max_size - songs[0][2]
    for i in song_ascend:
        if i[2] <= rem_space:
            playlist.append(i[0])
            rem_space -= i[2]
        else:
            break
    return playlist
    
# Correct
