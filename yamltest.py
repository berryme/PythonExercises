import yaml
import configparser


def read_yaml(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def dict_to_ini():
    config = {
        'user': 'ssluser',
        'password': 'password',
        'host': '127.0.0.1',
        'client_flags': 'SSL',
        'ssl_ca': '/opt/mysql/ssl/ca.pem',
        'ssl_cert': '/opt/mysql/ssl/client-cert.pem',
        'ssl_key': '/opt/mysql/ssl/client-key.pem',
    }
    parser = configparser.ConfigParser()
    parser.read(config)
    with open('config2.ini', 'w') as writer:
        parser.write(writer)
    return config


def main():
    yaml = read_yaml('config.yaml')
    dict_to_ini()
    print(yaml)



    if __name__ == "__main__":

        main()
