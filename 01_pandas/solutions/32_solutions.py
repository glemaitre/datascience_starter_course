gdf_regions = gpd.read_file(os.path.join('data', 'regions.geojson'))
gdf_regions = gdf_regions.merge(regions_vote, how='inner', left_on='code', right_on='code_y')

gdf_normalized = gdf_regions.copy()
gdf_normalized['Choice A'] /= gdf_regions[['Choice A', 'Choice B']].sum(axis=1)
gdf_normalized['Choice B'] /= gdf_regions[['Choice A', 'Choice B']].sum(axis=1)
