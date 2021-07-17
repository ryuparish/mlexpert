# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    eDistances = {}
    for pid in examples:
        process = examples[pid]
        eDistance = 0
        eDistanceSquaredSum = 0
        for featureNum in range(len(process["features"])):
            eDistanceSquaredSum += (features[featureNum] - process["features"][featureNum])**2 
        eDistance = eDistanceSquaredSum**(1/2)
        eDistances[eDistance] = process["is_intrusive"]
    topKDistances = sorted(eDistances)[:k]
    topKLabels = [eDistances[distance] for distance in topKDistances]
    noCount = topKLabels.count(0)
    yesCount = topKLabels.count(1)
    if(yesCount > noCount):
        return 1
    return 0

def find_k_nearest_neighbors(examples, features, k):
    eDistances = {}
    for pid in examples:
        process = examples[pid]
        eDistance = 0
        eDistanceSquaredSum = 0
        for featureNum in range(len(process["features"])):
            eDistanceSquaredSum += (features[featureNum] - process["features"][featureNum])**2 
        eDistance = eDistanceSquaredSum**(1/2)
        eDistances[eDistance] = pid
    topKDistances = sorted(eDistances)[:k]
    topKProcesses = [eDistances[distance] for distance in topKDistances]
    return topKProcesses
