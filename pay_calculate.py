hours = float(input("근무 시간을 입력하세요: "))
rate = float(input("시간당 급여를 입력하세요: "))

if hours > 40:
    print("Overtime Working")
    pay = (40 * rate) + (hours-40) * (rate * 1.5)
    print("이번달 급여는 ", pay, "원 입니다.")
else:
    print("Regular Working")
    pay = hours * rate
    print("이번달 급여는 ", pay, "원 입니다.")

