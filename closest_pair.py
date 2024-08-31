def naive_closest_pair(points):
    min_distance = float('inf')
    closest_pair = None
    closest_pair_index = (0, 0)

    # compair each pair of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            distance = euclidean_distance(p1, p2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (p1, p2)
                closest_pair_index = i, j

    return closest_pair, min_distance, closest_pair_index

def euclidean_distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) **2) ** 0.5

points_ = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_pair_, distance_, _ = naive_closest_pair(points_)
print(f"Naive approach - Closest pair: {closest_pair_}, Distance: {distance_}")

def closest_pair(points):
    # sort point by x- coordinate
    points_sorted_by_x = sorted(points, key=lambda p:p[0])
    return closest_pair_recursive(points_sorted_by_x)

def closest_pair_recursive(points_sorted_by_x):
    # Length of the array
    n = len(points_sorted_by_x)

    # Base case: if there are 2 or 3 points, use the brute-force
    if n <= 3:
        return naive_closest_pair(points_sorted_by_x)

    # Divide: split the points into two halves
    mid = n // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    # Conquer: Recursively find the closet point in the sorted halves
    closest_pair_left, min_distance_left, closest_pair_left_index = closest_pair_recursive(left_half)
    closest_pair_right, min_distance_right, closest_pair_right_index = closest_pair_recursive(right_half)

    # Combine: Find the closest pair across the divide
    if min_distance_left < min_distance_right:
        min_distance = min_distance_left
        closest_pair = closest_pair_left
        closest_pair_index = closest_pair_left_index
    else:
        min_distance = min_distance_right
        closest_pair = closest_pair_right
        closest_pair_index = closest_pair_right_index

    # check point near the divide
    closest_point_across, min_distance_across = closest_point_across_divide(points_sorted_by_x, mid, min_distance)

    if min_distance_across < min_distance:
        return closest_point_across, min_distance_across, _
    else:
        return closest_pair, min_distance, closest_pair_index


def closest_point_across_divide(points_sorted_by_x, mid, min_distance):
    mid_x = points_sorted_by_x[mid][0]

    # Consider points within the distance min_dist from the midpoint
    strip = [p for p in points_sorted_by_x if abs(p[0] - mid_x) < min_distance]

    # Sort the strip by y-coordinate
    strip.sort(key=lambda p: p[1])

    min_dist_across = min_distance
    closest_pair_across = None

    # Check only the points within the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist_across:
                break
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_dist_across:
                min_dist_across = distance
                closest_pair_across = (strip[i], strip[j])

    if closest_pair_across:
        return closest_pair_across, min_dist_across
    else:
        return None, float('inf')

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_pair, distance, _ = closest_pair(points)
print(f"Divide and Conquer approach - Closest pair: {closest_pair}, Distance: {distance}")