# Application of geopandas
 
This script uses the Geopandas library to perform various geographic data processing tasks such as reading shapefiles, plotting geometries, performing geometric operations such as intersection, union, and difference, reprojecting geometries, creating buffers, finding centroids, joining attributes, and plotting data on a map.

# Requirements

The following libraries are used in the script and need to be installed in order to run it:

geopandas
matplotlib
pandas
shapely
To install the libraries, use the following command in your terminal:

pip install geopandas matplotlib pandas shapely

# Running the script
The script can be run from a Python environment such as IDLE or in a code editor such as Visual Studio Code. Make sure to have the required libraries installed and the necessary shapefiles and data in the same directory as the script before running it.

# Steps in the script

The script performs the following steps:

## list
- Reads in two shapefiles, Study_Area_1.shp and Study_Area_2.shp using the `read_file` method from geopandas.
- Plots both shapefiles.
- Reads in a third shapefile, `river.shp`.
- Performs an intersection of Study_Area_1 and Study_Area_2, and plots the result.
- Performs a union of Study_Area_1 and Study_Area_2, and plots the result.
- Performs a symmetric difference of Study_Area_1 and Study_Area_2, and plots the result.
- Performs a difference of Study_Area_1 and Study_Area_2, and plots the result.
- Dissolves the union of Study_Area_1 and Study_Area_2 into one geometry and plots the result.
- Reprojects the river shapefile into a projected coordinate reference system (CRS) and plots the result.
- Creates a 500 meter buffer around the river and plots the result.
- Finds the centroid of the union of Study_Area_1 and Study_Area_2 and plots it on the same graph.
- Reads in a csv file, `us_airports.csv`, containing information about airports in the United States.
- Reads in a shapefile, `us_states.shp`, containing information about the states in the United States.
- Joins the airport data and the state data and plots the result on a map with the states in blue and the airport locations as green markers.


# Conclusion
The script demonstrates how to perform various geographic data processing tasks using the Geopandas library. The resulting plots provide a visual representation of the geographic data and the results of the performed operations.
