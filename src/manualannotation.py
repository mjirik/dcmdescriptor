#! /usr/bin/ipython
# -*- coding: utf-8 -*-


import pdb
#  pdb.set_trace();

# import funkcí z jiného adresáře
import sys
#sys.path.append("../src/")
import featurevector

import logging
logger = logging.getLogger(__name__)

#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat


vyber = 0

    

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




#class values:
#    val = 0
#    bodyparts = ['foot', 'calf', 'knee', 'thigh','hip','colon', \
#            'kidneys', 'liver', 'heart', 'lungs', 'neck', \
#            'face', 'brain']






#def buttons_in_matplotlib():
class ButtonsInMatplotlib:
    from matplotlib.widgets import Button
    import matplotlib.pyplot as plt
    bodyparts = ['foot', 'calf', 'knee', 'thigh','pelvis','colon', \
            'kidneys', 'liver', 'heart', 'lungs', 'neck', \
            'face', 'brain','error']
    bodypartsind=0
    retvalue=0
    backrequest = 0
    exitrequest = 0
    
    def __init__(self, data ):
        from matplotlib.widgets import Button
        import matplotlib.pyplot as plt
        plt.figure()


        plt.imshow(data, cmap=plt.cm.gray)
        plt.subplots_adjust(right=0.85,left=0.18)
        baxes = []
        buttons = []
        callbacks = []
        #l1 = lambda: self.callback(0)

        btback = Button(plt.axes ([0.02, 0.05, 0.1, 0.1]), 'back')
        btback.on_clicked(self.backcallback)
        btexit= Button(plt.axes ([0.02, 0.17, 0.1, 0.1]), 'exit')
        btexit.on_clicked(self.exitcallback)

        for i in range(0,len(self.bodyparts)):
            baxes.append(plt.axes([0.85, 0.05+0.06*i, 0.12, 0.05]))
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
        buttons[13].on_clicked(self.callback13)
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
        self.bodypartsind = ind

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
    def callback13(self, evnt ):
        self.stdcallback(13)





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

def manual_annotation_from_dir(datadir, databasedir='', wildcard = '*.dcm',\
        annotationfile = 'annotation.yaml', newannotationfile = False, 
        step=1):
    """ User interactive data annotation 

    annotationfile: name of filelist
    newannotationfile: True/False Creates new file, oteherwise is new 
        annotation added to end of existing filelist
    step: if data are sorted there is no need for annotate every slice
    """

    import system
    filelist = system.dcmsortedlist(datadir, wildcard, databasedir)
    manual_annotation(filelist,databasedir = databasedir, 
            annotationfile=annotationfile,
            newannotationfile=newannotationfile, 
            step=step
            )



def manual_annotation(filelist, databasedir = None, annotationfile =
'annotation.yaml', newannotationfile = False, step = 1):
    ''' Manual slice classification from file list.

    >>> filelist = ['/home/mjirik/data/img1.dcm', './img2.png']

    manual_anotation(filelist)
    
    '''
    import dicom
    from matplotlib.widgets import Button
    import os
    import operator
    import matplotlib.pyplot as plt
    import system


    # vytvoreni noveho souboru
    if newannotationfile | operator.not_(os.path.exists(annotationfile)):
        annotation = {}
        annotation ['data'] = {}
    else:
        annotation = system.annotation_from_file(annotationfile)
        print 'přidávám anotaci do souboru'


    #print 'pocet souboru: ', len(filelist)

    # test jen na prvnim obrazku
    #filelist = [filelist[0]]
    # For step annotation
    #prev_retvalue = 'none'
    #prev_bodypartsind = 0
    dm = None

    fileind = 0
    while fileind < len(filelist):
        filepath = filelist[fileind]
        relfilepath = os.path.relpath(filepath, databasedir)



        dcmdata=dicom.read_file(filepath)
        #logger.info('Modality: ' + dcmdata.Modality)
        #logger.info('PatientsName: ' + dcmdata.PatientsName)
        #logger.info('BodyPartExamined: '+ dcmdata.BodyPartExamined)
        #logger.info('SliceThickness: '+ str(dcmdata.SliceThickness))
        #logger.info('PixelSpacing: '+ str(dcmdata.PixelSpacing))
        # get data
        data = dcmdata.pixel_array

        if fileind % step == 0:
            dm = ButtonsInMatplotlib(data)
            logger.info( 'finished ('+str(fileind)+ '/'+ str(len(filelist))\
                    + ') ' + str(dm.retvalue))



        if dm.backrequest == 1:
            fileind = fileind -step
            dm.backcallback = 0
        elif dm.exitrequest == 1:
            fileind = len(filelist) + step
        else:
            fileind = fileind + step
            annotation['data'][relfilepath] = {'filepath':relfilepath,
                    'slicedescription': dm.retvalue,
                    'sliceclass':dm.bodypartsind}


    #pdb.set_trace();
    #annotation={}
    #annotation['data'] = annotation_data
    annotation['info'] = {'classes': dm.bodyparts}
    system.annotation_to_file(annotation, annotationfile)




if __name__ == "__main__":
    import sys
    import Tkinter
    import system

    logging.basicConfig(format='%(asctime)s %(message)s')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    logger.debug('input params')
    for arg in sys.argv:
        logger.debug(''+arg)

    databasedir = '/home/mjirik/data'
    if len(sys.argv) < 2:
        datatraindir = 'medical/data_orig/jatra-kma/jatra_06mm_jenjatra'
        #datatraindir = 'medical/data_orig/jatra-kma/jatra_5mm'
        #datatraindir = 'medical/dara'
    else:
        datatraindir = sys.argv[1]

    logger.debug('Adresar ' + datatraindir)
    #dm = Dialogmenu()
    #print dm.retval

    #filelist = training.filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')
    #filelist = system.filesindir(datatraindir, '*.dcm',databasedir)
    filelist = system.dcmsortedlist(datatraindir, '*.dcm',databasedir)
    manual_annotation(filelist,databasedir = databasedir, annotationfile =
            '../data/annotation.yaml')
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

