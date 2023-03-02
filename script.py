# %%
import geopandas as gpd
import matplotlib.pyplot as plt

# %%
SA1 = gpd.read_file('Study_Area_1.shp')
SA1.plot()

# %%
SA2 = gpd.read_file('Study_Area_2.shp')
SA2.plot() 

# %%
river = gpd.read_file('river.shp')
river.plot()

# %% [markdown]
# Plot multiple graphs

# %%
fig, ax = plt.subplots()
SA1.plot(ax = ax, color = 'blue', edgecolor = 'black')
SA2.plot(ax = ax, color = 'none', edgecolor = 'black')
river.plot(ax = ax)

# %% [markdown]
# Intersection

# %%
intersection = gpd.overlay(SA1, SA2, how = 'intersection')
intersection.plot()

# %% [markdown]
# Union

# %%
union = gpd.overlay(SA1, SA2, how = 'union')
union.plot()

# %% [markdown]
# Symmetric difference (Union - 2*Intersection)

# %%
sd = gpd.overlay(SA1, SA2, how = 'symmetric_difference')
sd.plot()

# %% [markdown]
# Difference of polygons (SA1 - SA2) 

# %%
difference = gpd.overlay(SA1, SA2, how = 'difference')
difference.plot()
plt.show()

# %% [markdown]
# Dissolve (SA1 + SA2)

# %%
union = gpd.overlay(SA1, SA2, how = 'union')
union['common'] = 1

dissolved_sa = union.dissolve(by = 'common')
dissolved_sa.plot()

# %% [markdown]
# Reprojecting river Geopandas GeoDataFrame into a projected CRS

# %%
river_projected = river.to_crs(epsg=24547)
print(river, river_projected, type(river_projected))

# %% [markdown]
# Buffer

# %%
buffer_500 = river_projected['geometry'].buffer(distance = 500)
buffer_500.plot(figsize = (7,7))

# %% [markdown]
# 

# %% [markdown]
# Obtaining centroid

# %%
union = gpd.overlay(SA1, SA2, how = 'union')
union.plot(edgecolor = 'black')

centroid = union['geometry'].centroid
centroid.plot()

# %% [markdown]
# Plot both graph in one figure

# %%
fig1, ax1 = plt.subplots()
union.plot(ax = ax1, color = 'blue', edgecolor = 'black')
centroid.plot(ax = ax1, color = 'black')
river.plot(ax = ax)

# %% [markdown]
# Airport Data

# %%
import pandas as pd
from shapely.geometry import Point

# %% [markdown]
# Import the states ESRI shp of the USA

# %%
us_states = gpd.read_file('us_states.shp')
us_states.plot()

# %%
airport_data = pd.read_csv('us_airports.csv')

airport_data.columns

# %%
geometry = [Point(xy) for xy in zip(airport_data['LONGITUDE'], airport_data['LATITUDE'])]

# %% [markdown]
# Plotting CSV file

# %%
airport_us = gpd.GeoDataFrame(airport_data, geometry= geometry, crs = us_states.crs )
airport_us.plot()

# %% [markdown]
# Rename column name

# %%
airport_us.rename(columns= {'STATE':'state_code'}, inplace=True)
airport_us

# %%
us_states = pd.read_csv('state names and codes.csv')
us_states

# %% [markdown]
# Join Attributes

# %%
airport_us = airport_us.merge(us_states, on = 'state_code')


# %%
airport_us = airport_us[['AIRPORT', 'geometry']]
airport_us

# %%
fig , ax = plt.subplots(figsize = (8,8))
us_states.plot(ax = ax, color ='blue', edgecolor= 'black')
airport_us.plot(ax = ax, markersize = 2, color= 'green')

# %% [markdown]
# Spatial Join

# %%
airport_us = gpd.sjoin(airport_us, us_states, how = 'inner', op= 'intersects')

# %%
airport_us

# %%



