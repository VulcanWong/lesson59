print("Hi! It me the LCM calculater, you can  call me lcm for short, you need to type in the highest and the smallest number:):):):):):):))):):):)")
h = int(input("Enter the highest number in your life : "))
s = int(input("Enter the smallest number in your life : "))
while(h):
    st = h
    h = s // h
    s = st
print("The LCM of the two Highest and the smallest numbers is___________:", s)
print("Ta da da daaaaaa")