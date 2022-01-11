from Podpunkt_1 import *

if __name__ == '__main__':
    podpunkt_1 = Podpunkt_1()
    podpunkt_1.number_of_possibilities(0, 0, False, False)

    print("Opcje: " + str(podpunkt_1.counter))
    print("Prawdopodobieństwo: " + str(podpunkt_1.counter/6 ** 7))
    print("Prawdopodobieństwo: " + str(podpunkt_1.map_of_throws))

    podpunkt_1.reset_counter()
    podpunkt_1.reset_map()

    podpunkt_1.number_of_possibilities(3, 1, True, False)  # startujemy z trzeciego pola więc żółty jest na true
    print("Opcje: " + str(podpunkt_1.counter))
    print("Prawdopodobieństwo: " + str(podpunkt_1.counter / 6 ** 7))
    print("Prawdopodobieństwo: " + str(podpunkt_1.map_of_throws))




