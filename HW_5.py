def check_elements_recursive(array, number):
    if len(array) == 0:
        return True

    if array[0] != number:
        return False


    return check_elements_recursive(array[1:], number)


arr = [1, 1, 1, 1]
num = 1

result = check_elements_recursive(arr, num)

if result:
    print("Все элементы массива совпадают с числом", num)
else:
    print("Не все элементы массива совпадают с числом", num)
input("press any key to close window")
