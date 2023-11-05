
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
        # Here we are creating a new variable called prices so we can append our filtered clean data into this new variable later.
            for val in row [1:]:
        # Using a control flow statement we want to filter out val in our row of data to only include data from 1 til the end.
        # what this means esentially is that from our data we want to skip or filter out the date and keep the rest of our data.
                try:
                    float(val)
                    prices.append(float(val))
                except:
                    continue 
        # The try and except function will make sure that we are going to try and convert all of our values from a string to a float.
        # After we convert our data from a string to a float we will append them into the prices variable list that we have created.
        # If we encounter something that can't be converted into a float like " " empty spaces we will simply ignore and continue it
        # thus filtering out spaces in our data.
    
            calculated_averages = round(sum(prices) / len(prices), 3)
            averages.append(calculated_averages)
        print(averages)
        return averages
    
        # Since our validation code only accepts numbers rounded to the third decimal we must also round our prices to the third decimal.
        # We will calculate our average using the average function which is the sum of all prices divided by the amount of numbers we have.

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

        # The median follows the same principle as the code we have used above for average. The only difference is instead we are using the stat module
        # to calculate the median for us.
        

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

        # The standard deviation follows the same principle as the code we have used above for average. The only difference is instead we are using the stat module
        # to calculate the standard deviation for us.