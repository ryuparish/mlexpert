def get_statistics(input_list):
    # Write your code here.
    myDict = {
        "mean": 0 ,
        "median": 0,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0],
    }
    if(len(input_list) < 1):
        return myDict
    input_list.sort()
    myDict["mean"] = sum(input_list) / len(input_list)
    myDict["median"] = input_list[len(input_list)//2] if len(input_list) % 2 == 1 else (input_list[len(input_list)//2] + input_list[(len(input_list)//2) -1])/2
    myDict["mode"] = max([(input_list.count(i),i) for i in input_list])[1] if max([input_list.count(i) for i in input_list]) != 1 else input_list[len(input_list) -1]
    myDict["sample_variance"] = sum([(i - myDict["mean"])**2 for i in input_list])/(len(input_list) - 1)
    myDict["sample_standard_deviation"] = myDict["sample_variance"]**(1/2)
    myDict["mean_confidence_interval"] = [myDict["mean"] - 1.96*(myDict["sample_standard_deviation"]/(len(input_list)**(1/2))), myDict["mean"] + 1.96*(myDict["sample_standard_deviation"]/(len(input_list)**(1/2)))]
    return myDict
