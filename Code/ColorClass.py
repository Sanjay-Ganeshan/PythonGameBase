class ColorClass:
    Colors = {}
    def __init__(self):
        try:
            f = open('../ReqContent/Colors.txt','r')
        except IOError:
            raise Exception("Could not locate Colors.txt!")
        for line in f:
            temp = line.split('\t')
            self.Colors[(str(temp[0])).replace('*','')] = (int(temp[1]),int(temp[2]),int(temp[3]))
    def getColors(self):
        return self.Colors.keys()
