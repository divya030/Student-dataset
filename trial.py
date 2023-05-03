def get_requirements(file_path:str):
    """
    this function will return the list of requirements
    """

    requirements = []
    HYPEN_E_DOT = "-e ."

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n',"")    for i in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


print(get_requirements('requirements.txt'))