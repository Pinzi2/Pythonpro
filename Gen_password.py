import random
def gen(aaa):
    waos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = "".join(random.choice(waos)for i in range(aaa))
    print("La contraseña es",contra)
    return contra
nuevo = imput("Quieres crear una contraseña")
if nuevo == "si":
    cr7 = int(intput("Longitud clave:"))
    test = gen(cr7)
