def split_document_number_to_parts(document_number):
    parts = document_number.split('/')
    if len(parts) != 4:
        raise ValueError('Doc numb must have four characters with \' / \'.')

    year_quarter, number = parts[2].split('-'), parts[3]

    if len(year_quarter) != 2:
        raise ValueError("Error: Invalid document number format")

    year, quarter = year_quarter[0], year_quarter[1]

    return {
        'document_type': parts[0],
        'department': parts[1],
        'year': year,
        'quarter': quarter,
        'number': number
    }


document_number = "FV/BI/2023-1/10"
try:
    result = split_document_number_to_parts(document_number)
    print(result)
except ValueError as error:
    print(error)
