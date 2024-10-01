def main():
    num = int(input("Enter the range till where you want to print the Armstrong series: "))
    list_armstrong = []
    for i in range(1, num+1):
        str_i = str(i)
        calculation_1 = 0
        for j in str_i:
            calculation_1 += int(j) ** len(str_i)
        if calculation_1 == i:
                list_armstrong.append(calculation_1)
    print(list_armstrong)
main()