from dv import AedatFile
import numpy as np

with AedatFile('dvSave-2023_05_11_11_10_55.aedat4') as f:
    # list all the names of streams in the file
    print(f.names)

    # events will be a named numpy array
    events = np.hstack([packet for packet in f['events'].numpy()])
    # Slice events
    first_x_events = events#[:1000000]
    # Access information of all events by type
    timestamps, x, y, polarities = first_x_events['timestamp'], first_x_events['x'], first_x_events['y'], first_x_events['polarity']
    # Access individual events information
    #event_123_x = events[123]['x']

data = np.column_stack([timestamps, x, y, polarities])
datafile_path = "MyFile.txt"
np.savetxt(datafile_path , data, fmt=['%d','%d', '%d','%d'])


