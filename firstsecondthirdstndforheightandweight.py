import random
import plotly.figure_factory as ff
import plotly.express as ps
import pandas as spb
import statistics

data = spb.read_csv("dataforhandw.csv")

fig = ff.create_distplot([data["Height(Inches)"].tolist()], ["height"], show_hist=False)
fig.show()

#height

hlist = data["Height(Inches)"].tolist()

hmean = statistics.mean(hlist)
hmode = statistics.mode(hlist)
hmedian = statistics.median(hlist)
h_stnd = statistics.stdev(hlist)

h_first_stnd_start, h_first_stnd_end = hmean - h_stnd, hmean + h_stnd
h_second_stnd_start, h_second_stnd_end = hmean - (2*h_stnd), hmean + (2*h_stnd)
h_third_stnd_start, h_third_stnd_end = hmean - (3*h_stnd), hmean + (3*h_stnd)

h_list_of_data_within_one_stnd = [result for result in hlist if result>h_first_stnd_start and result<h_first_stnd_end]
h_list_of_data_within_second_stnd = [result for result in hlist if result>h_second_stnd_start and result<h_second_stnd_end]
h_list_of_data_within_third_stnd = [result for result in hlist if result>h_third_stnd_start and result<h_third_stnd_end]

print("Median is ", hmedian)
print("Mode is ", hmode)
print("Mean is ", hmean)
print("Standard Deviation is ", h_stnd)
print("{}% of data lies within 1 Standard Deviation ".format(len(h_list_of_data_within_one_stnd)*100/len(hlist)))
print("{}% of data lies within 2 Standard Deviation ".format(len(h_list_of_data_within_second_stnd)*100/len(hlist)))
print("{}% of data lies within 3 Standard Deviation ".format(len(h_list_of_data_within_third_stnd)*100/len(hlist)))

#weight

wlist = data["Weight(Pounds)"].tolist()

wmean = statistics.mean(wlist)
wmode = statistics.mode(wlist)
wmedian = statistics.median(wlist)
w_stnd = statistics.stdev(wlist)

w_first_stnd_start, w_first_stnd_end = wmean - w_stnd, wmean + w_stnd
w_second_stnd_start, w_second_stnd_end = wmean - (2*w_stnd), wmean + (2*w_stnd)
w_third_stnd_start, w_third_stnd_end = wmean - (3*w_stnd), wmean + (3*w_stnd)

w_list_of_data_within_one_stnd = [result for result in wlist if result>w_first_stnd_start and result<w_first_stnd_end]
w_list_of_data_within_second_stnd = [result for result in wlist if result>w_second_stnd_start and result<w_second_stnd_end]
w_list_of_data_within_third_stnd = [result for result in wlist if result>w_third_stnd_start and result<w_third_stnd_end]

print("Median is ", wmedian)
print("Mode is ", wmode)
print("Mean is ", wmean)
print("Standard Deviation is ", w_stnd)
print("{}% of data lies within 1 Standard Deviation ".format(len(w_list_of_data_within_one_stnd)*100/len(wlist)))
print("{}% of data lies within 2 Standard Deviation ".format(len(w_list_of_data_within_second_stnd)*100/len(wlist)))
print("{}% of data lies within 3 Standard Deviation ".format(len(w_list_of_data_within_third_stnd)*100/len(wlist)))