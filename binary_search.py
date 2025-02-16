_list = [12,34,78,90,345,676]
n=int(input("Enter the target:"))
if n not in _list:
        print(n,"not in list")

low=0
high=5
mid=0
while n!=_list[mid]:
        mid = int((low+high)/2)
        if _list[mid]==n:
	        break
        elif n>_list[mid]:
	        low=mid+1
        elif n<_list[mid]:
	        high=mid-1
print(n,"at",mid)

