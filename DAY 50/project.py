red = int(input("Enter red balls: "))
blue = int(input("Enter blue balls: "))
green = int(input("Enter green balls: "))

if red < 0 or blue < 0 or green < 0:
    print("Ball counts cannot be negative.")
total = red + blue + green
if total == 0:
    print("The bag must contain at least one ball.")
    
red_probability = red / total
blue_probability = blue / total
green_probability = green / total

print("\nTotal balls:", total)
print(f"Red: {red_probability:.2%}")
print(f"Blue: {blue_probability:.2%}")
print(f"Green: {green_probability:.2%}")