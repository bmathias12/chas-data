import os
import zipfile

RAW_DATA_ZIPFILE_LOC = './2014thru2018-140-csv.zip'
RAW_EXTRACT_LOC = './data/raw/'

def main():

    # create data directory and raw directory to unzip raw datafile
    if not os.path.exists(RAW_EXTRACT_LOC):
        extract_raw_data(RAW_DATA_ZIPFILE_LOC, RAW_EXTRACT_LOC)
    else:
        print(f'{RAW_EXTRACT_LOC} already exists. Skipping extract.')

        

def extract_raw_data(ziploc, extractloc):
    """Function to extract a zipfile to a location
    
    Args:
        ziploc: Location of zipfile for extracting
        extractloc: directory for extracting ziploc into

    Returns:
        None
    """
    if os.path.exists(extractloc):
        raise FileExistsError(f"File {extractloc} already exists.")
    else:
        os.makedirs(extractloc)
    
    with zipfile.ZipFile(ziploc, 'r') as zip_ref:
        zip_ref.extractall(extractloc)


if __name__ == '__main__':
    main()