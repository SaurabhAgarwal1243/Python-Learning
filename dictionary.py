#Dictionary is a datatype which allows user to store data in key value pair
#"Key": "Value"
#key should always be unique

month_convert = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_convert["Nov"])     #accessing dictionary value using key

print(month_convert.get("Dec")) #accessing using get function

print(month_convert.get("ooo", "Not a valid Key"))      #get function helps in providing a usecase where passed key is not present in dictionary.
