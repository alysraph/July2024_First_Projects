numYears = 31
avgHeartBeats = 72

ageInDays = numYears * 365 + (numYears / 4)
print(ageInDays)
ageInHours = ageInDays * 24
print(ageInHours)
ageInMinutes = ageInHours * 60
print(ageInMinutes)
totalHeartBeats = ageInMinutes * avgHeartBeats
print("\n")

print("Did you know?\n")
print(f"Your heart has approximately beat {totalHeartBeats} over the span of your life so far.")
print(f"You are approximately {ageInDays} days old, not counting any leap years.")

