# -*- encoding: utf-8 -*-


def quick_sort(series):
    '''快速排序'''
    if not isinstance(series, list):
        print('请输入列表')
        return
    tag = series[0]
    right_tag = len(series) - 1
    left_tag = 0
    while left_tag < right_tag:
        if series[right_tag] < tag:
            if series[left_tag] > tag:
                series[left_tag], series[right_tag] = series[right_tag], series[left_tag]
            left_tag += 1
        else:
            right_tag -= 1
    series[0], series[left_tag] = series[left_tag], series[0]
    return series


def quick_sort_1(series, left, right):
    '''快速排序, 直接使用原列表排序'''
    if not isinstance(series, list):
        print('请输入列表')
        return
    tag = series[left]
    right_tag = right
    left_tag = left
    while left_tag < right_tag:
        if series[right_tag] < tag:
            if series[left_tag] > tag:
                series[left_tag], series[right_tag] = series[right_tag], series[left_tag]
                right_tag -= 1
            else:
                left_tag += 1
        else:
            right_tag -= 1
    series[left], series[left_tag] = series[left_tag], series[left]
    if left <= left_tag - 1:
        quick_sort_1(series, left, left_tag-1)
    if left_tag + 1 <= right:
        quick_sort_1(series, left_tag+1, right)


if __name__ == '__main__':
    # print(quick_sort([6, 1, 2, 7, 9, 3, 4, 5, 10, 8]))
    series = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort_1(series, 0, len(series)-1)
    print(series)
    # print(quick_sort([6, 1, 2, 3]))
