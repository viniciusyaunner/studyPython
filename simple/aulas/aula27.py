num = 10
print(num)
def func():
    global num
    num = 50
    print(num)
func()
print(num)
