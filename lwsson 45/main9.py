class Playlist:
 def __init__(self,name,genre):
    self.name = name
    self.genre = genre
    self.songs=[]
    print(f"Playlist'{self.name}'({self.genre}) is ready")

 def add_song(self.song)
 self.songs.append(song)
 print(f"'{song}'added to {self.name}")

 def remove_songs(self.song):
   if song in self.songs:
      self.songs.remove(song)
      print(f"'{song}'removed")
    else:
      print(f"'{song}'is not found in playlist")

 def display(self):
   print(f"\n---{self.name}({self.genre})---")
   if self.songs:
      for i,song in enumerate(self.songs,1):
        