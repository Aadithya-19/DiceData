import random
import plotly.figure_factory as ff
import plotly.express as ps
import pandas as spb
import statistics

dice_result = []
count = []

for i in range(0, 1000):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice_result.append(num1+num2)

median = statistics.median(dice_result)
mode = statistics.mode(dice_result)


stnd_deviation = statistics.stdev(dice_result)

mean = sum(dice_result)/len(dice_result)

first_stnd_start, first_stnd_end = mean - stnd_deviation, mean + stnd_deviation
second_stnd_start, second_stnd_end = mean - (2*stnd_deviation), mean + (2*stnd_deviation)
third_stnd_start, third_stnd_end = mean - (3*stnd_deviation), mean + (3*stnd_deviation)

list_of_data_within_one_stnd = [result for result in dice_result if result>first_stnd_start and result<first_stnd_end]
list_of_data_within_second_stnd = [result for result in dice_result if result>second_stnd_start and result<second_stnd_end]
list_of_data_within_third_stnd = [result for result in dice_result if result>third_stnd_start and result<third_stnd_end]

print("Median is ", median)
print("Mode is ", mode)
print("Mean is ", mean)
print("Standard Deviation is ", stnd_deviation)
print("{}% of data lies within 1 Standard Deviation ".format(len(list_of_data_within_one_stnd)*100/len(dice_result)))
print("{}% of data lies within 2 Standard Deviation ".format(len(list_of_data_within_second_stnd)*100/len(dice_result)))
print("{}% of data lies within 3 Standard Deviation ".format(len(list_of_data_within_third_stnd)*100/len(dice_result)))