def include(file_path, lib_name, lib_path, soft=True):
    """

    :param path: Path where the file is t
    :param lib_dict: A dictionary with the name of the library as the key and the path as the value.
    :return:
    """
    with open(path,"w") as file:
        for line in file:
            line = line.strip()
            line = line.split()
            if len(line) == 3:
                if line[1] == lib_name and line[0] ==:
                    break
        if lib_dict is not None:
            for name, lib_path in lib_dict:
                printf(file,)