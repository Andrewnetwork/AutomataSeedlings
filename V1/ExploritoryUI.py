from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import NumericProperty

import numpy as np
from GraphFN import *
from matrixDiff import *


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')

class TestApp(App):
    topBttns         = []
    bottomButtons    = []
    activePixels     = NumericProperty(0)
    currentActiveLBL = None
    clearBttn        = None
    cols             = 16

    def pressPixelButton(self,instance):
        if(instance.background_color == [1,1,1,1]  ):
            instance.background_color = [99,99,99,99]
            self.activePixels += 1
        else:
            instance.background_color = [1, 1, 1, 1]
            self.activePixels -= 1

        try:
            matrixD = self.computeMatrixDiff()
            self.currentActiveLBL.text = "[ "+str(matrixD[0])+" | "+str(matrixD[1])+" ]"
        except:
            self.currentActiveLBL.text = "NEED INPUT"

    def computeMatrixDiff(self):
        rows = len(self.topBttns) / self.cols
        imageMatrixTop = np.zeros(shape=(rows, self.cols), dtype=np.int8)
        imageMatrixBot = np.zeros(shape=(rows, self.cols), dtype=np.int8)
        rowVal = []

        count = 0
        for bttn in self.topBttns:
            rowVal.append(0 if bttn.background_color == [1, 1, 1, 1] else 1)

            if (count % self.cols == 0):
                imageMatrixTop[count / self.cols, :] = rowVal
                rowVal = []

            count += 1

        rowVal = []

        count = 0
        for bttn in self.bottomButtons:
            rowVal.append(0 if bttn.background_color == [1, 1, 1, 1] else 1)

            if (count % self.cols == 0):
                imageMatrixBot[count / self.cols, :] = rowVal
                rowVal = []

            count += 1

        return matrixDiff(imageMatrixTop, imageMatrixBot)

    def clearBttnFn(self, instance):
        for bttn in self.topBttns:
            bttn.background_color = [1, 1, 1, 1]

        for bttn in self.bottomButtons:
            bttn.background_color = [1, 1, 1, 1]

        self.activePixels = 0

        self.currentActiveLBL.text = "NEED INPUT"

    def build(self):
        #self.activePixels.bind(self.pixelValChange)

        boxLayout = BoxLayout(orientation='vertical')

        topLayer = BoxLayout( orientation="horizontal", size_hint=(1, .1), padding=4)

        self.currentActiveLBL = Label(text="== HELLO, I AM A GENERAL PATTERN RECOGNIZER ==",size_hint=(1, 1))
        self.clearBttn = Button(text="Clear", size_hint=(0.5, 1), on_press=self.clearBttnFn)

        topLayer.add_widget(self.currentActiveLBL)
        topLayer.add_widget(self.clearBttn )

        boxLayout.add_widget(topLayer)

        gridLayoutTop = GridLayout(cols=self.cols, padding=10,  size_hint=(1, 2) )
        gridLayoutBottom = GridLayout(cols=self.cols, padding=10, size_hint=(1, 2))

        for i in range(80*2):
            ntb = Button()
            nbb = Button()

            self.topBttns.append(ntb)
            self.bottomButtons.append(nbb)

            ntb.bind(on_press=self.pressPixelButton)
            nbb.bind(on_press=self.pressPixelButton)

            gridLayoutTop.add_widget(ntb)
            gridLayoutBottom.add_widget(nbb)

        boxLayout.add_widget(gridLayoutTop)
        boxLayout.add_widget(gridLayoutBottom)

        return boxLayout

TestApp().run()