import yaml


def read_yaml(fpath, fname):
    full_path = os.path.join(fpath, fname)
    with open(full_path, 'r') as ifile:
        try:
            config = yaml.safe_load(ifile)

        except Exception as err:
            config = -1

        finally:
            ifile.close()

    return config
