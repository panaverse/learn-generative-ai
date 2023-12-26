import yaml
# https://ioflood.com/blog/python-import/

with open('foo.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service)