@@ -0,0 +1,41 @@
# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("1.Number of members : ",len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2.After adding members")
print(justice_league)


# 3. Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3.Wonder Woman as leader")
print(justice_league)


# 4. Separate Aquaman and Flash
# Insert "Superman" between them (or Green Lantern)
justice_league.remove("Superman")
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash, "Superman")
print("\n4.After separating Aquaman and Flash")
print(justice_league)


# 5. Replace entire list
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5.New team")
print(justice_league)


# 6. Sort alphabetically
justice_league.sort()
print("\n6.Sorted list")
print(justice_league)
print("\nNew Leader:", justice_league[0])
