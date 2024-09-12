import time

devices = ["iphone", "android", "radio", "tv", "tablet", "pc", "laptop"] * (10**7)

user_input = input("Enter name:\n").lower()

start_time = time.perf_counter()

if user_input in devices:
    print(f"{user_input} is in the list.")
else:
    print(f"{user_input} is not in the list.")

end_time = time.perf_counter()

time = end_time - start_time

print(f"Time taken to check: {time:.10f} seconds")
