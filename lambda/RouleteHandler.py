from OutSpeachBuilder import OutputSpeachBuilderFactory

class RouleteHandler():

    def __init__(self, roulette):
        self.rouleteName  = roulette["name"]
        self.rouleteItems = roulette["items"]
        self.numOfItems   = len(self.rouleteItems)

    def run(self):
        return ( self.getOutputSpeech( self.getRandomItem() ) )
        
    def getRandomItem(self, ignore=[]):
        return self.rouleteItems[ random.randint(0, self.numOfItems-1  ) ]


    def getOutputSpeech(self, selected_item):
        return ( 
            OutputSpeachBuilderFactory()
                .make( self.rouleteItems, selected_item )
                .get()
        )