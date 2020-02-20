import parsingDocuments
import insertingQuery
import searchOfDocuments

if __name__ == '__main__':

    loop = 1
    i = 0
    state = 0
    root = ""

    while loop == 1:

        if i == 0:

            state = 1
            i = -1

        if state == 1:

            root_dir = input("Unesite korenski direktorijum: \n")
            (success, root) = parsingDocuments.parsing(root_dir)

            if success:

                print("Uspesno su parsirana dokumenta. \n")

            else:

                print("Neuspesno su parsirana dokumenta. \n")

        elif state == 2:

            query = input("Unesite upit: \n")
            (correct, logical_op, search) = insertingQuery.parse(query)

            if correct:

                print("Uspesno je unet upit. \n")
                [konacan_set, konacan_recnik] = searchOfDocuments.find(root, logical_op, search)

                if not konacan_recnik:

                    print("Nije pronadjena nijedna rec! \n")

                else:

                    print("Reci su pronadjene. \n")
                    print(konacan_set)
                    print(konacan_recnik)

            else:

                print("Neuspesno je unet upit. \n")

        elif state == 3:

            loop = -1
            print("Izlazak iz programa. \n")

        else:

            print("Morate uneti opciju 1,2 ili 3. \n")

        state = input("Opcije:\n 1 - Unesite,ponovo,korenski direktorijum: \n 2 - Unesite upit: \n 3 - Izlazak iz programa.\n")
