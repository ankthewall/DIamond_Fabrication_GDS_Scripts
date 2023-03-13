import gdspy as gdspy

# Setting up configuration for new GDS Write

lib=gdspy.GdsLibrary()
cell=lib.new_cell('FIRST')

# Writing the write area
write_area=gdspy.Rectangle((-1500,-1500),(1500,1500),layer=1)
cell.add(write_area)

# Writing the 1500 um test structure
test_structure_1=gdspy.Rectangle((-1500,-1500),(0,0),layer=2)
cell.add(test_structure_1)

text_1=gdspy.Text("1500 um",10,(-750,100),layer=2)
cell.add(text_1)

# Writing the 500 um test structure
test_structure_2=gdspy.Rectangle((500,500),(1000,1000),layer=2)
cell.add(test_structure_2)

text_2=gdspy.Text("500 um",10,(750,1100),layer=2)
cell.add(text_2)

# Writing the 200 um test structure
test_structure_3=gdspy.Rectangle((-1450,1400),(-1250,1200),layer=2)
cell.add(test_structure_3)

text_3=gdspy.Text("500 um",10,(-1350,1475),layer=2)
cell.add(text_3)

# Writing the 100 um test structure
test_structure_4=gdspy.Rectangle((-1200,1400),(-1100,1300),layer=2)
cell.add(test_structure_4)

text_4=gdspy.Text("500 um",10,(-1150,1475),layer=2)
cell.add(text_4)

# Writing the 50 um test structure
test_structure_5=gdspy.Rectangle((-1050,1400),(-1000,1350),layer=2)
cell.add(test_structure_5)

text_5=gdspy.Text("500 um",10,(-1025,1475),layer=2)
cell.add(text_5)

# Writing the 30 um test structure
test_structure_6=gdspy.Rectangle((-950,1400),(-920,1370),layer=2)
cell.add(test_structure_6)

text_6=gdspy.Text("500 um",10,(-935,1475),layer=2)
cell.add(text_6)


# Finally quick spot check
lib.write_gds('2023_03_13_Ni_Wet_Etch_Test_Mask.gds')
gdspy.LayoutViewer(lib)