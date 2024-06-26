import sys

def kok(a,b,c):
    delta = b ** 2 - 4 * a * c
    if(delta < 0):
        print("Reel kok yok..")
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kok bulma", kok(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru rakam girin..")
    sys.stderr.flush()

    # 1. check
    
