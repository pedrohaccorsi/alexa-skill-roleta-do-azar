import random
from   OutputBuilder import OutputSpeachBuilderFactory

class RouleteHandler():

    def __init__(self, roulete):
        self.rouleteName  = roulete["name"]
        self.rouleteItems = roulete["items"]
        self.numOfItems   = len(self.rouleteItems)

    def run(self):
        return ( 
            getOutputSpeech(
                getRandomItem()
            )
        )
        
    def getRandomItem(self, ignore=[]):
        return self.rouleteItems[ random.randint(0, numOfItems-1  ) ]

    def getResponseType(self):
        luckyFactor = random.randint(1, 20)
        for _ in range (luckyFactor):
            responseType = random.randint(1, 16)  
        return responseType


    def getOutputSpeech(self, selected_item):
        return ( 
            OutputSpeachBuilderFactory()
                .make(
                    getResponseType(),
                    self.rouleteItems, 
                    selected_item
                )
                .get()
        
        )
