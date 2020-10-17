from panda3d.core import loadPrcFileData
loadPrcFileData('', 'sync-video t')
loadPrcFileData('', 'show-frame-rate-meter f')
loadPrcFileData('', 'win-size 800 600')
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
import sys
class Game(DirectObject):
    def __init__(self):
        base = ShowBase()
        self.forward_speed = 5.0 # units per second
        self.backward_speed = 2.0
        self.forward_button = KeyboardButton.ascii_key('w')
        self.backward_button = KeyboardButton.ascii_key('s')
        self.in_button = KeyboardButton.ascii_key('d')
        self.out_button = KeyboardButton.ascii_key('a')
        self.space_button = KeyboardButton.space()
        self.pagenumber = 1
       # base.setBackgroundColor(1,1,1)
        base.accept('escape',sys.exit)
        base.useTrackball()
        base.trackball.node().setPos(-7.55,0,6)
        self.image = self.loadImageAsPlane('Psalms/ReadingThePsalmsWithLuther' + str(self.pagenumber) + '.jpg')
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(1.4)
        onebutton = DirectButton(text = ('Next'), scale=.06, command=self.nextpage)
        onebutton.setPos(-1.2,0,0.7)
        twobutton = DirectButton(text = ('Previous'), scale=.06, command=self.previouspage)
        twobutton.setPos(-1.2,0,0.9)
        threebutton = DirectButton(text = ('Jump10'), scale=.06, command=self.jump10)
        threebutton.setPos(-1.2,0,0.5)
        fourbutton = DirectButton(text = ('Jump50'), scale=.06, command=self.jump50)
        fourbutton.setPos(-1.2,0,0.3)
        fivebutton = DirectButton(text = ('Jump100'), scale=.06, command=self.jump100)
        fivebutton.setPos(-1.2,0,0.1)
        sixbutton = DirectButton(text = ('Jump200'), scale=.06, command=self.jump200)
        sixbutton.setPos(-1.2,0,-0.1)
        #sevenbutton = DirectButton(text = ('Jump500'), scale=.06, command=self.jump500)
       # sevenbutton.setPos(-1.2,0,-0.3)
        self.accept('arrow_up', self.previouspage)
        self.accept('arrow_down', self.nextpage)
        self.accept('1', self.jump10)
        self.accept('2', self.jump25)
        self.accept('3', self.jump50)
        self.accept('4', self.jump100)
        self.accept('5', self.jump200)
        self.accept('6', self.jump500)
        taskMgr.add(self.exampleTask, 'MyTaskName')
    def loadimage(self):
        self.image.removeNode();
        self.image = self.loadImageAsPlane('Psalms/ReadingThePsalmsWithLuther' + str(self.pagenumber) + '.jpg')
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(1.4)
    def previouspage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber-1
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def nextpage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+1
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def jump10(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+10
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def jump25(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+25
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def jump50(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+50
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def jump100(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+100
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def jump200(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+200
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()

    def jump500(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+500
        try :
            self.loadimage()
        except IOError:
            self.pagenumber = 1
            self.loadimage()
    def exampleTask(self,task):
        base.trackball.node().setPos(-7.55, base.trackball.node().getY(), base.trackball.node().getZ())
        base.trackball.node().setHpr(0, 0, 0)
        if (base.trackball.node().getY() < -12):
            base.trackball.node().setY(-12)
        if (base.trackball.node().getY() > 1):
            base.trackball.node().setY(1)
        if (base.trackball.node().getZ() < 4):
            base.trackball.node().setZ(4)
        if (base.trackball.node().getZ() > 8):
            base.trackball.node().setZ(8)
        speed = 0.0
        #self.image.setScale(0.2) 
        is_down = base.mouseWatcherNode.is_button_down
        if is_down(self.forward_button):
            speed += self.forward_speed
            y_delta = -5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.backward_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.in_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_y(base.trackball.node().getY() - y_delta)
        if is_down(self.out_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_y(base.trackball.node().getY() + y_delta)
        if is_down(self.space_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        return task.cont
    def loadImageAsPlane(self, filepath, yresolution = 600):
        	tex = loader.loadTexture(filepath)
        	tex.setBorderColor(Vec4(0,0,0,0))
        	tex.setWrapU(Texture.WMBorderColor)
        	tex.setWrapV(Texture.WMBorderColor)
        	cm = CardMaker(filepath + ' card')
        	cm.setFrame(-tex.getOrigFileXSize(), tex.getOrigFileXSize(), -tex.getOrigFileYSize(), tex.getOrigFileYSize())
        	card = NodePath(cm.generate())
        	card.setTexture(tex)
        	card.setScale(card.getScale()/ yresolution)
        	card.flattenLight()
        	return card     
fgame = Game()
base.run()
