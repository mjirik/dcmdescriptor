#! /usr/bin/ipython
# -*- coding: utf-8 -*-


#
#from sklearn import svm
#X = [[0, 0], [1, 1],[0,4],[0.1, 0.2]]
#Y = [0, 1, 2 , 0]
#clf = svm.SVC()
#clf.fit(X, Y)  
#print clf.predict([[2,3]])
#
#dec = clf.decision_function([[1]])
#dec.shape[1]
#

# import funkcí z jiného adresáře
import sys
sys.path.append("../src/")
import featurevector
import training


#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat


vyber = 0

def traindata(fileslist):
    import dicom

    for filepath in filelist:
        dcmdata=dicom.read_file(filepath)
        print 'Modality: ', dcmdata.Modality
        print 'PatientsName: ' , dcmdata.PatientsName
        print 'BodyPartExamined: ', dcmdata.BodyPartExamined
        print 'SliceThickness: ', dcmdata.SliceThickness
        print 'PixelSpacing: ', dcmdata.PixelSpacing
        # get data
        data = dcmdata.pixel_array
        #print data
        featurevector.fvector(data)

        import matplotlib.pyplot as plt

        plt.figure()

        plt.imshow(data, cmap=plt.cm.gray)
        plt.show()
        plt.close()
    

def oneimage(data=1):
    import Tkinter
    top = Tkinter.Tk()


    frame = Frame(top)
    frame.pack()

    bottomframe = Frame(top)
    bottomframe.pack( side = BOTTOM )

    redbutton = Button(frame, text="Red", fg="red")
    redbutton.pack( side = LEFT)

    greenbutton = Button(frame, text="Brown", fg="brown")
    greenbutton.pack( side = LEFT )

    bluebutton = Button(frame, text="Blue", fg="blue")
    bluebutton.pack( side = LEFT )

    blackbutton = Button(bottomframe, text="Black", fg="black")
    blackbutton.pack( side = BOTTOM)

    # Code to add widgets will go here...
    top.mainloop()


def dialog():
    win = Tkinter.Toplevel()                                     
    Tkinter.Label(win,  text='Message!').pack()   
    ch = 0
    Tkinter.Button(win, text='OK', command=win.destroy).pack()   
    if makemodal:
        win.focus_set()       
        win.grab_set()           
        win.wait_window()       
    print 'dialog exit'         
    return 6

def classifDialog():
    import sys
    import Tkinter
    makemodal = (len(sys.argv) > 1)

    rootwin = Tkinter.Tk()

    listbox = Tkinter.Listbox(rootwin)
    listbox.pack()

    win = Tkinter.Toplevel()                                     
    listbox.insert(Tkinter.END, u"položka seznamu")
    for item in [u"jedna", u"dva", u"tři", u"čtyři"]:
            listbox.insert(Tkinter.END, item)
    #if makemodal:
    #    win.focus_set()       
    #    win.grab_set()           
    #    win.wait_window()       
    Tkinter.Button(rootwin, text='popup', command=rootwin.destroy).pack() 
    rootwin.mainloop()
    items = map(int, listbox.curselection())



class Dialogmenu:
    import sys
    import Tkinter
    retval = 0
    rootwin = None
    win = None

    bodyparts = ['foot', 'calf', 'knee', 'thigh','hip','colon', \
            'kidneys', 'liver', 'heart', 'lungs', 'neck', \
            'face', 'brain',]
    def __init__(self ):
        self.rootwin = Tkinter.Tk()
        #self.win = Tkinter.Toplevel()                                     
        #def start():
        #menuindexes =range(len(menuitemlist)) 
        Tkinter.Button(self.rootwin, text=self.bodyparts[0], command=lambda:
                self.callback(self.bodyparts[0],0)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[1], command=lambda:
                self.callback(self.bodyparts[1],1)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[2], command=lambda:
                self.callback(self.bodyparts[2],2)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[3], command=lambda:
                self.callback(self.bodyparts[3],3)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[4], command=lambda:
                self.callback(self.bodyparts[4],4)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[5], command=lambda:
                self.callback(self.bodyparts[5],5)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[6], command=lambda:
                self.callback(self.bodyparts[6],6)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[7], command=lambda:
                self.callback(self.bodyparts[7],7)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[8], command=lambda:
                self.callback(self.bodyparts[8],8)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[9], command=lambda:
                self.callback(self.bodyparts[9],9)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[10], command=lambda:
                self.callback(self.bodyparts[10],10)).pack()
        Tkinter.Button(self.rootwin, text=self.bodyparts[11], command=lambda:
                self.callback(self.bodyparts[11],11)).pack()



        Tkinter.mainloop()

    def callback(self, name, idx):
        #print "clicked!", name, ' i ', idx
        # win = Tkinter.Toplevel()                                     
        self.rootwin.destroy()
        self.retval = name



