
import random
from sorting.bubble_sort_optimized import bubble_sort_optimizedf
from sorting.bubble_sort import bubble_sortf
from sorting.isertion_sort import insertion_sortf
from sorting.selection_sort import selection_sortf
from searching.binary_search import binario
from searching.linear_search import linear_search
from recursion.countdown import regresiva
from recursion.factorial_of_n import factorial
from recursion.nth_fibonacci_number import fibo
from recursion.sum_of_first_n_nums_recursion import sum_n
from lists.largest_number_in_list import large_small
from lists.list_merge import combinacion
from brute_force.divisors_of_n import divisor
from brute_force.pin_unlock import unlock
from brute_force.sum_of_first_n_sums import sum_n_n

print("---Testing of algorithms---,","\n","\n")

#SORTING
print("-----sorting-----")
arr = [9, 5, 4, 7, 10, 14, 15, 13, 8, 2]
arr2 = [8, 5, 7, 8, 9, 10, 5 ,7, 3, 2]
print("input for all sorting: ",arr, "\n")

print("******bubble sort optimized******")
print("output: ", bubble_sort_optimizedf(arr), "\n")

print("******bubble sort******")
print("output: ", bubble_sortf(arr), "\n")

print("******insertion_sort******")
print("output: ", insertion_sortf(arr), "\n")

print("******selection_sort******")
print("output: ", selection_sortf(arr), "\n","\n")


#SEARCHING
print("-----searching-----")
arr = [9, 5, 4, 7, 10, 14, 15, 13, 8, 2]
arr2 = [8, 5, 7, 8, 9, 10, 5 ,7, 3, 2]
print("******binary search******")
print("input: ", arr, " and 5 ")
if binario(arr,4) == -1:
    ans = "el número no se encuentra en la lista"
else:
    ans = ("el número se encuentra en el indice: ",binario(arr,4))
print("output: ", ans,"\n")

print("******linear search******")
print("input: ", arr2, " and 4 ")
if linear_search(arr2,4) == -1:
    ans = "el número no se encuentra en la lista"
else:
    ans = "el número se encuentra en el indice: ",linear_search(arr2,4)
print("output: ", ans,"\n","\n")


#RECURSION
print("-----Recursion-----")
arr = [9, 5, 4, 7, 10, 14, 15, 13, 8, 2]
arr2 = [8, 5, 7, 8, 9, 10, 5 ,7, 3, 2]
print("******countdown******")
print("input: 3")
print("output: ")
print(regresiva(3), "\n")

print("******factorial_of_n******")
print("input: 4")
print("output: ", factorial(4),"\n")

print("******nth_fibonacci_number******")
print("input: 8" )
print("output: ", fibo(8),"\n")

print("******sum_of_first_n_nums_recursion******")
print("input: 10")
print("output: ", sum_n(10), "\n","\n")


#LISTS
print("-----lists-----")
print("******largest_number_in_list******")
randomlist = random.sample(range(1, 1000), 20)
print("input:", randomlist)
print("output: ")
print(large_small(randomlist), "\n")

print("******list_merge******")
list1 = [1,4,9]
list2 = [2,3,8]
print("inputs : ",list1, " and ", list2)
print("output: ", combinacion(list1,list2),"\n","\n") 


#BRUTE FORCE
print("-----brute_force-----")
print("******divisors_of_n******")
print("input: 893" )
print("output: ", divisor(893),"\n")

print("******pin_unlock******")
print("input: 4004" )
print("output: ", unlock("4004"),"\n")

print("******sum_of_first_n_sums******")
print("input: 50" )
print("output: ", sum_n_n(50),"\n")
