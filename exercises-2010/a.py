year = int(input("Digite o ano: "))
num_sign = year % 12
match num_sign:
    case 0:
        print("rato")
    case 1:
        print("boi")
    case 2:
        print("tigre")
    case 3:
        print("coelho")
    case 4:
        print("dragao")
    case 5:
        print("serpente")
    case 6:
        print("cavalo")
    case 7:
        print("carneiro")
    case 8:
        print("macaco")
    case 9:
        print("galo")
    case 10:
        print("cao")
    case 11:
        print("porco")