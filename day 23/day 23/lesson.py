def welc(name):
    print("welcome " + name)
welc("nika")

def no_space(x):
    for i in x:
        if i == " ":
            x.remove(i)

    return x

no_space("asd dsd rsa")