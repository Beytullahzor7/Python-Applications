with open("futbolcular.txt","r",encoding="utf-8") as file:

    Galatasaray=list()
    Beşiktaş=list()
    Fenerbahce=list()

    for satır in file:

        satır = satır[:-1]

        liste = satır.split(",") #satırlarda yer alan virgül ile ayrılmıs kısımları kendi içinde listeleştirir.

        oyuncuismi = liste[0]
        if len(liste) == 1:
            continue

        takim = liste[1]

        if (takim == "Galatasaray"):

            Galatasaray.append(oyuncuismi + "\n")

        elif (takim == "Beşiktaş"):

            Beşiktaş.append(oyuncuismi + "\n")

        else:
            Fenerbahce.append(oyuncuismi + "\n")


        with open("Galatasaray.txt","w",encoding="utf-8") as file:

            for i in Galatasaray:
                file.write(i)

        with open("Beşiktaş.txt","w",encoding="utf-8") as file:

            for i in Beşiktaş:
                file.write(i)

        with open("Fenerbace.txt","w",encoding="utf-8") as file:

            for i in Fenerbahce:
                file.write(i)




