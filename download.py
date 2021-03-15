from pytube import YouTube

def download(video_name):

    yt = YouTube(video_name)
    # video = yt.streams.first().download()
    return yt

#download('https://www.youtube.com/watch?v=NMlKHIqtuO0&ab_channel=Caifanes-Topic')

# def prueba(**data):
#     print(data)


# prueba(a="Hola", b="No se")

# # def intro(**data):
# #     print("\nData type of argument:",type(data))

# #     for key, value in data.items():
# #         print("{} is {}".format(key,value))

# # intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# # intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda")