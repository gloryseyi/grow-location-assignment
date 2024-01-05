import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#read the GrowLocation.csv into a dataframe
dataframe = pd.read_csv('GrowLocations.csv')
#read map7.png
uk_map = mpimg.imread('map7.png')
#rename the longitude column as latitude and the latitude column as longitude
dataframe = dataframe.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})
#drop empty rows in the dataframe
cleaned_dataframe = dataframe.dropna()

min_latitude = 50.681 
max_latitude = 57.985 
min_longitude = -10.592 
max_longitude = 1.6848 
#set latitude and longitude filter for the dataframe
mask_latitude = (cleaned_dataframe['Latitude'] >= min_latitude) & (cleaned_dataframe['Latitude'] <= max_latitude)
mask_longitude = (cleaned_dataframe['Longitude'] >= min_longitude) & (cleaned_dataframe['Longitude'] <= max_longitude)
#apply the filters to the dataframe
filtered_data = cleaned_dataframe[mask_latitude & mask_longitude]
#plot longitude on x_axis and latitude on y_axis
plt.scatter(x=filtered_data['Longitude'], y=filtered_data['Latitude'])
#label the x and y axis and give the map a title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Plotting the Grow Dataset')
#set the boundary for the map
plt.imshow(uk_map, extent=[min_longitude, max_longitude, min_latitude, max_latitude])
plt.show()