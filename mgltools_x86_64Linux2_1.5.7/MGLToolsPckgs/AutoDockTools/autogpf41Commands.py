#############################################################################
#
# Author: Ruth HUEY, Michel F. SANNER
#
# Copyright: M. Sanner TSRI 2008
#
#############################################################################

# $Header: /mnt/raid/services/cvs/python/packages/share1.5/AutoDockTools/autogpf41Commands.py,v 1.3 2010/06/28 22:08:55 rhuey Exp $
#
# $Id: autogpf41Commands.py,v 1.3 2010/06/28 22:08:55 rhuey Exp $
#
#
#
#
#

"""
This Module facilitates producing a grid parameter file for AutoGrid41. The steps in this process are:

    * 'Macromolecule': Selecting the macromolecule: 
        The user can select the macromolecule for autogpf in two ways: 
           - it can be chosen from molecules previously added to the moleculeViewer  
           - it can be read in from a file:

        o Choose Macromol...

        o Read Macromolecule 


    * 'Set Map Types': Setting the types of maps to generate: 

        o Set Map Types Directly

        o By Choosing Ligand

        o By Reading Formatted File

The user can change the types of maps to be calculated.
He decides which types of possible hydrogen bonding he wishes to model. 
For instance, IF hydrogens are present  AND nitrogens, oxygens and /or sulfurs, 
the user can decide to model N-H bonds, O-H bonds and/or S-H bonds.  
He sets which type of dielectric to use:
    -distance-dependent dielectric  
    -constant dielectric  
(Other ligand-related commands allow the user to set energy parameters for new 
atom types or to set up a specialized 'covalent' grid-map.)


    * 'Set Grid': The user positions the grid and sets its dimensions by:

        o Setting the center of the grid maps: 

            - by picking an atom or

            - by entering the full-name of an atom or 

            - by entering the desired coordinates in entries 'x center', 'y center', 
'z center' (NB: ALL entries must be 'activated' by a 'Return')

            - by choosing  the 'Center on Macromolecule' option which sets the 
center of the grid to the geometric center of the macromolecule (obtained by 
averaging all its coordinates)

            - by choosing  the 'Center on Ligand' option which sets the center of 
the grid to the geometric center of the ligand (obtained by averaging all its 
coordinates)

        o Setting the number of grid points in each direction (which has to be an 
even number) and the spacing between the points. This is done by using the 
corresponding scale widgets.

        o Adjusting the position of the grid using scales for x-offset, y-offset 
and z-offset.  These scales allow the user to move the grid box up to 10 angstroms 
in any direction along any of the three axes. 
(NOTE that the units of these scales are tenths of Angstroms and the new coordinates 
of the center are reflected in the x-center, y-center, z-center entries)

    * 'Set Other Options': The user adjusts these additional parameters: 
    
        o the smoothing factor can be changed from its default 0.5Angstrom value.  
This changes the radius of the area within which the minimum energy is stored.
        o  electrostatic potential map may or may not be generated by AutoGrid

        o floating point potential map may or may not be generated 

        o the user may decide whether or not to use the default distance dependent 
dielectric constant.  If not, he can enter his desired dielectric constant or use 
the default value, 40. It should be noted that this entered value is multiplied 
by 0.1146 by the program for input to AutoGrid.

    * 'Write GPF': The results of the previous steps are written to a file. 
The user selects a filename via a filebrowser.  By convention, the file should 
have a .gpf extension. If no macromolecule has been selected, it is not possible 
to write a grid parameter file and the user gets a warning message to that effect. 
Likewise, the types of the maps to be calculated must be set before the grid 
parameter file is written and a warning message to this effect appears if the 
types have not been set.

    * 'Edit GPF': Allows user to edit a grid parameter file.  If one has been
written, it is automatically loaded. Otherwise, the user can select any *.gpf
file to edit from a file browser.
    
"""
from ViewerFramework.VFCommand import CommandGUI

