#Adding a vetor layer
layer=iface.addVectorLayer("D:/GIS_Related_File/Nepal_admin_boundary/hermes_NPL_new_wgs_1.shp","Nepal","ogr")

#Checking Layers coordinate system
crs= layer.crs()

#Checking Layers Extent
extent= layer.extent()
min_x= extent.xMinimum()
min_y = extent.yMinimum()
max_x = extent.xMaximum()
max_y= extent.yMaximum()
print(min_x,min_y,max_x,max_y)

