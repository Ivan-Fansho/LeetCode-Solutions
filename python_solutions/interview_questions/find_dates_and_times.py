import re

text = "Hi, my name is Jane and my phone number is 555-123-4567. My email address is jane_doe@example.com. I live on 123 Main St. Apt. #456, and I was born on January  11th, 1990. I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/ 05/21. Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting sometime in June. I would love June 19th around 14:00.Thank you!"

date = r'(\b\d{4}\s*[-/]\s*\d{1,2}\s*[-/]\s*\d{1,2}\b|\b\d{1,2}(?:th|st|nd|rd)?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:th|st|nd|rd)?(?:,\s+\d{4})?)'
time = r'(\b\d{1,2}:\d{2}(?:am|pm)?\b|\b\d{1,2}:\d{2}\b)'

dates = []
times = []

pos = 0
while pos < len(text):
    match = re.search(date, text[pos:])
    if match:
        dates.append(match.group(0))
        pos += match.end()
    else:
        break

pos = 0
while pos < len(text):
    match = re.search(time, text[pos:])
    if match:
        times.append(match.group(0))
        pos += match.end()
    else:
        break

print("Dates:")
for date in dates:
    print(date)

print("Times:")
for time in times:
    print(time)
