#String Built-in Methods

str1 = "python"
print(str1.capitalize())

str2 = "python program"
print(str2.title())

str3 = "Computer Science"
print(str3.istitle())

str4 = "SHiva"
print(str4.lower())

print(str4.upper())

str5 = "pythonbytecode"
print(str5.islower())

print(str5.isupper()) #False

str6 = "HRINTERN"
print(str6.isupper())

str7 = "PyThon"
print(str7.swapcase())

str8 = "shiva"
print(str8.startswith("s"))

print(str8.endswith("va"))

str9 = " hello "
print(str9)
print(str9.strip())

str10 = "Hello   "
print(str10)
print(str10.rstrip())

str11 = "   Hello"
print(str11)
print(str11.lstrip())

print(str11.count("l"))

print(str11.index("l"))

print(str11.rindex("l"))

print(str10.find("e"))

print(str10.rfind("l"))

print("_name".isidentifier())

print("Hello".isalpha())

print("Hello123".isalnum())

print("  ".isspace())

print("Shiva".split())

print(",".join(["Shiva","Python Full Stack Dev"]))

print("python".center(10,"*"))
