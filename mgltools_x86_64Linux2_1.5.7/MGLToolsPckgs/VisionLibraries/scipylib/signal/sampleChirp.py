########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Tuesday 27 November 2007 11:19:09 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /mnt/raid/services/cvs/VisionLibraries/scipylib/signal/sampleChirp.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#
# $Id: sampleChirp.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#

from NetworkEditor.macros import MacroNode
class sampleChirp(MacroNode):

    def __init__(self, constrkw={}, name='sampleChirp', **kw):
        kw['name'] = name
        apply( MacroNode.__init__, (self,), kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        ## loading libraries ##
        from MyDefaultLib import mydefaultlib
        net.editor.addLibraryInstance(mydefaultlib,"MyDefaultLib", "mydefaultlib")


    def afterAddingToNetwork(self):
        masterNet = self.macroNetwork
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        ## loading libraries ##
        from MyDefaultLib import mydefaultlib
        ## building macro network ##
        sampleChirp_1 = self
        from traceback import print_exc
        ## loading libraries ##
        from MyDefaultLib import mydefaultlib
        self.macroNetwork.getEditor().addLibraryInstance(mydefaultlib,"MyDefaultLib", "mydefaultlib")

        try:
            ## saving node input Ports ##
            input_Ports_2 = self.macroNetwork.ipNode
        except:
            print "WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork"
            print_exc()
            input_Ports_2=None

        try:
            ## saving node output Ports ##
            output_Ports_3 = self.macroNetwork.opNode
        except:
            print "WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork"
            print_exc()
            output_Ports_3=None

        try:
            ## saving node linearChirp ##
            from MyDefaultLib.signal.linearChirp import linearChirp
            linearChirp_4 = linearChirp(constrkw = {}, name='linearChirp', library=mydefaultlib)
            self.macroNetwork.addNode(linearChirp_4,206,166)
            apply(linearChirp_4.inputPortByName['time'].configure, (), {'color': 'green'})
            apply(linearChirp_4.outputPortByName['y'].configure, (), {'color': 'green'})
            linearChirp_4.inputPortByName['chirpSlope'].unbindWidget()
            apply(linearChirp_4.configure, (), {'expanded': True})
        except:
            print "WARNING: failed to restore linearChirp named linearChirp in network self.macroNetwork"
            print_exc()
            linearChirp_4=None

        try:
            ## saving node timeRange ##
            from MyDefaultLib.signal.timeRange import timeRange
            timeRange_5 = timeRange(constrkw = {}, name='timeRange', library=mydefaultlib)
            self.macroNetwork.addNode(timeRange_5,195,95)
            apply(timeRange_5.outputPortByName['out0'].configure, (), {'color': 'green'})
            apply(timeRange_5.outputPortByName['fs'].configure, (), {'color': 'green'})
            timeRange_5.inputPortByName['fs'].unbindWidget()
        except:
            print "WARNING: failed to restore timeRange named timeRange in network self.macroNetwork"
            print_exc()
            timeRange_5=None

        self.macroNetwork.run()
        self.macroNetwork.freeze()

        ## saving connections for network sampleChirp ##
        if timeRange_5 is not None and linearChirp_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    timeRange_5, linearChirp_4, "out0", "time", blocking=True)
            except:
                print "WARNING: failed to restore connection between timeRange_5 and linearChirp_4 in network self.macroNetwork"
        output_Ports_3 = self.macroNetwork.opNode
        if linearChirp_4 is not None and output_Ports_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    linearChirp_4, output_Ports_3, "y", "new", blocking=True)
            except:
                print "WARNING: failed to restore connection between linearChirp_4 and output_Ports_3 in network self.macroNetwork"
        input_Ports_2 = self.macroNetwork.ipNode
        if input_Ports_2 is not None and timeRange_5 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_2, timeRange_5, "new", "fs", blocking=True)
            except:
                print "WARNING: failed to restore connection between input_Ports_2 and timeRange_5 in network self.macroNetwork"
        if input_Ports_2 is not None and linearChirp_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_2, linearChirp_4, "new", "chirpSlope", blocking=True)
            except:
                print "WARNING: failed to restore connection between input_Ports_2 and linearChirp_4 in network self.macroNetwork"
        self.macroNetwork.unfreeze()

#self.macroNetwork.run()

        #apply(sampleChirp_1.inputPortByName['linearChirp_chirpSlope'].createWidget, (), {'descr':{'initialValue': 0.0, 'labelGridCfg': {'column': 0, 'row': 0}, 'master': 'ParamPanel', 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'chirpSlope'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}})

        sampleChirp_1.shrink()

        ## reset modifications ##
        sampleChirp_1.resetTags()
        sampleChirp_1.buildOriginalList()
