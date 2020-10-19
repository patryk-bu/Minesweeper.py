import random as r


class square:
    def __init__(self, x, y, bomb, id):
        self.id = id
        self.value = 0
        self.location = (x, y)
        self.is_bomb = bomb
        self.pixel_pos = ()
        self.button = ""
        self.around=[]

    def make_bomb(self):
        self.is_bomb = True


class mine_field:
    def __init__(self):
        self.squares = []
        for y in range(14):
            for x in range(19):
                self.squares.append(square(x, y, False, len(self.squares)))
        bombs = []
        while len(bombs) < 40:
            x = r.randrange(266)
            if self.get_obj_by_val(x) not in bombs:
                self.get_obj_by_val(x).make_bomb()
                bombs.append(self.get_obj_by_val(x))
        for i in self.squares:
            x = i.location[0]
            y = i.location[1]
            to_check = [(x - 1, y - 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y - 1),
                        (x + 1, y - 1)]
            for j in to_check:
                if self.get_obj_by_coord(j) is not None:
                    if self.get_obj_by_coord(j).is_bomb:
                        # print(i.location," bomb at ", j)
                        i.value += 1
        self.uncovered = []
        self.edge = []
        self.flagged = []
        self.disabled=[]
        for i in self.squares:
            x = i.location[0]
            y = i.location[1]
            to_check = [(x - 1, y - 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y - 1),
                        (x + 1, y - 1)]
            for j in to_check:
                if self.get_obj_by_coord(j) is not None:
                    i.around.append(self.get_obj_by_coord(j))




    def click_on_obj(self, obj):
        check = []
        if not obj.is_bomb:
            if obj.value == 0:
                self.uncovered.append(obj)
                x = obj.location[0]
                y = obj.location[1]
                to_check = [(x - 1, y - 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                            (x, y - 1),
                            (x + 1, y - 1)]
                for i in to_check:
                    if self.get_obj_by_coord(i) is not None:
                        if not self.get_obj_by_coord(i).is_bomb:
                            if self.get_obj_by_coord(i).value == 0:
                                if self.get_obj_by_coord(i) not in self.uncovered:
                                    check.append(self.get_obj_by_coord(i))
                            else:
                                self.edge.append(self.get_obj_by_coord(i))
                for i in check:
                    self.click_on_obj(i)
            else:
                self.edge.append(obj)
        else:
            return True
        self.edge = list(dict.fromkeys(self.edge))

    def get_obj_by_val(self, val):
        for i in self.squares:
            if i.id == val:
                return i
        return None

    def get_obj_by_coord(self, coords):
        for i in self.squares:
            if i.location == coords:
                return i
        return None
