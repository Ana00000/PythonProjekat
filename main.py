import insertingQuery
import searchOfDocuments
import parsingDocuments
import trie
import time


if __name__ == '__main__':

    loop1 = "1"
    loop2 = "1"
    root = trie.TrieNode("*")
    logical_op = ""
    search = []

    while loop1 == "1":

        if loop2 == "1":

            while True:

                root_dir = input("Unesite korenski direktorijum: \n")
                beginning = time.time()
                (success, root) = parsingDocuments.parsing(root_dir)
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

                    print(konacan_set)
                    print(konacan_recnik)
                    print("\n")

            else:

                print("Neuspesno je unet upit. \n")

            loop2 = input("Opcije:\n 1 - Unesite,ponovo,korenski direktorijum: \n "
                          "2 - Unesite upit: \n 3 - Izlazak iz programa.\n")

        elif loop2 == "3":

            loop1 = "-1"
            print("Izlazak iz programa.")

        else:

            loop2 = input("Morate uneti opciju 1,2 ili 3. \n")
