#!/bin/ksh ~/.mgltools/pythonsh
########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Monday 14 February 2011 12:31:28 
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
# $Header: /mnt/raid/services/cvs/CADD/workflows/virtualScreening/AutoDockML_0.1_net.py,v 1.1 2011/04/15 16:19:38 nadya Exp $
#
# $Id: AutoDockML_0.1_net.py,v 1.1 2011/04/15 16:19:38 nadya Exp $
#


if __name__=='__main__':
    from sys import argv
    if '--help' in argv or '-h' in argv or '-w' in argv: # run without Vision
        withoutVision = True
        from Vision.VPE import NoGuiExec
        ed = NoGuiExec()
        from NetworkEditor.net import Network
        import os
        masterNet = Network("process-"+str(os.getpid()))
        ed.addNetwork(masterNet)
    else: # run as a stand alone application while vision is hidden
        withoutVision = False
        from Vision import launchVisionToRunNetworkAsApplication, mainLoopVisionToRunNetworkAsApplication
	if '-noSplash' in argv:
	    splash = False
	else:
	    splash = True
        masterNet = launchVisionToRunNetworkAsApplication(splash=splash)
        import os
        masterNet.filename = os.path.abspath(__file__)
from traceback import print_exc
## loading libraries ##
from AutoDockTools.VisionInterface.Adt import Adt
from WebServices.VisionInterface.WSNodes import wslib
from Vision.StandardNodes import stdlib
try:
    masterNet
except (NameError, AttributeError): # we run the network outside Vision
    from NetworkEditor.net import Network
    masterNet = Network()

masterNet.getEditor().addLibraryInstance(Adt,"AutoDockTools.VisionInterface.Adt", "Adt")

masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")

masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
try:
    addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
except:
    pass