from AutoDockTools.autogpfCommands import GpfSetGpo,\
GpfMacroInit, GpfLoadDefaults, GpfEditor, GpfWriter,\
SelectCenter, SetUpCovalentMap4, SetBoxParameters, SetOtherOptions,\
Gpf4ParameterFileSelector, Gpf4ParameterFileEditor, GpfMergeNonPolarHs,\
Gpf4SetMapTypes, Gpf4SetAtomTypes, Gpf4MacroInit, Gpf4MacroReader,\
Gpf4MacroChooser, Gpf4InitLigand, Gpf4LigandChooser, Gpf4LigReader,\
Gpf4FlexResChooser, Gpf4FlexResReader, Gpf4Writer, menuText, gridOpts,\
messages, checkHasGpo, box, cenSph, cenCross


GpfLoadDefaults41GUI = CommandGUI()
GpfLoadDefaults41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], menuText['ReadGpfMB'])


GpfEditor41GUI= CommandGUI()
GpfEditor41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
        menuText['EditGpfMB'])


GpfWriter41GUI= CommandGUI()
GpfWriter41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['WriteGpfMB'], cascadeName=menuText['WriteMB'])


SetUpCovalentMap41GUI = CommandGUI()
SetUpCovalentMap41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['SetUpCovalentMap4'], cascadeName = menuText['SetMapTypesMB'])


SetBoxParameters41GUI= CommandGUI()
SetBoxParameters41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['SetGridMB'])


SetOtherOptions41GUI= CommandGUI()
SetOtherOptions41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['SetOtherOptionsMB_AG3'], cascadeName = menuText['SetOtherOptionsMB'])


Gpf4ParameterFileSelector41GUI=CommandGUI()
Gpf4ParameterFileSelector41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
menuText['SetParameterFilename'], cascadeName = menuText['SetOtherOptionsMB'])


Gpf4ParameterFileEditor41GUI=CommandGUI()
Gpf4ParameterFileEditor41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
menuText['EditParameterFile'], cascadeName = menuText['SetOtherOptionsMB'])



Gpf4SetMapTypes41GUI= CommandGUI()
Gpf4SetMapTypes41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
    menuText['SetMapDirectly4'], cascadeName = menuText['SetMapTypesMB'])



Gpf4SetAtomTypes41GUI= CommandGUI()
Gpf4SetAtomTypes41GUI.addMenuCommand('menuRoot', 'Edit','Assign AD4 type', cascadeName = 'Atoms')



Gpf4MacroReader41GUI = CommandGUI()
Gpf4MacroReader41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
    menuText['ReadMacro4'], cascadeName = menuText['MacromoleculeMB'])


Gpf4MacroChooser41GUI = CommandGUI()
Gpf4MacroChooser41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
menuText['ChooseMacro4'], cascadeName = menuText['MacromoleculeMB'])


Gpf4LigandChooser41GUI= CommandGUI()
Gpf4LigandChooser41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
    menuText['ByChoosingLigand4'], cascadeName = menuText['SetMapTypesMB'])


Gpf4LigReader41GUI= CommandGUI()
Gpf4LigReader41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['ByReadingFile4'], cascadeName = menuText['SetMapTypesMB'])



Gpf4FlexResChooser41GUI= CommandGUI()
Gpf4FlexResChooser41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'],\
    menuText['ByChoosingFlexRes4'], cascadeName = menuText['SetMapTypesMB'])


Gpf4FlexResReader41GUI= CommandGUI()
Gpf4FlexResReader41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['ByReadingFlexResFile4'], cascadeName = menuText['SetMapTypesMB'])


Gpf4Writer41GUI= CommandGUI()
Gpf4Writer41GUI.addMenuCommand('AutoTools41Bar', menuText['AutoGpfMB'], \
    menuText['WriteGpf4MB'], cascadeName=menuText['WriteMB'])

