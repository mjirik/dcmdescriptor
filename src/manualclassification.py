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
    rootwin.destroy

def dialogmenu(menuitemlist):
    import sys
    import Tkinter

    rootwin = Tkinter.Tk()

    for menuitemindex in range(len(menuitemlist)):
        mnidx = menuitemindex
        Tkinter.Button(rootwin, text=menuitemlist[menuitemindex],command=lambda:dlgselectclose(rootwin,menuitemlist[mnidx])).pack()
        print 'mnitemidx ', menuitemindex

    rootwin.mainloop()
    print 'a po ',vyber



if __name__ == "__main__":
    import sys
    import Tkinter
    import training
    print 'ahoj'
    # classifDialog()
    dialogmenu(['Ahoj', 'Nehoj', 'Neboj'])

    makemodal = (len(sys.argv) > 1)

    rootwin = Tkinter.Tk()
    #Tkinter.Button(root, text='popup', command=dialog).pack() 
    print makemodal
    var = Tkinter.IntVar(rootwin, value=0)
    Tkinter.Button(rootwin, text='popup22', command=lambda
            :dlgselectclose(rootwin,6)).pack() 
    Tkinter.Button(rootwin, text='popup', command=rootwin.destroy).pack() 
    if makemodal:
        rootwin.focus_set()       
        rootwin.grab_set()           
        rootwin.wait_window()       
    print 'a pred ', vyber
    #oneimage()
    #filelist = training.filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')
    #traindata(filelist)

