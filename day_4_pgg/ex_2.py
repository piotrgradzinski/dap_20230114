"""
Write a function that will get document a number as an argument
(in this format "FV/BI/2023-1/10") and will return a dictionary
containing elements of this number.

Number consists of:
document type/department/year-quarter/number

Example:
split_document_number_to_parts("FV/BI/2023-1/10")

returns

{
    "document_type": "FV",
    "department": "BI",
    "year": "2023",
    "quarter": "1",
    "number": "10"
}

Extra
Throw an exception if number does not match the pattern. You can check it by the number of "/".
"""


def split_document_number_to_parts(document_number: str) -> dict:
    if document_number.count('/') != 3:
        raise ValueError('Document number must have 4 parts separated with "/".')

    parts = document_number.split('/')
    return {
        'document_type': parts[0],
        'department': parts[1],
        'year': parts[2].split('-')[0],
        'quarter': parts[2].split('-')[1],
        'number': parts[3]
    }


result = split_document_number_to_parts("FV/BI/2023-1/10")
print(result)
