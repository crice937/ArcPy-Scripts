import os
import arcpy

in_feature  = arcpy.GetParameterAsText(0)
out_features  = arcpy.GetParameterAsText(1)
origin_year = int(arcpy.GetParameterAsText(2))
field_name = arcpy.GetParameterAsText(3)
start = int(arcpy.GetParameterAsText(4))
stop = int(arcpy.GetParameterAsText(5))
step = int(arcpy.GetParameterAsText(6))

path = arcpy.Describe(in_feature).path
new_field_name = arcpy.AddFieldDelimiters(path, field_name)

for x in range(start, stop, step):
    year_range = origin_year + x
    where_query = """{0} <= {1}""".format(new_field_name, year_range)

    year_out_name = os.path.join(out_features, "Years_{0}".format(x))
    mean_out_name = os.path.join(out_features, "Mean_{0}".format(x))

    arcpy.Select_analysis(in_feature, year_out_name, where_query)

    arcpy.MeanCenter_stats(year_out_name, mean_out_name, "#", "#", "#")