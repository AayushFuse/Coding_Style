import os
import pdb


def get_path(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    head, tail = os.path.split(filename)
    return head


filename = __file__
filename_path = get_path(filename)


pdb.set_trace()
print(f"path = {filename_path}")
