def erro(x):
    try:
        eval(x)
    except (TypeError,NameError) as e:
        print(type(e))
    except ValueError as e:
        print(type(e))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("nenhum erro")
    finally:
        print("sempre sera executado")

#TypeError
erro("int+int")
#NameError
erro("a")
#ValueErrorf
erro("int('a')")
#ZeroDivisionError
erro("5/0")
erro("10+10")

print("a aplicação foi finalizada")
