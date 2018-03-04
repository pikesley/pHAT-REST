from microdotphat import clear, show, set_pixel, set_decimal

def render(matrix, decimals):
    clear()

    for i in range(7):
        for j in range(45):
            try:
                set_pixel(j, i, matrix[i][j])
            except IndexError:
                pass

    for decimal in decimals:
        set_decimal(decimal, 1)

    show()
