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
        type(self).count += 1
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
    
    @classmethod
    def add_to_genres(cls, genre):
        
        if genre in cls.genres:
            cls.genre_count[genre] += 1
        else:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            cls.artist_count[artist] += 1
        else:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
            
        
        
        
    
