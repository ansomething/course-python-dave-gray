# dictionaries

band = {"vocals": "Plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/values pairs as tuples
print(band.items())

# verify if key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

print("")
band2 = band.copy()
band2["drums"] = "Dave"
print(band2)
print(band)

# or use the dict() constructor function
band3 = dict(band)
print(band3)
print("")

# nested dictionaries

member1 = {"name": "Plant", "instrument": "vocals"}

member2 = {"name": "Page", "instrument": "guitar"}

band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])

# sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

nums3 = {1, 2, 2, 3}
print(nums3)

nums4 = {1, True, 2, False, 3, 4, 0}
print(nums4)

# check if a value is in a set

print(1 in nums4)

# add a new element to a set
nums4.add(8)
print(nums4)

# add elements from one set to another
nums5 = {5, 6, 7}
nums4.update(nums5)
print(nums4)

# you can use update with lists, tuples, and dictionaries

# merge two sets to create a new set

one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)