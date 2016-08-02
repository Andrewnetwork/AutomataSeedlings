from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView

import numpy as np
from GraphMaker import *
import pandas as pd


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')

class TestApp(App):
    topBttns         = []
    bottomButtons    = []
    savedImages      = []
    savedImagesBttns = []
    activePixels     = NumericProperty(0)
    currentActiveLBL = None
    clearBttn        = None
    saveBttn         = None
    saveLayout       = None
    topImageBuffer   = None
    cols             = 35


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

            # Compute matrix diff for saved images.
            for idx,img in enumerate(self.savedImages):
                matrixD = self.matrixDiff( self.topImageBuffer,img )
                self.savedImagesBttns[idx].text =  "[ "+str(matrixD[0])+" | "+str(matrixD[1])+" ]"
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

        self.topImageBuffer = imageMatrixTop

        ## EDIT HERE
        return self.matrixDiff(imageMatrixTop, imageMatrixBot)

    def clearBttnFn(self, instance):
        for bttn in self.topBttns:
            bttn.background_color = [1, 1, 1, 1]

        for bttn in self.bottomButtons:
            bttn.background_color = [1, 1, 1, 1]

        self.activePixels = 0

        self.currentActiveLBL.text = "NEED INPUT"

    def matrixDiff(self, mt, mb):
        pmT =  ETPM( mt  )
        pmB =  ETPM( mb )

        vsd = vectorSimDiff(sorted(pmT[1].flatten()), sorted(pmB[1].flatten()))

        diff = pmT[1] - pmB[1]

        df1 = pd.DataFrame(pmT[1], index=pmT[0],columns=pmT[0])
        df2 = pd.DataFrame(pmB[1], index=pmB[0],columns=pmB[0])

        diffPd = pd.DataFrame(diff, index=pmB[0],columns=pmB[0])

        print("=====================================")
        print(df1)
        print(df2)
        print(diffPd)

        print(vsd)



        return vsd


    def saveImage(self, instance):
        nb = Button(width=100)
        self.savedImagesBttns.append(nb)
        self.saveLayout.add_widget(nb)

        rows = len(self.topBttns) / self.cols
        imageMatrixBot = np.zeros(shape=(rows, self.cols), dtype=np.int8)

        rowVal = []

        count = 0
        for bttn in self.bottomButtons:
            rowVal.append(0 if bttn.background_color == [1, 1, 1, 1] else 1)

            if (count % self.cols == 0):
                imageMatrixBot[count / self.cols, :] = rowVal
                rowVal = []

            count += 1

        self.savedImages.append(imageMatrixBot)



    def build(self):
        #self.activePixels.bind(self.pixelValChange)

        boxLayout = BoxLayout(orientation='vertical')

        topLayer = BoxLayout( orientation="horizontal", size_hint=(1, .4), padding=4)

        self.currentActiveLBL = Label(text="== HELLO, I AM A GENERAL PATTERN RECOGNIZER ==",size_hint=(1, 1))
        self.clearBttn = Button(text="Clear", size_hint=(0.5, 1), on_press=self.clearBttnFn)
        self.saveBttn = Button(text="Save", size_hint=(0.2, 1), on_press=self.saveImage)

        topLayer.add_widget(self.currentActiveLBL)
        topLayer.add_widget(self.clearBttn )
        topLayer.add_widget(self.saveBttn)

        boxLayout.add_widget(topLayer)

        gridLayoutTop = GridLayout(cols=self.cols, padding=10,  size_hint=(1, 2) )
        gridLayoutBottom = GridLayout(cols=self.cols, padding=10, size_hint=(1, 2))

        for i in range(350):
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

        self.saveLayout = BoxLayout(orientation="horizontal", spacing=10, padding=5)

        boxLayout.add_widget(self.saveLayout)

        return boxLayout

TestApp().run()