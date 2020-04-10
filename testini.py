import configparser


cf = configparser.ConfigParser()
cf.read('conf.ini', encoding='utf-8')
secs = cf.sections()
opts = cf.options('email')
print(secs, opts)
