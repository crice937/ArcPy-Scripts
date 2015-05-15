featureinput = r'c:\projects\waterway.gdb\stream' ##Location of the feature you wish to split.
featureoutput = r'c:\projects\waterway.gdb\stream10' ##Location of where you’d like the split feature to be.
outputcount = 10 ##Number of segments you'd like the feature to be split into.

line = arcpy.da.SearchCursor(in_fc, ("SHAPE@",)).next()[0] ##Gets the geometry of the first record.
arcpy.CopyFeatures_management([line.segmentAlongLine(i/float(out_count), ((i+1)/float(out_count)), True) for i in range(0, out_count)], out_fc)
##Creates a list of 10 equal segments and creates a new feature class.
