import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.ExcelFile( "Obes-phys-acti-diet-eng-2014-tab.xls")

# Reading in second section by age
data_age = data.parse( u'7.2', skiprows=4, skipfooter=14)
# Read the sheet by skipping the top 4 rows and bottom 14 rows

#Renaming unnamed column to "year"
data_age.rename( columns = {u'Unnamed: 0': u'Year'}, inplace=True)
#inplace = True, modifies the existing object without creating a new object

#Drop na
data_age.dropna( inplace=True)

#Changing the indexing based on year, makes plotting easier
data_age.set_index( 'Year', inplace=True);
#Setting index to year

#Plotting
data_age.plot()

#Removing total: better analyze age groups
data_age_minus_total = data_age.drop('Total', axis = 1)
#axis=1, drop columns
#data_age_minus_total.plot()
plt.show()

plt.close()
#Plot children vs adultsp
data_age['Under 16'].plot(label="Under 16")
data_age['35-44'].plot(label="25-44")
plt.legend(loc="upper left")
plt.show()

#Curvefitting + Polynomial
kids_values = data_age['Under 16'].values
x_axis = range(len(kids_values))
# extract values for children under 16

#Increased degrees of polynomials can increase precision but can create incoherent results
poly_degree = 3
curve_fit = np.polyfit( x_axis, kids_values, poly_degree)
poly_interp = np.poly1d( curve_fit)
#Fit a graph through the data
#poly1d(), equation generated to create a function used to generate values

poly_fit_values = []
for i in range( len( x_axis)):
	poly_fit_values.append( poly_interp(i))
#Loop from 0 to 10, curve fitting algorithm for each x_axis value

plt.plot( x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot( x_axis, kids_values, "-b", label = "Orig")
plt.legend( loc="upper left")
plt.show()
#re-reun poly_interp(), 0-15
x_axis2 = range(15)

poly_fit_values = []
for i in range( len( x_axis2)):
	poly_fit_values.append(poly_interp(i))
#depending on your polynomial degree, here 3 or 4
#you can reach completely different conclusions

#Increased degrees of polynomials can increase precision but can create incoherent results
poly_degree = 4
curve_fit = np.polyfit( x_axis, kids_values, poly_degree)
poly_interp = np.poly1d( curve_fit)
#Fit a graph through the data
#poly1d(), equation generated to create a function used to generate values

poly_fit_values = []
for i in range( len( x_axis)):
	poly_fit_values.append( poly_interp(i))
#Loop from 0 to 10, curve fitting algorithm for each x_axis value

plt.plot( x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot( x_axis, kids_values, "-b", label = "Orig")
plt.legend( loc="upper left")
plt.show()
#re-reun poly_interp(), 0-15
x_axis2 = range(15)

poly_fit_values = []
for i in range( len( x_axis2)):
	poly_fit_values.append(poly_interp(i))

#Increased degrees of polynomials can increase precision but can create incoherent results
poly_degree = 5
curve_fit = np.polyfit( x_axis, kids_values, poly_degree)
poly_interp = np.poly1d( curve_fit)
#Fit a graph through the data
#poly1d(), equation generated to create a function used to generate values

poly_fit_values = []
for i in range( len( x_axis)):
	poly_fit_values.append( poly_interp(i))
#Loop from 0 to 10, curve fitting algorithm for each x_axis value

plt.plot( x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot( x_axis, kids_values, "-b", label = "Orig")
plt.legend( loc="upper left")

#re-reun poly_interp(), 0-15
x_axis2 = range(15)

poly_fit_values = []
for i in range( len( x_axis2)):
	poly_fit_values.append(poly_interp(i))