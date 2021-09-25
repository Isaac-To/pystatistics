import math

class basic:
    def sum(data):
        sum = 0
        for i in data: sum += i
        return sum

    def fivenumbersummary(data):
        data.sort()
        return {
            "min": data[0],
            "max": data[-1],
            "q1":  center.quartiles(data)[0],
            "q3": center.quartiles(data)[1],
            "median": center.median(data)
        }

    def recurPow(data, pow):
        return [i**pow for i in data]

class center:
    def mean(data):
        s = sum(data)
        mean = s / len(data)
        return mean

    def median(data):
        lL = len(data) - 1
        hP = lL // 2
        data.sort()
        if lL % 2 != 0:
            return center.mean([data[hP], data[hP + 1]])
        else:
            return data[hP]
        
    def quartiles(data):
        data.sort()
        m = center.median(data)
        fH = [data[i] for i in range(len(data)//2)]
        sH = [data[i] for i in range(round(len(data)/2), len(data))]
        q1 = center.median(fH)
        q3 = center.median(sH)
        return (q1, q3)

    def mode(data):
        data.sort()
        highest = [[0, data[0]], [0, data[1]]]
        repeat = 0
        buffer = 0
        for i in data:
            if i == buffer:
                repeat += 1
            else:
                buffer = i
                repeat = 1
            if repeat >= highest[0][0]:
                if buffer != highest[0][1]:
                    highest.append([repeat, buffer])
                highest[-1][0] = repeat
        return[i[1] for i in highest if i[0] == highest[-1][0]]

class spread:
    def distanceFromMean(data):
        return [i - center.mean(data) for i in data]

    def meanDeviation(data):
        return center.mean(spread.distanceFromMean(data))

    def varience(data):
        return center.mean([i**2 for i in spread.distanceFromMean(data)])

    def standardDeviation(data):
        return math.sqrt(spread.varience(data))
    
    def range(data):
        return max(data) - min(data)

    def iqr(data):
        iqr = center.quartiles(data)
        return iqr[1] - iqr[0]

    def outliers(data):
        iqr = spread.iqr(data)
        quartiles = center.quartiles(data)
        mdistance = iqr * 1.5
        return [i for i in data if i < quartiles[0] - mdistance or i > quartiles[1] + mdistance]

class comparison:
    def zscore(item, arg, arg1 = None):
        if arg1 is None:
            return (item - center.mean(arg))/spread.standardDeviation(arg)
        else:
            return (item - arg)/arg1        

    def percentile(item, data):
        data.sort()
        for i, j in enumerate(data):
            if item <= j:
                break
        return i * 100 / (len(data)-1)

class normalDistribution:
    def probabilityDensityFunction(mean, standardDeviation, value):
        return (math.e ** ((-1 * (value-mean) ** 2)/(2 * (standardDeviation ** 2))))/(math.sqrt(2 * math.pi * (standardDeviation ** 2)))

    def culminativeDensityFunction(mean, standardDeviation, min, max):
        sum, val = 0, 0
        for i in range(min, max):
            for j in range(0, 100000):
                val = i + (j / 100000)
                sum += normalDistribution.probabilityDensityFunction(mean, standardDeviation, val)/100000
        return sum

    def inverseCulminativeDensityFunction(mean, standardDeviation, area):
        sum, val = 0, 0
        for i in range(mean - standardDeviation * 5, mean + standardDeviation * 5):
            for j in range(0, 100000):
                val = i + (j / 100000)
                if math.isclose(sum, area, abs_tol=0.000001):
                    print(sum)
                    return val
                sum += normalDistribution.probabilityDensityFunction(mean, standardDeviation, val)/100000
        return val

class twodarray:
    def __init__(self, *array):
        self.array = [i for i in array]
    
    def toString(self):
        return self.array

    def index(self, index):
        return self.array[index]
    
    def append(self, x, y):
        self.array.append([x, y])

    def remove(self, index):
        self.array.remove(index)

    def removeWhereX(self, x):
        self.array = [i for i in self.array if i[0] != x]
    
    def removeWhereY(self, y):
        self.array = [i for i in self.array if i[1] != y]

    def remove(self, x, y):
        self.array = [i for i in self.array if i[0] != x and i[1] != y]

    def clear(self):
        self.array = []

    def fill0(self, num):
        self.array.clear()
        self.array = [[0, 0] for i in range(0, num)]

    def xList(self):
        return [self.array[i][0] for i in range(len(self.array))]

    def yList(self):
        return [self.array[i][1] for i in range(len(self.array))]

    def sort(self, d = "x", order = "asc"):
        if d == "x":
            dnum = 0
        elif d == "y":
            dnum = 1
        for i in range(0, len(self.array)):
            for j in range(i, len(self.array)):
                if order == "asc":
                    if self.array[i][dnum] > self.array[j][dnum]:
                        self.array[i], self.array[j] = self.array[j], self.array[i]
                elif order == "desc":
                    if self.array[i][dnum] < self.array[j][dnum]:
                        self.array[i], self.array[j] = self.array[j], self.array[i]

    def r(self):
        n = len(self.array)
        x = self.xList()
        y = self.yList()
        xSq = basic.recurPow(x, 2)
        ySq = basic.recurPow(y, 2)
        xy = [x[i] * y[i] for i in range(n)]
        sumX = basic.sum(x)
        sumY = basic.sum(y)
        sumXSq = basic.sum(xSq)
        sumYSq = basic.sum(ySq)
        sumXY = basic.sum(xy)
        return (((n * sumXY) - (sumX * sumY))/(math.sqrt((n * sumXSq - sumX**2) * (n * sumYSq - sumY**2))))
    
    def rsquared(self):
        return (self.r())**2

    def leastSquaresRegressionLine(self):
        r = self.r()
        SDx = (spread.standardDeviation(self.xList()))
        SDy = (spread.standardDeviation(self.yList()))
        slope = r * (SDy/SDx)
        constant = center.mean(self.yList()) - slope * center.mean(self.xList())
        return {
            "slope": slope,
            "constant": constant,
            "r": r,
            "r2": r**2
        }

    def residual(self, x, y):
        eq = (self.leastSquaresRegressionLine())
        return y - (eq["slope"]*x + eq["constant"])

    def recurResidual(self):
        return [[i[0], self.residual(i[0], i[1])] for i in self.array]
