import random
import copy

def init(n, max_nmr, min_nmr):
    """
    Maakt een lijst met random getallen aan. En een lijst in roster-stijl voor de bucket sort.

    @param       n: lengte van de lijst met random getallen
    @param max_nmr: grootste waarde dat een random getal kan aannemen
    @param min_nmr: kleinste waarde dat een random getal kan aannemen
    @return       : de twee aangemaakte lijsten
    """
    one_dimensional = [random.randint(min_nmr, max_nmr) for i in range(n)]
    # two_dimensional = [ [x, [None for x in range(n-1)]] for x in range(10) ]
    two_dimensional = [ [x, []] for x in range(10) ] # maak een roster aan met 9 rijen. elke rij heeft een lijst waarin de gesorteerde getallen komen te staan

    return one_dimensional, two_dimensional


def sorter(to_sort, bucket, tiental, slice_at):
    """ 
    Deze functie voert de sortering in de bucket uit. 

    @param  to_sort: de ongesorteerde lijst die gesorteert moet worden
    @param   bucket: het roster waarin de getallen worden verdeeld
    @param  tiental: geeft aan of het algoritme bij een tiental, honderdtal etc. is
    @param slice_at: dit geeft aan op welk cijfer in een getal de focus ligt.
    @return        : een bewerkte lijst na één ronde sortering van de originele lijst
    """
    
    new_list = []

    for i in to_sort:
        if i < tiental:     
            bucket[0][1].append(i)
        elif slice_at == 1:
            unit = int(str(i)[-1:])
            bucket[unit][1].append(i)
        else:
            unit = int(str(i)[-(slice_at):-(slice_at - 1)])
            bucket[unit][1].append(i)
    
    for x in range(0, 10):
        new_list.extend(bucket[x][1])

    return new_list
        

def bucket_sort():
    """
    De main functie die de bucket-sort uitvoert tot dat er een van klein naar groot gesorteerde lijst is.

    @return: een van klein naar groot gesorteerde lijst.
    """

    # hier wordt de gebruiker gevraagd om input te geven
    # TODO: errors & verkeerde inputs opvangen. een aparte functie van maken
    lenght_list = int(input("Geef de lengte van de lijst aan:"))
    max_nmr     = int(input("Geef de maximale grootte van de getallen aan:"))
    min_nmr     = int(input("Geef de minimale grootte van de getallen aan:"))
    
    # de te sorteren lijst wordt aangemaakt + het rooster waar in gesorteerd wordt. De lijst wordt vereeld in positieve en negatieve getallen
    to_sort, bucket = init(lenght_list, max_nmr, min_nmr)
    positive_list = list(i for i in to_sort if i >= 0)
    negative_list = list(i * -1 for i in to_sort if i < 0) 


    print(f"De random gegenereerde lijst is: {to_sort}. \nDe lijst wordt nu gesorteerd..")


    # een paar variabele moeten aangemaakt worden die het algoritme later nodig heeft
    clean_bucket = copy.deepcopy(bucket)    # creeer een deepcopy van een lege bucket om te hergebruiken
    tiental = 1                             # geeft aan of het algoritme bij een tiental, honderdtal etc. is
    slice_at = 1                            # variabele om de juiste cijfer in een getal aan te wijzen bij het sorteren
    max_tiental = len(str(max(list(abs(i) for i in to_sort))))    # om ervoor te zorgen dat er tot en met het grootste getal wordt gesorteerd


    # loop die het algoritme uitvoert
    for i in range(0, max_tiental):
        bucket = copy.deepcopy(clean_bucket)    # maak de bucket schoon


        positive_list = sorter(positive_list, bucket, tiental, slice_at)  # sorteer positieve getallen
        bucket = copy.deepcopy(clean_bucket)    # maak de bucket schoon
        negative_list = sorter(negative_list, bucket, tiental, slice_at)  # sorteer negatieve getalle

        
        tiental *= 10   # na elke gathering pass ga je naar de volgende tiental. 10 -> 100 -> 1000
        slice_at += 1   # na elke gathering pass verschuift de focus één cijfer naar links. 
    

    # lijst met negatieve getallen wordt gereversed om de juiste volgorde te krijgen, en wordt samengevoegd met de positieve lijst om tot een eindresultaat te komen
    negative_list = list(i * -1 for i in list(reversed(negative_list)))
    to_sort = negative_list + positive_list

    print(f"De lijst is succesvol gesorteerd! Dit is het resultaat: {to_sort}")


    return to_sort

bucket_sort()