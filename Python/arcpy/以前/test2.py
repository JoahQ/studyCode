# Author:   Jennifer (esri_id: jenn775)
# Created:  July 20, 2010
# Edits:    Mathew Coyle, May 24, 2012

from Tkinter import *
import arcpy

# SelectPopup.py sample Python script using Tkinter for a user interface
# User selects feature from list, code selects and zooms to feature

# Use in ArcMap by attaching script to a button for best results
# In ArcGIS 10, you can add scripts and models to buttons in the UI without using VBA.
# Create a Python script tool using this script and then
# see "Adding a custom tool to a menu or toolbar" in this help topic:
# http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#//002400000005000000.htm

Layer = arcpy.GetParameterAsText(0) # Layer
SelField =  arcpy.GetParameterAsText(1) # Field to Select
Title =  arcpy.GetParameterAsText(2) # Title (optional)

# Troubleshooting messages
#arcpy.AddMessage("Layer is "+repr(Layer))
#arcpy.AddMessage("Selection field is "+repr(SelField))
#arcpy.AddMessage("Title is " + repr(Title))

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets(master)

    def createWidgets(self, master):
        self.yScroll  =  Scrollbar ( self, orient=VERTICAL )
        self.yScroll.grid ( row=0, column=1, sticky=N+S )
        self.stList = Listbox (self, yscrollcommand=self.yScroll.set)
        self.stList.grid( row=0, column=0 )
        self.yScroll["command"] = self.stList.yview
        # populate list with choices, sorted ascending
        mxd = arcpy.mapping.MapDocument("CURRENT")
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == Layer:
                break
        # for large datasets where the selection field contains many blanks or
        # non-unique values, you can create a summary table and set SelTable
        # equal to it for faster creation of the selection dialog
        SelTable = lyr.dataSource
        rows = arcpy.SearchCursor(SelTable, "", "", SelField, SelField + " A")
        oldVal = ""
        for row in rows:
            newVal = row.getValue(SelField)
            #only add value to Listbox if it is not a duplicate
            if newVal <> oldVal:
                self.stList.insert( END, row.getValue(SelField) )
            oldVal = newVal
        #add selection and quit button
        self.selButton = Button (self, text='Select', command=self.selectFeat)
        self.selButton.grid( row=0, column=2 )
        self.quitButton = Button ( self, text='Quit', command=master.destroy )
        self.quitButton.grid( row=1, column=2 )

    def selectFeat(self):
        sel = self.stList.curselection()
        myFeature = self.stList.get(sel[0])

        def BuildQuery(table, field, operator, value=None):
            """Generate a valid ArcGIS query expression

            arguments

              table - input feature class or table view
              field - field name (string)
              operator - SQL operators ("=","<>", etc)
                 "IS NULL" and "IS NOT NULL" are supported
              value - query value (optional)

            """
            # Adds field delimiters
            qfield=arcpy.AddFieldDelimiters(table,field)

            # tweak value delimeter for different data types
            if type(value) == str:
                # add single quotes around string values
                qvalue = "'" + value + "'"
            elif value == None:
                # drop value when not specified (used for IS NULL, etc)
                qvalue = ""
            else:
                # numeric values are fine unmodified
                qvalue = value

            sql = "{0} {1} {2}".format(qfield,operator,qvalue)
            #print repr(sql)
            return sql.strip()

        where = BuildQuery(Layer, SelField, "=", myFeature)
        arcpy.AddMessage(where)
        arcpy.SelectLayerByAttribute_management(Layer, "NEW_SELECTION", where)
        mxd = arcpy.mapping.MapDocument("CURRENT")
        for df in arcpy.mapping.ListDataFrames(mxd):
            if df.name == mxd.activeView:
                df.zoomToSelectedFeatures()
                arcpy.RefreshActiveView()


root = Tk()
app = Application(master=root)
app.master.title(Title)
app.mainloop()