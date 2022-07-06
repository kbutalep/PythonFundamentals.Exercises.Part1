#Create a Python script called *fahrenheit_to_celsius.py*

#* The script should declare a variable called fahrenheit.
#* The script should then convert the value of fahrenheit to celsius.
#* The conversion should be displayed on the screeen in the following format:
#"32 degrees fahrenheit is equal to 0.0 degree(s) celsius"


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8000
    print(str(fahrenheit) + " degrees fahrenheit is equal to " + str(celsius) + " degree(s) celsius")

fahrenheit_to_celsius(32)

