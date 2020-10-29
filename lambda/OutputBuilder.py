import random 

class OutputSpeachBuilder_00():

    def __init__(self, items, selected_item):
        self.items         = items
        self.selected_item = selected_item
        self.numOfItems    = len(items)

    def getRandomItem(self, ignore=[]):
        item = self.items[ random.randint(0, self.numOfItems)-1]
        while( item in ignore ):
            item = self.items[ random.randint(0, self.numOfItems)-1]
        return item 

class OutputSpeachBuilder_01(OutputSpeachBuilder_00):
    
    def get(self):
        new_selected_item = self.getRandomItem( ignore = [self.selected_item] )
        return( f'O sortuto da vez é: {self.selected_item} ... não, pensando bem, mudei de ideia... dessa vez é o {new_selected_item}' )
            
class OutputSpeachBuilder_02(OutputSpeachBuilder_00):

    def get(self):
        return ( f'O sortudo é o... , {self.selected_item} !'  )

class OutputSpeachBuilder_03(OutputSpeachBuilder_00):
    
    def get(self):
        return ( f'Com 53 por cento dos votos, ... , ... {self.selected_item}, é você!' )

class OutputSpeachBuilder_04(OutputSpeachBuilder_00):
    
    def get(self):
        return( f'A decisão é unânime: {self.selected_item}' )

class OutputSpeachBuilder_05(OutputSpeachBuilder_00):
    
    def get(self):
        return ( f'Nessa não preciso nem pensar, claro que é o {self.selected_item}' )

class OutputSpeachBuilder_06(OutputSpeachBuilder_00):

    def get(self):
        selected_item_2 = self.getRandomItem(ignore = [self.selected_item])
        selected_item_3 = self.getRandomItem(ignore = [self.selected_item, selected_item_2])
        return ( f'Tô meio dividida entre {self.selected_item} e {selected_item_2}, na dúvida, vou de {selected_item_3}' )

class OutputSpeachBuilder_07(OutputSpeachBuilder_00):
    
    def get(self):
        selected_item_2 = self.getRandomItem(ignore = [self.selected_item])
        return ( f'Par ou ímpar entre {self.selected_item} e {selected_item_2}' )

class OutputSpeachBuilder_08(OutputSpeachBuilder_00):

    def get(self):
        return self.selected_item

class OutputSpeachBuilder_09(OutputSpeachBuilder_00):
    
    def get(self):
        selected_item_2 = self.getRandomItem(ignore = [self.selected_item])
        return f'hmmm... se o ítem {self.selected_item} foi sorteado alguma vez nos últimos 3 dias, então é {selected_item_2}, mas se não, {chosen}'

class OutputSpeachBuilder_10(OutputSpeachBuilder_00):
    
    def get(self):
        return ( f'O sortudo é o... , {self.selected_item} !'  )

class OutputSpeachBuilder_11(OutputSpeachBuilder_00):

    def get(self):
        return ( f'O ítem {self.selected_item} tá meio suspeito, então vai ele mesmo' )

class OutputSpeachBuilder_12(OutputSpeachBuilder_00):

    def get(self):
        selected_item_2 = self.getRandomItem(ignore = [self.selected_item])
        return ( f'Eu eras mais {self.selected_item}, mas pedi a opinião do pessoal aqui e aí me convenceram... {selected_item_2}, é você' )

class OutputSpeachBuilder_13(OutputSpeachBuilder_00):
    
    def get(self):
        return ( f'É muito difícil dizer isso, mas... infelizmente... acho que... quem volta pra casa hoje... é você ... , ... , ... , , , ... , , ... , {self.selected_item}' )

class OutputSpeachBuilder_14(OutputSpeachBuilder_00):
    
    def get(self):
        return ( f'rra rra rra {self.selected_item}'  )

class OutputSpeachBuilder_15(OutputSpeachBuilder_00):

    def get(self):
        return ( f'Juro que calculei 3 vezes e caiu {self.selected_item} em todas' )

class OutputSpeachBuilder_16(OutputSpeachBuilder_00):
    
    def get(self):
        return'guga' if 'guga' in self.items else self.selected_item 

class OutputSpeachBuilderFactory():

    def make(self, responseType, items, selected_item):

        if responseType == 1 : return OutputSpeachBuilder_01(items, selected_item)
        if responseType == 2 : return OutputSpeachBuilder_02(items, selected_item)
        if responseType == 3 : return OutputSpeachBuilder_03(items, selected_item)
        if responseType == 4 : return OutputSpeachBuilder_04(items, selected_item)
        if responseType == 5 : return OutputSpeachBuilder_05(items, selected_item)
        if responseType == 6 : return OutputSpeachBuilder_06(items, selected_item)
        if responseType == 7 : return OutputSpeachBuilder_07(items, selected_item)
        if responseType == 8 : return OutputSpeachBuilder_08(items, selected_item)
        if responseType == 9 : return OutputSpeachBuilder_09(items, selected_item)
        if responseType == 10: return OutputSpeachBuilder_10(items, selected_item)
        if responseType == 11: return OutputSpeachBuilder_11(items, selected_item)
        if responseType == 12: return OutputSpeachBuilder_12(items, selected_item)
        if responseType == 13: return OutputSpeachBuilder_13(items, selected_item)
        if responseType == 14: return OutputSpeachBuilder_14(items, selected_item)
        if responseType == 15: return OutputSpeachBuilder_15(items, selected_item)
        if responseType == 16: return OutputSpeachBuilder_16(items, selected_item)