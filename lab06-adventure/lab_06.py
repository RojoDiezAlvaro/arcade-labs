class Room:
    def __init__(self,desc,n,e,s,w):
        self.description = desc
        self.north = n
        self.east = e
        self.south = s
        self.west = w

def main():
    room_list = []
    current_room = 0
    done = False
    anillo = False
    room = Room(
        "Ves la entrada de la mansión, hay una puerta reforzada hacia el este, una puerta tosca hacia el oeste y un arco que conduce hacia el sur",
        None,2,4,1)
    room_list.append(room)
    room = Room(
        "Estas en una despensa llena de comida, chorizos y jamones cuelgan del techo y las paredes estan llenas de quesos en distintos estados de maduración, en direccion sur ves una puerta manchada de grasa, una puerta tosca te espera al este",
        None, 1, 3, None)
    room_list.append(room)
    room = Room(
        "Tras atravesar la puerta reforzada llegas a una armeria, lanzas con marcas de oxido y alabardas melladas pueblan las paredes y te llama la atencion una armadura en un maniquí, es lo unico que brilla de la estancia, solamente puedes volver por la puerta reforzada hacia el oeste",
        None, None, None, 1)
    room_list.append(room)
    room = Room(
        "Has llegado a las cocinas, una olla burbujea sobre el fuego y un enorme hacha de cocina esta clavada en la mesa, ves una puerta grasienta hacia el norte y otra, mas limpia, hacia el sur",
        0, None, 5, None)
    room_list.append(room)
    room = Room(
        "Te encuentras en unos tetricos jardines, los arboles, como retorcidos de dolor, tienen las raices llenas de hongos y exceptuando un camino que lleva desde el arco al norte hacia una puerta reforzada al sur, gran parte de los jardines están cubiertos de charcos verdosos",
        1, None, 6, None)
    room_list.append(room)
    room = Room(
        "Ves un enorme salón de banquetes, iluminado por varios candelabros y una chimenea en un extremo, pese a las llamas, parece estar helado, tienes una puerta hacia el norte y una puerta reforzada hacia el este",
        3, 6, None, None)
    room_list.append(room)
    room = Room(
        "Estas en una sala de guardia, barricadas con clavos oxidados apuntan hacia las puertas reforzadas en todas las direcciones, excepto hacia la puerta del sur, que parece que protegen",
        4, 7, 8, 5)
    room_list.append(room)
    room = Room(
        "Llegas a una mazmorra, cadenas y grilletes cubren pareces y techo y marcas de sangre seca y otras mucho mas recientes vuelven el suelo resbaladizo, afortunadamente no hay nadie, tienes una puerta reforzada hacia el oeste",
        None, None, None, 6)
    room_list.append(room)
    room = Room(
        "Estas en la habitación principal de la mansión, ves una gran cama con dosel en una pared y varias literas en el otro extremo de la habitación, como si se intentasen mantener lo mas alejadas posible,ves el anillo del conde sobre la mesa, rapidamente lo coges, es hora de escapar, la única salida es la puerta hacia el norte",
        6, None, None, None)
    room_list.append(room)
    while not done:
        print()
        if current_room == 1 and anillo:
            print("Consigues llegar hasta el gran portico con el anillo. Felicidades, hsas escapado de la mansión")
            done = True
        else:
            print(room_list[current_room].description)

            if current_room == 8:
                anillo = True

            print("¿En qué dirección quieres ir?")

            direccion: str = input()

            if direccion.lower() == "n" or direccion.lower() == "norte":
                next_room = room_list[current_room].north
                if next_room is None:
                    print("No puedes ir en esa dirección")
                else:
                    current_room = next_room

            elif direccion.lower() == "e" or direccion.lower() == "este":
                next_room = room_list[current_room].east
                if next_room is None:
                    print("No puedes ir en esa dirección")
                else:
                    current_room = next_room

            elif direccion.lower() == "s" or direccion.lower() == "sur":
                next_room = room_list[current_room].south
                if next_room is None:
                    print("No puedes ir en esa dirección")
                else:
                    current_room = next_room

            elif direccion.lower() == "o" or direccion.lower() == "oeste":
                next_room = room_list[current_room].west
                if next_room is None:
                    print("No puedes ir en esa dirección")
                else:
                    current_room = next_room

            else:
                print("Esa dirección no es valida")
    quit()


main()
