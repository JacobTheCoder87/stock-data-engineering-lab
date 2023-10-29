
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            prices = []
            for val in row [1:]:
                #print(type(val))
                try:
                    float(val)
                    prices.append(float(val))
                except:
                    continue 
            
            calculated_averages = round(sum(prices) / len(prices), 3)
            averages.append(calculated_averages)
        print(averages)
        return averages

    def median02(self):
        """pt2
        """
        median = []
        for row2 in self.data:
            prices2 = []
            for val2 in row2 [1:]:
                try:
                    float(val2)
                    prices2.append(float(val2))
                except:
                    continue
            calculated_median = stats.median(prices2)
            median.append(calculated_median)
        print(median)
        return median

        

    def stddev03(self):
        """pt3
        """
        standarddeviation = []
        for row3 in self.data:
            prices3 = []
            for val3 in row3 [1:]:
                try:
                    float(val3)
                    prices3.append(float(val3))
                except:
                    continue
            calculated_median = stats.stdev(prices3)
            standarddeviation.append(round(calculated_median, 3))
        print(standarddeviation)
        return standarddeviation
