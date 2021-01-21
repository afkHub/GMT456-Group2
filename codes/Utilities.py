"""
The file which helps to obtain the path of example shapefile.
"""

def test_data_folder():
    this_filename = inspect.stack()[0][1]
    basepath, _ = os.path.split(this_filename)
    return os.path.join(basepath, 'data')
