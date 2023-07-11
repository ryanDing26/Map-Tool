########################################################################
#
#    Vision Node - Python source code - file generated by vision
#    Tuesday 27 November 2007 06:26:02 
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
# $Header: /mnt/raid/services/cvs/VisionLibraries/scipylib/signal/lowPass_Remez.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#
# $Id: lowPass_Remez.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#

# import node's base class node
from NetworkEditor.items import NetworkNode
class lowPass_Remez(NetworkNode):
    mRequiredTypes = {}
    mRequiredSynonyms = [
    ]
    def __init__(self, constrkw = {},  name='lowPass Remez', **kw):
        kw['constrkw'] = constrkw
        kw['name'] = name
        apply( NetworkNode.__init__, (self,), kw)
        code = """def doit(self, ntaps, fs, passband):
    from scipy.signal import remez
    b=remez(ntaps,[0, passband, passband*1.10, fs/2.0],[1, 0],[.9,.1],Hz=fs)
## to ouput data on port filter_coefficients use
    self.outputData(filter_coefficients=b)
"""
        self.configure(function=code)
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'ntaps', 'cast': True, 'datatype': 'None', 'balloon': 'number of FIR taps', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'fs', 'cast': True, 'datatype': 'None', 'balloon': 'sampling frequency', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'passband', 'cast': True, 'datatype': 'None', 'balloon': 'pass band in units of fs', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.outputPortsDescr.append(
            {'name': 'filter_coefficients', 'datatype': 'None', 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.widgetDescr['ntaps'] = {
            'initialValue': 10, 'widgetGridCfgnode': {'rowspan': 1, 'labelSide': 'left', 'column': 1, 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 0}, 'increment':1, 'height': 20, 'labelGridCfg': {'rowspan': 1, 'column': 0, 'sticky': 'w', 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 0}, 'width': 60, 'master': 'node', 'wheelPad': 1, 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'ntaps'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}
        self.widgetDescr['passband'] = {
            'initialValue': 1.0, 'widgetGridCfgnode': {'rowspan': 1, 'labelSide': 'left', 'column': 1, 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 1}, 'increment':1.0, 'height': 20, 'labelGridCfg': {'rowspan': 1, 'column': 0, 'sticky': 'w', 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 1}, 'width': 60, 'master': 'node', 'wheelPad': 1, 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'passband'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}


    def beforeAddingToNetwork(self, net):
        try:
            ed = net.getEditor()
        except:
            import traceback; traceback.print_exc()
            print 'Warning! Could not import widgets'

