@@ -0,0 +1,27 @@
#Task1

def format_ex(n,s):
    result=f"Number :{n}, String : {s}"
    print(result)
    print("The result is printed using formatted format")
format_ex(145,'o')


#Task2

radius= 84
pi = 3.14
area = pi * (radius ** 2)
print("Area of pond:", int(area))
# Water calculations
water_per_sqm = 1.4
total_water = area * water_per_sqm
print("Total water in pond :", int(total_water))

#Task3

distance = 490 
time_min = 7
time_sec= time_min * 60
speed = distance / time_sec
print("Speed:", int(speed),"m/s")
