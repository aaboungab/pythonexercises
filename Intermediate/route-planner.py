print("Enter your route e.g. 0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15")
#input route for user
peaks = input()

#function to plan best route
def route_planner(peaks):
    peaks_list = peaks.split(" ")
    #create a new list to store increasing peaks 
    final_route = []
    for peak in peaks_list: 
        if len(final_route) == 0:
            final_route.append(peak)
        #if peak is greater than previous peak then append, if not then continue 
        elif int(peak) > int(final_route[len(final_route) - 1]):
            final_route.append(peak)
        else:
            continue
    return final_route

best_route = route_planner(peaks)
print(f"The best route to take is going to be:  {' '.join(best_route)}")
