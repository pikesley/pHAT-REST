import inkyphat

def render(matrix):
    for x in range(inkyphat.WIDTH):
        for y in range(inkyphat.HEIGHT):
            inkyphat.putpixel((x, y), 0)

    for x in range(inkyphat.WIDTH):
        for y in range(inkyphat.HEIGHT):
            try:
                inkyphat.putpixel((x, y), matrix[y][x])
            except(IndexError):
                pass

    inkyphat.show()
