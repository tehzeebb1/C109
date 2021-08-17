import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

dice_result=[]

for i in range(0,1000):
    dice1= random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

#dice_result=3,10,12,4,6.....

#Calculating the mean and the standard deviation
mean = sum(dice_result) / len(dice_result)

std_deviation=statistics.stdev(dice_result)

print("Mean:",mean)
print("SD:",std_deviation)
#Calculating the median and mode
median = statistics.median(dice_result)
print("Median:",median)
mode = statistics.mode(dice_result)
print("Mode:", mode)

#fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
#fig.show()

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation

second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#Printing the findings
list_of_data_within_1_std_deviation=[result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies between 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))