class Line:
    node_dic = {}

    def __init__(self, stx, sty, edx, edy):
        super().__init__()
        self.stx = stx
        self.sty = sty
        self.edx = edx
        self.edy = edy

    def set_st(self, x, y):
        self.stx = x
        self.sty = y

    def set_ed(self, x, y):
        self.edx = x
        self.edy = y
