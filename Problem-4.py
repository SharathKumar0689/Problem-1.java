def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)
     
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
 
# Driver function
if __name__ == "__main__":
    my_list =[1,2,8,9,12,46,76,82,15,20,30]
    CountFrequency(my_list)
