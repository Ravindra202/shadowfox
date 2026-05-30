@@ -0,0 +1,45 @@
#Task1-dice

import random
rolls = 20
count_6 = 0
count_1 = 0
consecutive_6 = 0
prev_roll = 0
for i in range(rolls):
    roll = random.randint(1, 6)
    print("Roll",i+1,":",roll)
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and prev_roll == 6:
        consecutive_6 += 1
    prev_roll = roll
    
print("\nResults:")
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Consecutive 6s:", consecutive_6)



#Task2-Jumping jacks

total = 100
done = 0
while done < total:
    print("Do 10 jumping jacks")
    done += 10
    if done >= total:
        print("Congratulations! You completed the workout")
        break
        
    tired = input("Are you tired? (yes/no): ").lower()
        
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip remaining? (yes/no): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of ",done," jumping jacks")
            break
print((total - done),"jumping jacks remaining")
