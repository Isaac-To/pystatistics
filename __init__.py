import math

class basic:
    def sum(data):
        sum = 0
        for i in data: sum += i
        return sum

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

class fiveNumberSummary:
    def __init__(self, data: list):
        self.data = data.sort()
    
    def calculate(self):
        self.min = self.data[0]
        self.max = self.data[-1]
        self.q1 = center.quartiles(self.data)[0]
        self.q3 = center.quartiles(self.data)[1]
        self.median = center.median(self.data)
        return {
            "min": self.min,
            "max": self.max,
            "q1": self.q1,
            "q3": self.q3,
            "median": self.median
        }
    
