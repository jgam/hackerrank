# Complete the activityNotifications function below.
def median(aux, half, even):
        if  even: # made a median of 2 central elements
                return (aux[half] + aux[half + 1]) / 2
        else: # return central element
                return aux[half]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
        notifications = 0
        initial_day = 0
        last_day = d

        #this is median array sorted already
        median_arr = sorted(expenditure[initial_day:last_day])
        
        # the following vars don't change in the future, so they need be computaded one time
        n_median = len(median_arr) # len of median array will be fixed
        half = math.ceil(n_median/2) - 1
        even = True if n_median % 2 == 0 else False 

        n = len(expenditure) # the length of the exp array
        while last_day < n:
                med = median(median_arr, half, even) # calculate the median
                last_day_exp = expenditure[last_day] # get the last day expenditure
                if last_day_exp >= 2 * med: # check if have some notification
                        notifications += 1
                j = bisect.bisect_left(median_arr, expenditure[initial_day]) # get the postition of the exp. of the initial day
                del median_arr[j] # remove the element to keep the median_arr with the same length
                bisect.insort(median_arr, last_day_exp) # insert the actual last day exp. that will be part of the median in the next loop
                # increment the days
                initial_day += 1
                last_day += 1

        return notifications # return the num of notifications
