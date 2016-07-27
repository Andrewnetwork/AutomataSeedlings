from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import NumericProperty

import numpy as np


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')

class TestApp(App):
    bttns            = []
    activePixels     = NumericProperty(0)
    currentActiveLBL = None
    maximumPixelsTXT = None
    clearBttn        = None
    saveBttn         = None
    nameTXT          = None
    cols             = 20

    def pressPixelButton(self,instance):
        if(instance.background_color == [1,1,1,1]  ):
            if(self.maximumPixelsTXT.text.isdigit() and self.activePixels < int(self.maximumPixelsTXT.text) ):
                instance.background_color = [99,99,99,99]
                self.activePixels += 1
        else:
            instance.background_color = [1, 1, 1, 1]
            self.activePixels -= 1


    def on_activePixels(self,instance, value):
        self.currentActiveLBL.text = str(value)

    def clearBttnFn(self, instance):
        for bttn in self.bttns:
            bttn.background_color = [1, 1, 1, 1]
            self.activePixels = 0

    def saveImage(self, instance):
        rows = len(self.bttns) / self.cols
        imageMatrix = np.zeros(shape=(rows,self.cols))
        rowVal = []

        count = 0
        for bttn in self.bttns:
            rowVal.append( 0 if bttn.background_color == [1,1,1,1] else 1 )

            if(count % self.cols == 0):
                imageMatrix[count/self.cols,:] = rowVal
                rowVal = []

            count += 1

        imageMatrix.tofile("tmpOutput/"+self.nameTXT.text+".numpy")

    def build(self):
        #self.activePixels.bind(self.pixelValChange)

        boxLayout = BoxLayout(orientation='vertical')

        topLayer = BoxLayout( orientation="horizontal", size_hint=(1, .1), padding=4)

        self.maximumPixelsTXT = TextInput(hint_text="Maximum Pixels",text="5", size_hint=(0.2, 1))
        self.nameTXT = TextInput(hint_text="Image Name" , size_hint=(0.2, 1))

        self.currentActiveLBL = Label(text="0",size_hint=(0.2, 1))
        self.saveBttn = Button(text="Save",size_hint=(0.2, 1), on_press=self.saveImage)
        self.clearBttn = Button(text="Clear",size_hint=(0.2, 1),on_press=self.clearBttnFn)

        topLayer.add_widget(self.maximumPixelsTXT)
        topLayer.add_widget(self.nameTXT)
        topLayer.add_widget(self.currentActiveLBL)
        topLayer.add_widget(self.saveBttn )
        topLayer.add_widget(self.clearBttn)


        boxLayout.add_widget(topLayer)

        gridLayout = GridLayout(cols=self.cols, padding=10,  size_hint=(1, 2) )

        for i in range(80*4):
            nb = Button()
            self.bttns.append(nb)
            nb.bind(on_press=self.pressPixelButton)
            gridLayout.add_widget(nb)

        boxLayout.add_widget(gridLayout)

        return boxLayout

TestApp().run()