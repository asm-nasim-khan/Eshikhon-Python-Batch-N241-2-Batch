# Add_song()
# Play_song()
# Next_song()
# Remove_song()
# print_PlayList()

class Music:
    def __init__(self,name):
        self.name = name
        self.playlist = []
        self.serial = 0

    def Add_song(self,*args):
        for song in args:
            self.playlist.append(song)
    
    def Play_song(self,song):
        if song in self.playlist:
            for index in range(len(self.playlist)):
                if song == self.playlist[index]:
                    print(song,"is playing. ")
                    self.serial = index
        else:
            print(song," is not in the list.")

    def Next_song(self):
        print(self.playlist[self.serial+1],"is playing. ")
        self.serial += 1
    
    def Remove_song(self,song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(song," has removed.")
        else:
            print(song," is not in the list.")
    def print_PlayList(self):
        num = 0
        print(self.name,"====================")
        for song in self.playlist:
            print(num,"=>",song)
            num += 1

user_1 = Music("Nasim")
user_1.Add_song("ABC","DEF","GHI")
user_1.print_PlayList()
user_1.Play_song("ABC")
user_1.Next_song()
user_1.Remove_song("DEF")
user_1.print_PlayList()

User_2 = Music("Rakib")
User_2.Add_song("OPS","OLP","RST")
User_2.print_PlayList()





