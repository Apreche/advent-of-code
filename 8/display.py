class Display:
    def __init__(self, width=1, height=1):
        self.grid = []

        if width < 1 or height < 1:
            raise Exception('width and height must both be > 0')

        self.width = width
        self.height = height

        for y in range(height):
            row = []
            for x in range(width):
                row.append('.')
            self.grid.append(row)

    def set_bit(self, x, y, value):
        try:
            self.grid[y][x] = value
        except IndexError:
            raise Exception("coordinate doesn't exist")

    def get_bit(self, x, y):
        try:
            return self.grid[y][x]
        except IndexError:
            raise Exception("coordinate doesn't exist")

    def rect(self, width, height):
        for x in range(width):
            for y in range(height):
                self.set_bit(x, y, '#')

    def rotate_row(self, row, distance):
        if row > self.height:
            raise Exception("row doesn't exist")
        distance = distance * -1
        self.grid[row] = self.grid[row][distance:] + self.grid[row][:distance]

    def rotate_column(self, column, distance):
        if column > self.width:
            raise Exception("column doesn't exist")
        distance = distance * -1
        data = []
        for y in range(self.height):
            data.append(self.get_bit(column, y))
        data = data[distance:] + data[:distance]
        for y, bit in enumerate(data):
            self.set_bit(column, y, bit)

    @property
    def count(self):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.get_bit(x, y) == '#':
                    count += 1
        return count

    def __unicode__(self):
        rows = []
        for row in self.grid:
            rows.append(''.join(row))
        return '\n'.join(rows)

    def __str__(self):
        return self.__unicode__()
