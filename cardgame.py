#Ilya Paley
#paley1

import wx
import random

class Card(object):
    ranks = {1:"Ace",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King"}
    suits = {"c":"Clubs","d":"Diamonds","h":"Hearts","s":"Spades"}
    royals = {"11":"j","12":"q","13":"k"}
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.image = Card.get_img(self)
    def __str__(self): 
        mysuit = self.suits[self.suit] 
        myrank = self.ranks[self.rank] 
        return myrank + " of "+mysuit
    def get_img(self):
        if self.rank < 11: 
            return wx.Image("cards_gif/"+self.suit+str(self.rank)+".gif",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        else:
            return wx.Image("cards_gif/"+self.suit+str(self.royals[str(self.rank)])+".gif",wx.BITMAP_TYPE_ANY).ConvertToBitmap()

class Pile(object):
    def __init__ (self, cards):
        self.cards=cards
    def add_card (self, card):
        self.cards.append(card)      
    def draw_card(self):
        return self.cards.pop()
    def top_card(self):
        return self.cards[0]
    def shuffle():
        random.shuffle(self.cards)

class Deck(Pile):
    def __init__(self):
        ranks=range(1,14)
        suits=["h","d","s","c"]
        self.cards=[]
        for a in ranks:
            for b in suits:  
                card=Card(a,b)
                self.add_card(card)
        super(Deck,self).__init__(self.cards)
        random.shuffle(self.cards)

class Hand(Pile):
    def is_flush(self):
        histogram={}
        suit_counter=0
        for card in self.cards:
            if card.suit not in histogram:
                suit_counter +=1
        if suit_counter==1:
            return True
        else:
            return False
    def is_straight(self):
        histogram=[]
        for card in self.cards:
            histogram.append(card.rank)
            histogram.sort()
        if histogram[0]+1==histogram[1] and histogram[1]+1==histogram[2] and histogram[2]+1==histogram[3] and histogram[3]+1==histogram[4]:
            return True
        else:
            return False
    def score(self):
        histogram={}
        score = 0
        for i in range(1,14):
            histogram[i]=0
            for card in self.cards:            
                if card.rank==[i]:
                    histogram[card.rank]+=1
        RanksCounter=0 
        for key in histogram:
            if histogram[key]!=0:
                RanksCounter+=1
        if RanksCounter==2:
            for key in histogram:
                if histogram[key]==4:
                    return 16
                if histogram[key]==3:
                    return 10             
        if RanksCounter==3:
            for key in histogram:
                if histogram[key]==3:
                    return 6
                if histogram[key]==2:
                    return 3
        if RanksCounter==4:
                return 1
        if RanksCounter==5:
            if self.is_straight()==True and self.is_flush()==True:
                if histogram[1]==1 and histogram[10]==1:
                    return 50
                return 30
            if self.is_flush()==True:
                return 5
            if self.is_straight()==True:
                return 12
            else:
                return 0
        if len(self.cards)!=5:
            raise ValueError
        return score()

class DeckButton(wx.BitmapButton):
    def __init__(self,parent):
        super(DeckButton,self).__init__(parent,-1)
        self.deck=Deck()
        top=self.deck.top_card()
        self.SetBitmapLabel(top.get_img())
    def draw_card(self):
        top=self.deck.draw_card()
        self.SetBitmapLabel(top.get_img())
        return top
    def restart(self):
        self.deck=Deck()
        top=self.deck.top_card()
        self.SetBitmapLabel(top.get_img())   

class CellButton(wx.BitmapButton):
    def __init__(self,parent):
        super(CellButton,self).__init__(parent)
        back=wx.Image("cards_gif/b1fv.gif",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.SetBitmapLabel(back)
        self.occupied=False
        self.card=None
    def add_card(self,x):
        self.card = x
        self.occupied = True
        self.SetBitmapLabel(self.card.get_img())
    def restart(self):
        self.occupied=False
        self.card=None
        self.SetBitmapLabel(card.get_img())

class Game(wx.Frame):
    def __init__(self):
        super(Game, self).__init__(None, -1, "Poker")
        self.cells = [[],[],[],[],[]]

        self.status=self.CreateStatusBar()
        self.status.SetStatusText("Score = 0")

        top = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.deck = DeckButton(top)
        self.cell = CellButton(top)
        sizer.Add(self.deck)
        sizer.Add(self.cell)
        self.Bind(wx.EVT_BUTTON, self.cell_clicked, self.cell)
        top.SetSizer(sizer)

        bottom = wx.Panel(self)
        sizer = wx.GridSizer(rows=5, cols=5)
        for i in range(5):
            for j in range(5):
                self.cells[i].append(CellButton(bottom))
                sizer.Add(self.cells[i][j])
                self.Bind(wx.EVT_BUTTON, self.place_card, self.cells[i][j])
        bottom.SetSizer(sizer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(top, 0, flag=wx.EXPAND)
        sizer.Add(bottom, 1, flag=wx.EXPAND)
        self.SetSizer(sizer)
        
        self.Show()
        self.Fit()

    def place_card(self, evt):
        for i in range(5):
            for j in range(5):
                if (self.cells[i][j].GetId() == evt.GetId()) and (self.cells[i][j].occupied is False):
                    card = self.deck.draw_card()
                    self.cells[i][j].add_card(card)
                    self.check_state()
    
    def cell_clicked(self, evt):
        card = self.deck.draw_card()
        self.cell.add_card(card)

    def check_state(self):
        def score_col(self,col_num): 
            hand=Hand() 
            j=col_num
            for i in range(5):
                occupied=self.cells[i][j].occupied
                card=self.cells[i][j].card
        return hand.score()
        def score_row(self, row_num):
            hand=Hand()
            i=row_num
            for i in range(5):
                occupied=self.cells[i][j].occupied
                card=self.cells[i][j].card
        return hand.score()
    
if __name__=="__main__":
    app=wx.App()
    game=Game()
    game.Show()
    app.MainLoop()

