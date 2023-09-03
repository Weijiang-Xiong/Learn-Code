import numpy as np
import pandas as pd
import geopandas
import contextily as ctx
import matplotlib.pyplot as plt

place_name = "Chavannes-pres-Renens"
loc = ctx.Place(place_name, zoom_adjust=0)  # zoom_adjust modifies the auto-zoom
# # Define the bounding box coordinates
west, south, east, north = loc.w, loc.s, loc.e, loc.n


# https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html
df = pd.DataFrame(
    {
        "Points": ["Boundary1", "Boundary2"],
        "Longitude": [west, east],
        "Latitude": [south, north],
    }
)
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
).to_crs(epsg=3857) # transform all points from longitude-latitude coordinates to Web Mercator

# https://geopandas.org/en/stable/gallery/plotting_basemap_background.html
fig, ax = plt.subplots(figsize=(5,5))
gdf.plot("Points", ax=ax, markersize=0) # just to set the boundary

ctx.add_basemap(ax)

# now create a new df with the sensors and plot their locations
# remember to use .to_csr with geopandas
# https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html
df = pd.DataFrame(
    {
        "Points": ["data1", "data2"],
        "Longitude": [west + 0.5*abs(east - west), west + 0.75*abs(east - west)],
        "Latitude": [south+ 0.5*abs(north - south), south+ 0.75*abs(north - south)],
    }
)
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
).to_crs(epsg=3857) # transform all points from longitude-latitude coordinates to Web Mercator

# coordinates in Spherical Mercator projection
points = np.array([(p.x, p.y) for p in gdf.geometry])
xs, ys = points[:, 0], points[:, 1]

ax.plot(xs, ys)

# turn off the axis, only keep the map and the markers
ax.axis("off")
plt.show()
fig.savefig("plot_map.png")