try:
    ## saving node AutodockVS ##
    from Adt.Macro.AutodockVS import AutodockVS
    AutodockVS_0 = AutodockVS(constrkw={}, name='AutodockVS', library=Adt)
    masterNet.addNode(AutodockVS_0,357,292)
    apply(AutodockVS_0.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
    autodock_kryptonite_nbcr_net_4 = AutodockVS_0.macroNetwork.nodes[3]
    autodock_kryptonite_nbcr_net_4.inputPortByName['ga_run'].widget.set(r"", run=False)
    apply(autodock_kryptonite_nbcr_net_4.inputPortByName['lib'].widget.configure, (), {'choices': ('sample', 'NCIDS_SC', 'NCI_DS1', 'NCI_DS2', 'human_metabolome', 'chembridge_building_blocks', 'drugbank_nutraceutics', 'drugbank_smallmol', 'fda_approved')})
    autodock_kryptonite_nbcr_net_4.inputPortByName['lib'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['filter_file_url'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['ga_num_evals'].widget.set(r"", run=False)
    apply(autodock_kryptonite_nbcr_net_4.inputPortByName['sched'].widget.configure, (), {'choices': ('SGE', 'CSF')})
    autodock_kryptonite_nbcr_net_4.inputPortByName['sched'].widget.set(r"SGE", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['ga_num_generations'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['userlib'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['ga_pop_size'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['localRun'].widget.set(0, run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['email'].widget.set(r"", run=False)
    autodock_kryptonite_nbcr_net_4.inputPortByName['execPath'].widget.set(r"", run=False)

    ## saving connections for network AutodockVS ##
    AutodockVS_0.macroNetwork.freeze()
    AutodockVS_0.macroNetwork.unfreeze()

    ## modifying MacroInputNode dynamic ports
    input_Ports_1 = AutodockVS_0.macroNetwork.ipNode
    input_Ports_1.outputPorts[1].configure(name='PrepareADVSInputs_ligands')
    input_Ports_1.outputPorts[2].configure(name='PrepareADVSInputs_autogrid_results')
    input_Ports_1.outputPorts[3].configure(name='PrepareADVSInputs_dpf_template_obj')

    ## modifying MacroOutputNode dynamic ports
    output_Ports_2 = AutodockVS_0.macroNetwork.opNode
    output_Ports_2.inputPorts[1].configure(singleConnection='auto')
    output_Ports_2.inputPorts[1].configure(name='GetMainURLFromList_newurl')
    AutodockVS_0.inputPorts[0].configure(name='PrepareADVSInputs_ligands')
    AutodockVS_0.inputPorts[0].configure(datatype='LigandDB')
    AutodockVS_0.inputPorts[1].configure(name='PrepareADVSInputs_autogrid_results')
    AutodockVS_0.inputPorts[1].configure(datatype='autogrid_results')
    AutodockVS_0.inputPorts[2].configure(name='PrepareADVSInputs_dpf_template_obj')
    AutodockVS_0.inputPorts[2].configure(datatype='dpf_template')
    ## configure MacroNode input ports
    AutodockVS_0.outputPorts[0].configure(name='GetMainURLFromList_newurl')
    AutodockVS_0.outputPorts[0].configure(datatype='string')
    ## configure MacroNode output ports
    AutodockVS_0.shrink()
    apply(AutodockVS_0.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
except:
    print "WARNING: failed to restore AutodockVS named AutodockVS in network masterNet"
    print_exc()
    AutodockVS_0=None

try:
    ## saving node DownloadSaveDir ##
    from WebServices.VisionInterface.WSNodes import DownloadSaveDirNode
    DownloadSaveDir_6 = DownloadSaveDirNode(constrkw={}, name='DownloadSaveDir', library=wslib)
    masterNet.addNode(DownloadSaveDir_6,357,391)
    apply(DownloadSaveDir_6.inputPortByName['url'].configure, (), {'defaultValue': None})
    DownloadSaveDir_6.inputPortByName['url'].rebindWidget()
    DownloadSaveDir_6.inputPortByName['url'].widget.set(r"", run=False)
    DownloadSaveDir_6.inputPortByName['url'].unbindWidget()
    apply(DownloadSaveDir_6.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DownloadSaveDirNode named DownloadSaveDir in network masterNet"
    print_exc()
    DownloadSaveDir_6=None

try:
    ## saving node Output_Directory ##
    from Vision.StandardNodes import DirBrowserNE
    Output_Directory_7 = DirBrowserNE(constrkw={}, name='Output_Directory', library=stdlib)
    masterNet.addNode(Output_Directory_7,547,265)
    Output_Directory_7.inputPortByName['directory'].widget.set(r"AutoDockML_0.1_output", run=False)
    apply(Output_Directory_7.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DirBrowserNE named Output_Directory in network masterNet"
    print_exc()
    Output_Directory_7=None

try:
    ## saving node AutogridResURL ##
    from Adt.Input.AutogridResURL import AutogridResURL
    AutogridResURL_8 = AutogridResURL(constrkw={}, name='AutogridResURL', library=Adt)
    masterNet.addNode(AutogridResURL_8,374,145)
    AutogridResURL_8.inputPortByName['url'].widget.set(r"http://kryptonite.nbcr.net/appautogrid1296246047469-570974390/", run=False)
    apply(AutogridResURL_8.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore AutogridResURL named AutogridResURL in network masterNet"
    print_exc()
    AutogridResURL_8=None

try:
    ## saving node PublicServerLigandDB ##
    from Adt.Input.PublicServerLigandDB import PublicServerLigandDB
    PublicServerLigandDB_9 = PublicServerLigandDB(constrkw={}, name='PublicServerLigandDB', library=Adt)
    masterNet.addNode(PublicServerLigandDB_9,13,145)
    PublicServerLigandDB_9.inputPortByName['server_lib'].widget.set(r"sample", run=False)
except:
    print "WARNING: failed to restore PublicServerLigandDB named PublicServerLigandDB in network masterNet"
    print_exc()
    PublicServerLigandDB_9=None

try:
    ## saving node DPFTemplateBrowser ##
    from Adt.Input.DPFTemplateBrowser import DPFTemplateBrowser
    DPFTemplateBrowser_10 = DPFTemplateBrowser(constrkw={}, name='DPFTemplateBrowser', library=Adt)
    masterNet.addNode(DPFTemplateBrowser_10,915,143)
    DPFTemplateBrowser_10.inputPortByName['dpf_template_file'].widget.set(r"AutoDockML_0.1_input/2HTY_A.dpf", run=False)
    apply(DPFTemplateBrowser_10.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DPFTemplateBrowser named DPFTemplateBrowser in network masterNet"
    print_exc()
    DPFTemplateBrowser_10=None

#masterNet.run()
masterNet.freeze()

## saving connections for network AutoDockML-0.1 ##
if Output_Directory_7 is not None and DownloadSaveDir_6 is not None:
    try:
        masterNet.connectNodes(
            Output_Directory_7, DownloadSaveDir_6, "directory", "path", blocking=True
            , splitratio=[0.65546942220461224, 0.32042606395899709])
    except:
        print "WARNING: failed to restore connection between Output_Directory_7 and DownloadSaveDir_6 in network masterNet"
if AutodockVS_0 is not None and DownloadSaveDir_6 is not None:
    try:
        masterNet.connectNodes(
            AutodockVS_0, DownloadSaveDir_6, "GetMainURLFromList_newurl", "url", blocking=True
            , splitratio=[0.2182585732109612, 0.71171057897582179])
    except:
        print "WARNING: failed to restore connection between AutodockVS_0 and DownloadSaveDir_6 in network masterNet"
if PublicServerLigandDB_9 is not None and AutodockVS_0 is not None:
    try:
        masterNet.connectNodes(
            PublicServerLigandDB_9, AutodockVS_0, "ligDB", "PrepareADVSInputs_ligands", blocking=True
            , splitratio=[0.21870434345807416, 0.66803683999749475])
    except:
        print "WARNING: failed to restore connection between PublicServerLigandDB_9 and AutodockVS_0 in network masterNet"
if AutogridResURL_8 is not None and AutodockVS_0 is not None:
    try:
        masterNet.connectNodes(
            AutogridResURL_8, AutodockVS_0, "autogrid_res_obj", "PrepareADVSInputs_autogrid_results", blocking=True
            , splitratio=[0.44788171325418591, 0.35372301560992558])
    except:
        print "WARNING: failed to restore connection between AutogridResURL_8 and AutodockVS_0 in network masterNet"
if DPFTemplateBrowser_10 is not None and AutodockVS_0 is not None:
    try:
        masterNet.connectNodes(
            DPFTemplateBrowser_10, AutodockVS_0, "dpf_template", "PrepareADVSInputs_dpf_template_obj", blocking=True
            , splitratio=[0.33272690695264329, 0.20368928127553113])
    except:
        print "WARNING: failed to restore connection between DPFTemplateBrowser_10 and AutodockVS_0 in network masterNet"
masterNet.runOnNewData.value = False

if __name__=='__main__':
    from sys import argv
    lNodePortValues = []
    if (len(argv) > 1) and argv[1].startswith('-'):
        lArgIndex = 2
    else:
        lArgIndex = 1
    while lArgIndex < len(argv) and argv[lArgIndex][-3:]!='.py':
        lNodePortValues.append(argv[lArgIndex])
        lArgIndex += 1
    masterNet.setNodePortValues(lNodePortValues)
    if '--help' in argv or '-h' in argv: # show help
        masterNet.helpForNetworkAsApplication()
    elif '-w' in argv: # run without Vision and exit
         # create communicator
        from NetworkEditor.net import Communicator
        masterNet.communicator = Communicator(masterNet)
        print 'Communicator listening on port:', masterNet.communicator.port

        import socket
        f = open(argv[0]+'.sock', 'w')
        f.write("%s %i"%(socket.gethostbyname(socket.gethostname()),
                         masterNet.communicator.port))
        f.close()

        masterNet.run()

    else: # stand alone application while vision is hidden
        if '-e' in argv: # run and exit
            masterNet.run()
        elif '-r' in argv or len(masterNet.userPanels) == 0: # no user panel => run
            masterNet.run()
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)
        else: # user panel
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)

