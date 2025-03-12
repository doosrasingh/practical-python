# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    records = []
    
    rows = csv.reader(lines, delimiter=delimiter)
    # Read the headers
    headers = next(rows) if has_headers else []       

    # If a column selector is given, find indices of the specified columns
    # Also narrow the set of headers used for the resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    
    for rowno, row in enumerate(rows, start=1):
        if not row:         # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]
        
        # Type conversion
        if types:
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue
        
        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)  

    return records
