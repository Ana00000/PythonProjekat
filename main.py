import insertingQuery
import searchOfDocuments
import parsingDocuments
import trie
import time
from Graph import Graph
graph = None


def rangiranje(konacan_set, konacan_recnik):
    global graph
    rangovi_putanje = {}
    konacan_set = konacan_set.stranice

    # rangiranje po broju pojavljivanja reci
    for putanja in konacan_set:
        for putanja2 in konacan_recnik.keys():
            if putanja == putanja2:
                if putanja in rangovi_putanje.keys():
                    rangovi_putanje[putanja] = rangovi_putanje.get(putanja) + konacan_recnik.get(putanja)
                else:
                    rangovi_putanje[putanja] = konacan_recnik.get(putanja2)

    for putanja in rangovi_putanje.keys():
        rangovi_putanje[putanja] = rangovi_putanje.get(putanja)*0.3

    # rangiranje na osnovu broja linkova na tu stranicu
    rang1 = {}

    for putanja in rangovi_putanje.keys():
        for vertex in graph.vertices():
            if vertex.get_path() == putanja:
                if putanja in rang1.keys():
                    rang1[putanja] = rang1.get(putanja) + graph.edge_count(vertex)
                else:
                    rang1[putanja] = graph.edge_count_v(vertex)

    for putanja in rang1.keys():
        rangovi_putanje[putanja] = rangovi_putanje.get(putanja) + rang1.get(putanja)*0.2


    # rangiranje na osnovu stranica koje imaju link na taj hrml i sadrze trazenu rec
    rang2 = {}
    for putanja in rangovi_putanje.keys():
        for vertex in graph.vertices():
            if vertex.get_path() == putanja:

                if putanja not in rang2.keys():
                    rang2[putanja] = 0

                putanje_in = graph.putanje_in(vertex)
                for put in putanje_in:
                    if put in konacan_set:
                        rang2[putanja] = rang2.get(putanja) + 1

    for putanja in rang2.keys():
        rangovi_putanje[putanja] = rangovi_putanje.get(putanja) + rang1.get(putanja)*0.5

    return rangovi_putanje


def sort(rangovi_putanje):
    rangovi = []
    for putanja in rangovi_putanje.keys():
        rangovi.append(rangovi_putanje.get(putanja))

    rangovi = list(set(rangovi))

    merge_sort(rangovi)


    for rang in rangovi:
        for putanja in rangovi_putanje.keys():
            if rangovi_putanje.get(putanja) == rang:
                print("%6.3f" % rangovi_putanje.get(putanja), "\t", putanja)

def merge(left, right, arr):
    i = j = k = 0

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Python program for implementation of MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        merge(left, right, arr)  # merge sorted sub-arrays

def main_menu():
    global graph
    loop1 = "1"
    loop2 = "1"
    root = trie.TrieNode("*")
    logical_op = ""
    search = []

    while loop1 == "1":

        if loop2 == "1":

            while True:
                graph = Graph()

                root_dir = input("Unesite korenski direktorijum: \n")
                beginning = time.time()
                (success, root, graph) = parsingDocuments.parsing(root_dir)
                ending = time.time()
                tik = ending - beginning

                if success:

                    print("Uspesno su parsirana dokumenta. \n")
                    print("Vreme za parsiranje je bilo: \n", tik, " \n")
                    break

                else:

                    print("Neuspesno su parsirana dokumenta. \n")
                    print("Vreme za pokusaj parsiranja je bilo: \n", tik, " \n")

            loop2 = input("Opcije:\n 1 - Unesite,ponovo,korenski direktorijum: \n"
                          " 2 - Unesite upit: \n 3 - Izlazak iz programa.\n")

        elif loop2 == "2":

            correct = False

            while not correct:

                query = input("Unesite upit: \n")
                (correct, logical_op, search) = insertingQuery.parse(query)

            if correct:

                print("Uspesno je unet upit. \n")
                [konacan_set, konacan_recnik] = searchOfDocuments.find(root, logical_op, search)

                if not konacan_recnik:

                    print("Nije pronadjena nijedna rec! \n")

                else:

                    print("Reci iz upita su pronadjene. \n")

                    #RANGIRANJE STRANICA IZ KONACAN_SET

                    print('##################################################')
                    print(konacan_set)
                    print('##################################################')
                    print(konacan_recnik)
                    #print("\n")

                    rangovi_putanje = rangiranje(konacan_set, konacan_recnik)


                    sort(rangovi_putanje)
                    print('##################################################')


            else:

                print("Neuspesno je unet upit. \n")

            loop2 = input("Opcije:\n 1 - Unesite,ponovo,korenski direktorijum: \n "
                          "2 - Unesite upit: \n 3 - Izlazak iz programa.\n")

        elif loop2 == "3":

            loop1 = "-1"
            print("Izlazak iz programa.")

        else:

            loop2 = input("Morate uneti opciju 1,2 ili 3. \n")


if __name__ == '__main__':
    main_menu()
