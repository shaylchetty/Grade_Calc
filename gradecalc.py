from operator import mul
import copy
import functools



alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

my_dict = {
    "A": 4.33, "B": 4.00, "C": 3.66, "D": 3.33, "E": 3.00, "F": 2.66,
    "G": 2.33, "H": 2.00
}


convert_dict = {
    "A": "A+", "B": "A", "C": "A-", "D": "B+", "E": "B", "F": "B-", "G": "C+", "H": "C"
}


reversed_dict = dict(map(reversed, convert_dict.items()))



def recurse(grade_range_len, num_courses):
    m1 = []
    ranges = [(0, grade_range_len+1)] * num_courses
    ranges = [(0, num_courses+1)] * grade_range_len
    operations = functools.reduce(mul, (p[1]-p[0] for p in ranges))-1
    result = [i[0] for i in ranges]
    pos = len(ranges)-1
    increments = 0
    # print(result)
    while increments < operations:
        if result[pos] == ranges[pos][1]-1:
            result[pos] = ranges[pos][0]
            pos -= 1
        else:
            result[pos] += 1
            increments += 1
            pos = len(ranges)-1  # increment the innermost loop
            if sum(result) == num_courses:
                m1.append(result.copy())
    return m1


def calc_gpa(a_list, my_dict, num_courses):
    new_list = []
    for ints in a_list:
        temp_sum = 0
        for count, iz in enumerate(ints):
            for i in range(iz):
                temp_sum += list(my_dict.values())[count]

        new_list.append((ints, round(temp_sum/num_courses, 2)))
    return new_list


def grade_range(top, bottom):
    ret_dict = my_dict
    rtop = reversed_dict[top]
    rbot = reversed_dict[bottom]
    x = alpha.index(rtop)
    y = alpha.index(rbot) + 1
    cutAlpha = alpha[x:y]
    rangex = []
    for item in cutAlpha:
        rangex.append(convert_dict[item])
    for key in ret_dict.copy():
        if key not in cutAlpha:
            ret_dict.pop(key)
    return ret_dict, rangex


def optimize(num_courses, desired_GPA, GPA_variability, top, bottom):
    print("")
    retlist = []
    my_dict, rangex = grade_range(top, bottom)
    grade_range_len = len(my_dict)
    flist = calc_gpa(recurse(grade_range_len, num_courses),
                     my_dict, num_courses)
    max = desired_GPA + (GPA_variability/100)*desired_GPA
    min = desired_GPA - (GPA_variability/100)*desired_GPA
    for f in flist:
        if (f[1] < max) and (f[1] > min):
            retlist.append([f[1], f[0]])
    if len(retlist) == 0:
        print(
            f"It is not possible to achieve a GPA of {desired_GPA}, with a grade range from {top} to {bottom}.")
    else:
        print(
            f"There are {len(retlist)} different ways to achieve a GPA of approximately {desired_GPA} ({GPA_variability}% variability), across {num_courses} courses.")
        print("")
    for count, pair in enumerate(retlist):
        print(f"GPA: {pair[0]}")
        for i in range(grade_range_len):
            if pair[1][i] != 0:
                print(rangex[i] + ":", end=' ')
                print(pair[1][i])
        print("")
    # return retlist


optimize(10, 3.9, 1, "A", "B-")
