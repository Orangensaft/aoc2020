class WaitingArea:
    def __init__(self, area: str):
        self.area = area.split("\n")
        self.height = len(self.area)
        self.width = len(self.area[0])

    def get(self,x,y):
        raise NotImplementedError()

    def getNeighbors(self,x,y):
        raise NotImplementedError()
