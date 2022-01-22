lst1 = [1,3,4,5]
n = len(lst1)
expected_total =(n+1)*(n+2) // 2
actual_total = sum(lst1)

missing_number = expected_total - actual_total
print(missing_number)