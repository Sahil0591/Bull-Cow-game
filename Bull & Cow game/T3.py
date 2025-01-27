class MyDate:
    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return str(self.dd) + "-" + str(self.mm) + "-" + str(self.yy)


d = MyDate(15, 8, 1947)
print(d)
class MyEvent:
    def __init__(self, dd, mm, yy, detail):
        self.date = MyDate(dd, mm, yy)
        self.detail = detail
    def __str__(self):
        return str(self.date) + " => " + self.detail

e = MyEvent(15, 8, 1947, "Independence Day")
print(e)