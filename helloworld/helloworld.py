import datetime

def helloworld(bestmusic = None, crabtime=None, polite=None):
    """
	Returns Hello world, determines what the best kind of music is, calculates time since the crab nebula supernova event, and politely exits.
    """

    print("hello, world! and hello to you too, user!")


    if bestmusic == "vaporwave":
        print("You are correct. Vaporwave is indeed the best genre of music.")
    	

    else:
    	print("Vaporwave is actually the best genre of music.")



    if crabtime:
    	crabdate = datetime.datetime(1054, 6, 4)
    	timesince = datetime.datetime.now() - crabdate
    	print("{} days since the Crab Nebula's supernova.".format(timesince.days))


    if not polite:
    	print("I'm out. Cheerio!")

    if polite:
    	print("Pleasure making your acquantaince, friend. Adieu!")