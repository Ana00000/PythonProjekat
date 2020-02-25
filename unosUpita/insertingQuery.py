from typing import List, Any


def parse(query):
    cases = ("AND", "OR", "NOT", "and", "or", "not")
    splitted_query = query.split(' ')
    first_part = splitted_query[0]
    logical_op = ""
    search: List[Any] = []

    if first_part == "AND" or first_part == "and":

        if len(splitted_query) == 1:

            print("Logicki operatori ne mogu stajati sami!")

        else:

            print("Logicki operatori AND i OR ne mogu biti na prvom mestu!")

        return False, logical_op, search

    elif first_part == "OR" or first_part == "or":

        if len(splitted_query) == 1:

            print("Logicki operatori ne mogu stajati sami!")

        else:

            print("Logicki operatori AND i OR ne mogu biti na prvom mestu!")

        return False, logical_op, search

    elif first_part == "NOT" or first_part == "not":

        if len(splitted_query) == 1:

            print("Logicki operatori ne mogu stajati sami!")

        else:

            print("Logicki operatori AND i OR ne mogu biti na prvom mestu!")

        return False, logical_op, search

    else:

        if len(splitted_query) == 1:

            logical_op = "OR"
            search.append(first_part)
            return True, logical_op, search

        else:

            second_part = splitted_query[1]

            if second_part in cases:

                if len(splitted_query) >= 4:

                    print("Na prvom mestu je rec,na drugom mestu je logicki operator,te upit moze imati jos samo "
                          "jednu rec!")
                    return False, logical_op, search

                else:

                    if len(splitted_query) == 3:

                        if splitted_query[2] in cases:

                            print("Ne mogu stajati dva logicka operatora jedan za drugim!")
                            return False, logical_op, search

                        else:

                            logical_op = second_part
                            search.append(splitted_query[0])
                            search.append(splitted_query[2])

                    else:

                        print("Ne mogu stajati samo jedna rec i log.operator!")
                        return False, logical_op, search

            else:

                for word in splitted_query:

                    if word in cases:

                        print("Logicki operator se ne moze naci ovde!")
                        return False, logical_op, search

                    else:

                        if len(splitted_query) >= 4:

                            print("U upitu ne moze biti vise od 3 reci!")
                            return False, logical_op, search

                        else:

                            logical_op = "OR"
                            search.append(word)

    return True, logical_op, search