def dlgselectclose(rootwin, select):
    #if makemodal:
    #    win.focus_set()       
    #    win.grab_set()           
    #    win.wait_window()       
    print rootwin
    print select
    print 'hh'
    #rootwin.destroy
    # return select
    global vyber 
    vyber = select
    rootwin.destroy()

def dialogmenu(menuitemlist):
    import sys
    import Tkinter

    rootwin = Tkinter.Tk()
    menuindexes =range(len(menuitemlist)) 

    #for menuitemindex in menuindexes:
    #    mnidx = menuitemindex
    #    print 'mnitemidx ', menuitemindex
    #    Tkinter.Button(rootwin, text=menuitemlist[menuitemindex], \
    #            command=lambda: dlgselectclose(rootwin,menuindexes[mnidx])).pack() 
    #
    #    Tkinter.Button(rootwin, text=menuitemlist[menuitemindex],command=lambda:
    #            dlgselectclose(rootwin,8)).pack()
    Tkinter.Button(rootwin, text=menuitemlist[menuitemindex], \
            command=lambda: dlgselectclose(rootwin,menuindexes[mnidx])).pack() 



    rootwin.mainloop()
    print 'a po ',vyber

#class values:
#    val = 0
#    bodyparts = ['foot', 'calf', 'knee', 'thigh','hip','colon', \
#            'kidneys', 'liver', 'heart', 'lungs', 'neck', \
#            'face', 'brain']



def anotation_to_file(anotation, filename = 'anotation.json'):
    import json
    with open(filename, mode='w') as f:
        json.dump(anotation,f)

#def buttons_in_matplotlib():
class ButtonsInMatplotlib:
    from matplotlib.widgets import Button
    import matplotlib.pyplot as plt
    bodyparts = ['foot', 'calf', 'knee', 'thigh','pelvis','colon', \
            'kidneys', 'liver', 'heart', 'lungs', 'neck', \
            'face', 'brain']
    retvalue=0
    backrequest = 0
    exitrequest = 0
    
    def __init__(self, data ):
        from matplotlib.widgets import Button
        import matplotlib.pyplot as plt
        plt.figure()


        plt.imshow(data, cmap=plt.cm.gray)
        plt.subplots_adjust(right=0.75)
        baxes = []
        buttons = []
        callbacks = []
        #l1 = lambda: self.callback(0)

        btback = Button(plt.axes ([0.01, 0.01, 0.1, 0.1]), 'back')
        btback.on_clicked(self.backcallback)
        btexit= Button(plt.axes ([0.01, 0.12, 0.1, 0.1]), 'exit')
        btexit.on_clicked(self.exitcallback)

        for i in range(0,len(self.bodyparts)):
            baxes.append(plt.axes([0.8, 0.06+0.06*i, 0.07, 0.05]))
            buttons.append(Button(baxes[i],self.bodyparts[i]))
            #callbacks.append(self.callback0)
            #buttons[i].on_clicked(callbacks[i])
        
        buttons[0].on_clicked(self.callback0)
        buttons[1].on_clicked(self.callback1)
        buttons[2].on_clicked(self.callback2)
        buttons[3].on_clicked(self.callback3)
        buttons[4].on_clicked(self.callback4)
        buttons[5].on_clicked(self.callback5)
        buttons[6].on_clicked(self.callback6)
        buttons[7].on_clicked(self.callback7)
        buttons[8].on_clicked(self.callback8)
        buttons[9].on_clicked(self.callback9)
        buttons[10].on_clicked(self.callback10)
        buttons[11].on_clicked(self.callback11)
        buttons[12].on_clicked(self.callback12)
        #btn0 = Button(baxes[0],self.bodyparts[0])
        #btn1 = Button(baxes[1],self.bodyparts[1])
        #btn2 = Button(baxes[2],self.bodyparts[2])
        #btn3 = Button(baxes[3],self.bodyparts[3])
        #btn4 = Button(baxes[4],self.bodyparts[4])
        #btn5 = Button(baxes[5],self.bodyparts[5])
        #btn6 = Button(baxes[6],self.bodyparts[6])
        #btn.on_clicked(self.callback0)
        #for i in range(0,len(self.bodyparts)):

        #bnext.on_clicked(lambda:self.callback(0))
        #Button(baxes[0],'hoj')
        #Button(baxes[1],self.bodyparts[1])

        plt.show()

    def stdcallback(self, ind):
        import matplotlib.pyplot as plt
        plt.close()
        self.retvalue = self.bodyparts[ind]

    def callback0(self, evnt ):
        #self.retvalue = self.bodyparts[0]
        self.stdcallback(0)
    def callback1(self, evnt ):
        self.stdcallback(1)
    def callback2(self, evnt ):
        self.stdcallback(2)
    def callback3(self, evnt ):
        self.stdcallback(3)
    def callback4(self, evnt ):
        self.stdcallback(4)
    def callback5(self, evnt ):
        self.stdcallback(5)
    def callback6(self, evnt ):
        self.stdcallback(6)
    def callback7(self, evnt ):
        self.stdcallback(7)
    def callback8(self, evnt ):
        self.stdcallback(8)
    def callback9(self, evnt ):
        self.stdcallback(9)
    def callback10(self, evnt ):
        self.stdcallback(10)
    def callback11(self, evnt ):
        self.stdcallback(11)
    def callback12(self, evnt ):
        self.stdcallback(12)





    def backcallback(self, evnt):
        #self.retvalue = self.bodyparts[ind]
        print 'clicked ', evnt
        self.backrequest = 1
        import matplotlib.pyplot as plt
        plt.close()
    def exitcallback(self, evnt):
        #self.retvalue = self.bodyparts[ind]
        self.exitrequest = 1
        import matplotlib.pyplot as plt
        plt.close()



