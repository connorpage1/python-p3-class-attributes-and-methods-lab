class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}
    
    def __init__(self, name, artist, genre ) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
    
    @classmethod
    def add_to_genres(cls, genre):
        
        if genre in Song.genres:
            Song.genre_count[genre] += 1
        else:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist in Song.artists:
            Song.artist_count[artist] += 1
        else:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
            
        
        
        
    
