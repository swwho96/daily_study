def calculate(hours, rate):
    while True:
        try:
            hours = float(hours)
            rate = float(rate)
            break
        except ValueError:
            print("잘못된 값을 입력하셨습니다.")
    if hours > 40:
        print("Overtime Working")
        pay = (40 * rate) + (hours - 40) * (rate * 1.5)
        print("이번달 급여는 ", pay, "원 입니다.")
    else:
        print("Regular Working")
        pay = hours * rate
        print("이번달 급여는 ", pay, "원 입니다.")



a = input("Enter Hours: ")
b = input("Enter Rate: ")
calculate(a, b)
