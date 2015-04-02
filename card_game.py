#Ilya Paley
#paley1

import wx
import random

class Hex(object):
    def __init__(self,x,y,state):
        self.x=x
        self.y=y
        self.state=state
        state()=[0,1]
        for i in range(6):
            angle=(2*math.pi/6)*(i+.5)
            x_i=self.x+self.size*math.cos(angle)
            y_i=self.y+self.size*math.sin(angle)
            point=wx.Point(x_i,y_i)
            self.points.append(point)
        neighbors=[[[1,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]],[[1,0],[1,-1],[0,-1],[-1,0],[0,1],[1,1]]]
    def set_neighbors(self,neighbors):
	self.neighbors=neighbors
    def toggle(self):
        if state()==0:
            return state()==1
        else:
            return state()==0
    def distance(self,x,y):
        return x.point,y.point
    def draw(self,dc):
        dc.SetPen(wx.Pen(wx.BLACK,1))
        dc.SetBrush(wx.Brush(self.colors[self.state]))
        dc.DrawPolygon(self.points)
    def prepare(self,rules):
        configuration=0
        for i,neighbor in enumerate(self.neighbors):
            if neighbor:
                configuration|=neighbor.state<<i
        self.next=rules.get_value(configuration)
    def update(self):
        change_state()

class Grid(object):
    def __init__(self,100,100):
        wx.Panel(800,800)
        self.paint.bind(wx.EVT_PAINT)
        self.timer=wx.Timer(self) 
        self.Bind(wx.EVT_TIMER,self.update,self.timer). 
        self.timer.Start(300)
        self.Bind(wx.EVT_LEFT_DOWN,self.on_click)
    def paint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        for i in range(len(self.hexes)):
            for j in range(len(self.hexes[i])):
                hex=self.hexes[i][j]
                hex.draw(dc)
    def make_hexes(self):
        hex.draw(dc)+=self.hexes
    def randomize_grid(self):
        for a in self.hexes:
            random.state()
    def find_neighbors(self):
        for i in range(len(self.hexes)):
            for j in range(len(self.hexes[i])):
                hex=self.hexes[i][j]
                neighbors=[[[1,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]],[[1,0],[1,-1],[0,-1],[-1,0],[0,1],[1,1]]]
    def on_click(wx.evt):
        x=evt.GetX()
        y=evt.GetY()
        for i in range(len(self.hexes)):
            for j in range(len(self.hexes[i])):
                hex=self.hexes[i][j]
        toggle(hex)
class Rules(object):
    num_rules=2**6
    def __init__(self,num):
        self.states=[]
        for i in range(self.num_rules):
            value=num&1
            self.states.append(value)
            num>>=1
    def get_value(self,state):
        return self.states[state]

class UI(wx.Frame):
    

app=wx.App()
frame=wx.Frame(None)
grid=Grid(frame)
app.MainLoop()

