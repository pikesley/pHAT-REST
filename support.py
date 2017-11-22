import os

RASPI = os.uname()[1] == 'raspberrypi'

if RASPI:
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

else:
    def render(matrix, decimals):
        for row in matrix:
            m = ' '
            index = 0
            for bit in row:
                if (4 - (index % 8)) < 0:
                    m += ' '
                else:
                    if bit == 0:
                        m += '.'
                    if bit == 1:
                        m += 'o'
                index += 1
            print m

        d = ''
        for i in range(6):
            try:
                decimals.index(i)
                d += 'o'
            except ValueError:
                d += ' '
            d += '       '
        print d
