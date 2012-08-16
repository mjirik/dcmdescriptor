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
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(anotation,f)


def manual_anotation(filelist):
    ''' Manual slice classification from file list.

    filelist = ['/home/mjirik/data/img1.dcm', './img2.png']

    manual_anotation(filelist)
    '''
    import dicom
    from matplotlib.widgets import Button

    anotation = []

    print 'pocet souboru: ', len(filelist)

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
        #featurevector.fvector(data)

        import matplotlib.pyplot as plt

        plt.figure()


        plt.imshow(data, cmap=plt.cm.gray)
        # Button(
        
        plt.show()
        plt.close()
        print 'close()'

        # User selects classification
        dm = Dialogmenu()
        print dm.retval

        anotation.append({'filepath':filepath, 'slicedescription': dm.retval})

    anotation_to_file(anotation)




if __name__ == "__main__":
    import sys
    import Tkinter
    import training
    print 'ahoj'
    #dm = Dialogmenu()
    #print dm.retval


    filelist = training.filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')
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
