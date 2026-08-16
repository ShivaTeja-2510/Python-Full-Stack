# Simulating OTP verification
correct_otp = "7890"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    entered_otp = input("Enter OTP: ")
    if entered_otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")
        attempts += 1

else:
    print("OTP expired. Request a new one.")