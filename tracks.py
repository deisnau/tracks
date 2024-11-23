from tracks.track_lenght import load_gpx_as_geodataframe


if __name__ == "__main__":

    gpx_file_path = "./track_example.gpx"

    gdf_lines = load_gpx_as_geodataframe(gpx_file_path)

    print("\nTracks:")
    print(gdf_lines)
