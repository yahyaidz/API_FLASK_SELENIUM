import yaml

def get_conf(file_path: str = "./conf.yml") -> dict:
    """
    Retrieve configuration settings from a YAML file.
    :param file_path: Path to the configuration YAML file.
    :return: Dictionary containing the configuration settings.
    """
    with open(file_path, "r") as file:
        configuration = yaml.safe_load(file)
    return configuration