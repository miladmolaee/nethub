from Input.texture import Texture


class Input:
    texture: Texture

    def __init__(self):
        print('f')

    def read_file(self):

        self.texture = Texture()

        file = open('E:/NetHub/data/script', 'r')
        Lines = file.readlines()
        newLines = []

        for line in Lines:
            if not line[0] == '#':
                string = ''
                for i in line:
                    if not (i == ' ' or i == '\t'):
                        string = string + i
                newLines.append(string)

        count = 0
        # Strips the newline character
        for line in newLines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

        return self.texture