commandList = [
    {'name':'AD41gpf_readGPF','cmd':GpfLoadDefaults(),'gui':GpfLoadDefaults41GUI},
    #AutoGrid41
    {'name':'AD41gpf_readMacromolecule','cmd':Gpf4MacroReader(),'gui':Gpf4MacroReader41GUI},
    {'name':'AD41gpf_chooseMacromolecule','cmd':Gpf4MacroChooser(),'gui':Gpf4MacroChooser41GUI},
    {'name':'AD41gpf_setMapTypes','cmd':Gpf4SetMapTypes(),'gui':Gpf4SetMapTypes41GUI},
    {'name':'AD41gpf_chooseFormattedLigand','cmd':Gpf4LigandChooser(),'gui':Gpf4LigandChooser41GUI},
    {'name':'AD41gpf_readFormattedLigand','cmd':Gpf4LigReader(),'gui':Gpf4LigReader41GUI},
    {'name':'AD41gpf_chooseFormattedFlexRes','cmd':Gpf4FlexResChooser(),'gui':Gpf4FlexResChooser41GUI},
    {'name':'AD41gpf_readFormattedFlexRes','cmd':Gpf4FlexResReader(),'gui':Gpf4FlexResReader41GUI},
    {'name':'AD41gpf_setUpCovalentMap4','cmd':SetUpCovalentMap4(),'gui':SetUpCovalentMap41GUI},
    #set grid
    {'name':'AD41gpf_setGrid','cmd':SetBoxParameters(),'gui':SetBoxParameters41GUI},
    #AutoGrid41
    {'name':'AD41gpf_setParameterFilename','cmd':Gpf4ParameterFileSelector(),'gui':Gpf4ParameterFileSelector41GUI},
    {'name':'AD41gpf_editParameterFile','cmd':Gpf4ParameterFileEditor(),'gui':Gpf4ParameterFileEditor41GUI},
    {'name':'AD41gpf_writeGPF','cmd':Gpf4Writer(),'gui':Gpf4Writer41GUI},
    {'name':'AD41gpf_setAtomTypes','cmd':Gpf4SetAtomTypes(),'gui':Gpf4SetAtomTypes41GUI},
    {'name':'AD41gpf_editGPF','cmd':GpfEditor(),'gui':GpfEditor41GUI},
    ]


def initModule(vf):

    for dict in commandList:
        vf.addCommand(dict['cmd'],dict['name'],dict['gui'])
    if not hasattr(vf, 'ADgpf_initMacro'):
        vf.addCommand(GpfMacroInit(),'ADgpf_initMacro',None)
    if not hasattr(vf, 'ADgpf4_initMacro'):
        vf.addCommand(Gpf4MacroInit(),'ADgpf4_initMacro',None)
    if not hasattr(vf, 'ADgpf4_initLigand'):
        vf.addCommand(Gpf4InitLigand(),'ADgpf4_initLigand',None)
    if not hasattr(vf, 'ADgpf_setGpo'):
        vf.addCommand(GpfSetGpo(),'ADgpf_setGpo',None)
    if not hasattr(vf, 'ADgpf_selectCenter'):
        vf.addCommand(SelectCenter(),'ADgpf_selectCenter',None)
    if not hasattr(vf, 'ADgpf_mergeNonPolarHydrogens'):
        vf.addCommand(GpfMergeNonPolarHs(),'ADgpf_mergeNonPolarHydrogens',None)




    if hasattr(vf, 'GUI') and 'AutoTools41Bar' in vf.GUI.menuBars.keys():
        for item in vf.GUI.menuBars['AutoTools41Bar'].menubuttons.values():
            item.configure(background = 'tan')
            item.configure(underline = '-1')
        if not hasattr(vf.GUI, 'adtBar'):
            vf.GUI.adtBar = vf.GUI.menuBars['AutoTools41Bar']
            vf.GUI.adtFrame = vf.GUI.adtBar.menubuttons.values()[0].master

