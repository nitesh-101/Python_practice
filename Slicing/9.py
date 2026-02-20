nums = [5, 6, 1, 2]

if len(nums) % 2 == 0:
    if nums[:2] == nums[-2:]:
        print("Slices are same")
    else:
        print("Slices are different")
else:
    print("Odd length list")