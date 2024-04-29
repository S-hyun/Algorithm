import sys

nums1 = list(map(int, sys.stdin.readline().rstrip().split()))
nums2 = list(map(int, sys.stdin.readline().rstrip().split()))
nums3 = list(map(int, sys.stdin.readline().rstrip().split()))

if sum(nums1)==3:
    print("A")
elif sum(nums1)==2:
    print("B")
elif sum(nums1)==1:
    print("C")
elif sum(nums1)==0:
    print("D")
elif sum(nums1)==4:
    print("E")

if sum(nums2)==3:
    print("A")
elif sum(nums2)==2:
    print("B")
elif sum(nums2)==1:
    print("C")
elif sum(nums2)==0:
    print("D")
elif sum(nums2)==4:
    print("E")

if sum(nums3)==3:
    print("A")
elif sum(nums3)==2:
    print("B")
elif sum(nums3)==1:
    print("C")
elif sum(nums3)==0:
    print("D")
elif sum(nums3)==4:
    print("E")

