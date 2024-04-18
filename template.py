import copy
from random import choice
from PIL import Image




class OverlayImage:
    def __init__(self, image_name):
        self.image = Image.open(image_name)
        self.width, self.height = self.image.size
        self.x, self.y = 0, 0

        print(f'''Start image size:
                Width: {self.width} Height: {self.height}''')
        self.demo_image = Image.new('RGB', (self.width, self.height),
                                    (118, 255, 97))
        self.demo_image.paste(self.image, (0, 0), self.image)
        self.pixels = self.image.load()
        # создание матрицы с нулями
        self.matrix = [[0] * self.width for _ in range(self.height)]

    def crop(self):
        image_square = 0
        lower_right_coord = [None, None]
        upper_left_coord = [None, None]
        for i in range(self.width):
            for j in range(self.height):
                r, g, b, a = self.pixels[i, j]
                if a != 0:
                    image_square += 1
                    if upper_left_coord[0] is None:
                        upper_left_coord[0] = i
                    if upper_left_coord[1] is None:
                        upper_left_coord[1] = j

                    if lower_right_coord[0] is None:
                        lower_right_coord[0] = i
                    if lower_right_coord[1] is None:
                        lower_right_coord[1] = j
                    else:
                        if upper_left_coord[0] > i:
                            upper_left_coord = i
                        if upper_left_coord[1] > j:
                            upper_left_coord[1] = j

                        if lower_right_coord[0] < i:
                            lower_right_coord[0] = i
                        if lower_right_coord[1] < j:
                            lower_right_coord[1] = j
        self.demo_image = self.demo_image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        self.image = self.image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        self.width, self.height = self.image.size

    def save_rez(self, name=None):
        if name == None:
            self.image.save('image.png')
            self.demo_image.save('demo_image.png')

    def edit_random(self):
        flip_degrees = [0, 90, 180, 270]  # список градусов поворота
        degrees = choice(flip_degrees)  # выбор градуса поворота

        self.image = self.image.rotate(
            degrees, expand=True)  # поворот PNG изображения
        self.demo_image = self.demo_image.rotate(
            degrees,
            expand=True)
        self.width, self.height = self.image.size
        self.pixels = self.image.load()

    def create_matrix(self):
        # check pixels, matrix
        for i in range(self.height):
            for j in range(self.width):
                r, g, b, a = self.pixels[j, i]
                if a != 0:
                    self.matrix[i][j] = 1

    def get_data(self):
        self.image.save('ready_image.png')
        rez = dict()
        rez['x'] = self.x
        rez['y'] = self.y
        rez['height'] = self.height
        rez['matrix'] = self.matrix
        rez['width'] = self.width
        return rez


class MainImage(OverlayImage):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new(
            'RGBA', (self.width, self.height), (0, 0, 0, 0))
        self.demo_image = Image.new(
            'RGBA', (self.width, self.height), (118, 255, 97))
        self.main_matrix = [
            [0 for _ in range(self.width)] for __ in range(self.height)]
        self.pixels = self.image.load()


    def add_images(self, data):
        overlaying_image = Image.open('ready_image.png')
        x, y, over_matrix = data['x'], data['y'], data['matrix']
        ov_im_width, ov_im_height = overlaying_image.size
        good_height = False
        im_qual = 0
        fail_count = 0

        while not good_height and y >= 0:
            matrix_copy = copy.deepcopy(self.main_matrix)
            overlay = False
            over_matrix[0][0] = 'A'
            over_matrix[ov_im_height - 1][ov_im_width - 1] = 'Z'
            for i in range(self.height):
                for j in range(self.width):
                    # ENTER
                    small_i = i - y
                    small_j = j - x
                    if ov_im_height > small_i >= 0 and ov_im_width > small_j >= 0:
                        if not self.main_matrix[i][j] == over_matrix[small_i][small_j] == 1:
                            if self.main_matrix[i][j] == 0:
                                self.main_matrix[i][j] = over_matrix[small_i][small_j]

                        else:
                            overlay = True
            if not overlay:
                self.image.paste(
                    overlaying_image, (x, y), overlaying_image)
                good_height = True
                im_qual += 1
            else:
                fail_count += 1

                self.main_matrix = matrix_copy
                y -= 10

        print('DONE!')


    def save_rez(self, name=None):
        if name == None:
            self.image.save('main_image_from_1.1.1.png')
            file = open('rezult_1.1.1.txt', 'w', encoding='utf-8')
        else:
            self.image.save(f'{name}.png')
            file = open(f'{name}.txt', 'w', encoding='utf-8')

        for row in self.main_matrix:
            file.write(str(row))
            file.write('\n')

    def crop(self):
        return super().crop()


def start(name, size):
    NAME = name
    QUALITY = 150
    size_size = size.replace("(", "").replace(")", "").split(", ")
    WIDTH_1 = int(size_size[0])
    HEIGHT_1 = int(size_size[1])
    WIDTH, HEIGHT = WIDTH_1, HEIGHT_1
    MAIN_IMAGE = MainImage(WIDTH, HEIGHT)
    for t in range(QUALITY):
        OVER_IMAGE = OverlayImage(NAME)
        OVER_IMAGE.crop()
        OVER_IMAGE.edit_random()
        OVER_IMAGE.create_matrix()
        OVER_IMAGE.save_rez()
        datas = OVER_IMAGE.get_data()
        MAIN_IMAGE.add_images(datas)
        MAIN_IMAGE.save_rez()
