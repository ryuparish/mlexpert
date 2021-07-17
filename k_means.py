import random


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    initial_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    # Get the centroid values (2D array} of each centroid starter user
    user_centroids = [Centroid(user_feature_map[user]) for user in initial_centroid_users]

    # Write your code here.
    for i in range(10):
        # Adding each user to a centroid
        for user in user_feature_map:
            user_info = user_feature_map[user]
            eDistances = {}
            for index, centroid in enumerate(user_centroids):
                eDistance = 0
                for feature_num in range(num_features_per_user):
                    eDistance += abs(centroid.location[feature_num] - user_info[feature_num])
                eDistances[eDistance] = index
            closestDistance = min(eDistances)
            user_centroids[eDistances[closestDistance]].closest_users.add(tuple(user_info))
        # Finding the mean of each value attached to each centroid
        for centroid in user_centroids:
            newCentroidLocation = [0 for number in range(num_features_per_user)]
            for user in centroid.closest_users:
                for index, dimension in enumerate(user):
                    newCentroidLocation[index] += dimension
            if(len(centroid.closest_users) == 0):
                continue;
            newCentroidLocation = [value/len(centroid.closest_users) for value in newCentroidLocation]
            centroid.location = newCentroidLocation
            centroid.closest_users.clear()
    returnCentroids = []
    for centroid in user_centroids:
        returnCentroids.append(list(centroid.location))
    return returnCentroids
    
