"""
WorksetGetNames
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how get workset of element.
Use this sample along with the Video on Youtube.
"""
import clr
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit Services 
clr.AddReference('RevitServices')
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

import RevitServices
from RevitServices.Persistence import DocumentManager
# get the current document in Revit.
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo input
elements = UnwrapElement(IN[0])
# empty lists. 
WorksetIDList = list()
WorksetNameList = list()
# loop over elements 
for e in elements:
    # get all workset ids 
    WorksetIDList.append(doc.GetWorksetTable().GetWorkset(e.WorksetId))
# loop over workset ids of elements. 
for ws in WorksetIDList:
    # get the readable name to output. 
    WorksetNameList.append(ws.Name)

OUT = WorksetNameList