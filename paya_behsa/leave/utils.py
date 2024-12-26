from kavenegar import *
import random


def sms_sender(mobile_number='09398413991'):
    try:
        api = KavenegarAPI('696A7055612B2F5949533237797149686E533157496A6868707775644C5356626944546348544C6B7759493D')
        random_code = random.randint(1000, 9999)
        params = {'sender': '2000660110', 'receptor': '09398413991', 'message': str(random_code)}
        api.sms_send(params)
        return random_code
    except Exception as e:
        return False


api = KavenegarAPI('696A7055612B2F5949533237797149686E533157496A6868707775644C5356626944546348544C6B7759493D')
random_code = random.randint(1000, 9999)
params = {'sender': '0018018949161', 'receptor': '09116757470', 'message': str(random_code)}
api.sms_send(params)

