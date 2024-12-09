data = [4, 7, 3, 2, 1, 5, 6, 8]
print("data sebelum diurutkan:", data)
if len(data) > 1:
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    if len(left_half) > 1:
        mid_left = len(left_half) // 2
        left_left = left_half[:mid_left]
        left_right = left_half[mid_left:]
        left_left.sort()
        left_right.sort()
        sorted_left = []
        i = j = 0
        while i < len(left_left) and j < len(left_right):
            if left_left[i] < left_right[j]:
                sorted_left.append(left_left[i])
                i += 1
            else:
                sorted_left.append(left_right[j])
                j += 1
        sorted_left.extend(left_left[i:])
        sorted_left.extend(left_right[j:])
        left_half = sorted_left

    if len(right_half) > 1:
        mid_right = len(right_half) // 2
        right_left = right_half[:mid_right]
        right_right = right_half[mid_right:]
        right_left.sort()
        right_right.sort()
        sorted_right = []
        i = j = 0
        while i < len(right_left) and j < len(right_right):
            if right_left[i] < right_right[j]:
                sorted_right.append(right_left[i])
                i += 1
            else:
                sorted_right.append(right_right[j])
                j += 1
        sorted_right.extend(right_left[i:])
        sorted_right.extend(right_right[j:])
        right_half = sorted_right
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    data = result

print("data setelah diurutkan:", data)
