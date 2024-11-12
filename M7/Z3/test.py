colors = {
    "frame_color1": ["red", "yellow", "green", "blue", "purple", "black"],
    "frame_color2": [
        "brown",
        "orange",
        "aquamarine",
        "DeepSkyBlue",
        "violet",
        "SlateGray",
    ],
}

for frame in colors.keys():
    print(frame)

    for color in colors[frame]:
        print(color)
