# Tracks

Tracks -

`track_length` from [deisnau](https://github.com/deisnau)

## Installation

```bash
git clone git@github.com:
cd ./tracks
python -m venv ./env
. ./env/Scripts/activate
pip install -r ./requirements.txt
```

## Usage

```bash
python tracks.py ./path/my_tracks.gpx
```

Script *track_length* uses the library `geopandas` for reading *.gpx file and calculating track's lengths.
