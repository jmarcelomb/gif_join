import imageio

gifs = [
    # "gif0.gif",
    "gif1.gif",
    "gif2.gif",
    "gif2.gif",
    "gif2.gif",
    "gif2.gif",
    # "gif3.gif",
    "gif4.gif",
    "gif5.gif",
    "gif5.gif",
    "gif5.gif",
]
gif_list = []
for gif in gifs:
    gif_list.append(imageio.get_reader(gif))

combined_gif = imageio.get_writer("combined.gif")

for gif in gif_list:
    for frame in gif:
        combined_gif.append_data(frame)

for gif in gif_list:
    gif.close()

combined_gif.close()
