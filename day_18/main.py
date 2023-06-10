import colorgram

colors = colorgram.extract("spots.jpeg", 2 * 32)

rgb_colors = []

for color in colors:
    rgb_extracted = color.rgb
    rgb_total = sum([rgb for rgb in rgb_extracted])

    if rgb_total < 680:
        rgb_colors.append(tuple(rgb_extracted))
    
print(rgb_colors)