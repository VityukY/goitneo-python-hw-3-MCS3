from datetime import datetime

# Date as a string
dateString = "02-July-2023"


# Converting string date into datetime object
dateTimeObj = datetime.strptime(dateString, "%d-%B-%Y")
print(f"Date as {type(dateTimeObj)} is {dateTimeObj}")