def manual_anotation(filelist):
    ''' Manual slice classification from file list.

    filelist = ['/home/mjirik/data/img1.dcm', './img2.png']

    manual_anotation(filelist)
    '''
    import dicom
    from matplotlib.widgets import Button

    anotation = {}

    print 'pocet souboru: ', len(filelist)

    # test jen na prvnim obrazku
    #filelist = [filelist[0]]
    fileind = 0
    while fileind <= len(filelist):
        filepath = filelist[fileind]

    #for filepath in filelist:


        dcmdata=dicom.read_file(filepath)
        print 'Modality: ', dcmdata.Modality
        print 'PatientsName: ' , dcmdata.PatientsName
        print 'BodyPartExamined: ', dcmdata.BodyPartExamined
        print 'SliceThickness: ', dcmdata.SliceThickness
        print 'PixelSpacing: ', dcmdata.PixelSpacing
        # get data
        data = dcmdata.pixel_array
        #print data
        #featurevector.fvector(data)

        import matplotlib.pyplot as plt

        # Button(
        
        dm = ButtonsInMatplotlib(data)
        
        #plt.show()
        #axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        #bnext = Button(axnext, 'Next')
        #bnext.on_clicked(callback.next)
        #plt.close()
        print 'finished (',fileind, '/', len(filelist), ') ' , dm.retvalue

        # User selects classification
        #dm = Dialogmenu()
        #print dm.retval



        if dm.backrequest == 1:
            fileind = fileind -1
        elif dm.exitrequest == 1:
            fileind = len(filelist) + 1
        else:
            fileind = fileind + 1
            anotation[filepath] = {'filepath':filepath, 'slicedescription': dm.retvalue}


    anotation_to_file(anotation)




if __name__ == "__main__":
    import sys
    import Tkinter
    import training
    print 'ahoj'
    #dm = Dialogmenu()
    #print dm.retval

    #filelist = training.filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')
    filelist = training.filesindir('/home/mjirik/data/jatra_06mm_jenjatra','*.*')
    manual_anotation(filelist)
    #traindata(filelist)

    # classifDialog()
#    dialogmenu(['Ahoj', 'Nehoj', 'Neboj'])

#    makemodal = (len(sys.argv) > 1)
#
#    rootwin = Tkinter.Tk()
#    #Tkinter.Button(root, text='popup', command=dialog).pack() 
#    print makemodal
#    var = Tkinter.IntVar(rootwin, value=0)
#    Tkinter.Button(rootwin, text='popup22', command=lambda
#            :dlgselectclose(rootwin,6)).pack() 
#    Tkinter.Button(rootwin, text='popup', command=rootwin.destroy).pack() 
#    if makemodal:
#        rootwin.focus_set()       
#        rootwin.grab_set()           
#        rootwin.wait_window()       
#    print 'a pred ', vyber
#    #oneimage()
#
