import json, os
import requests
import xmltodict
from collections import OrderedDict
from hashlib import sha256
from urllib.parse import urlencode

def push_ussd(thirdPartyID,
              password,
              resultURL,
              timestamp,
              intiatorIdentifier,
              securityCredential,
              shortCode,
              primaryPartyIdentifier,
              receiverPartyIdentifier,
              amount,
              posDeviceID,
              currency='ETB', url="http://172.30.10.3:8081/payment/services/APIRequestMgrService"):
    request = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://cps.huawei.com/cpsinterface/api_requestmgr" xmlns:req="http://cps.huawei.com/cpsinterface/request" xmlns:com="http://cps.huawei.com/cpsinterface/common">
       <soapenv:Header/>
       <soapenv:Body>
          <api:Request>
             <req:Header>
                <req:Version>1.0</req:Version>
                <req:CommandID>InitTrans_C2B Online Payment Request</req:CommandID>
                <req:OriginatorConversationID>S_X20171211143322046</req:OriginatorConversationID>
                <req:Caller>
                   <req:CallerType>2</req:CallerType>
                   <req:ThirdPartyID>{thirdPartyID}</req:ThirdPartyID>
                   <req:Password>{password}=</req:Password>
                   <req:ResultURL>{resultURL}</req:ResultURL>
                </req:Caller>
                <req:KeyOwner>1</req:KeyOwner>
                <req:Timestamp>{timestamp}</req:Timestamp>
             </req:Header>
             <req:Body>
                <req:Identity>
                   <req:Initiator>
                      <req:IdentifierType>11</req:IdentifierType>
                      <req:Identifier>{intiatorIdentifier}</req:Identifier>
                      <req:SecurityCredential>{securityCredential}</req:SecurityCredential>
                      <req:ShortCode>{shortCode}</req:ShortCode>
                   </req:Initiator>
                   <req:PrimaryParty>
                      <req:IdentifierType>1</req:IdentifierType>
                      <req:Identifier>{primaryPartyIdentifier}</req:Identifier>
                   </req:PrimaryParty>
                   <req:ReceiverParty>
                      <req:IdentifierType>4</req:IdentifierType>
                      <req:Identifier>{receiverPartyIdentifier}</req:Identifier>
                   </req:ReceiverParty>
                </req:Identity>
                <req:TransactionRequest>
                   <req:Parameters>
                      <req:Amount>{amount}</req:Amount>
                      <req:Currency>{currency}</req:Currency>
                   </req:Parameters>
                </req:TransactionRequest>
                <req:ReferenceData>
                   <req:ReferenceItem>
                      <com:Key>POSDeviceID</com:Key>
                      <com:Value>{posDeviceID}</com:Value>
                   </req:ReferenceItem>
                </req:ReferenceData>
             </req:Body>
          </api:Request>
       </soapenv:Body>
    </soapenv:Envelope>
    """.format(
        thirdPartyID=thirdPartyID,
        password=password,
        resultURL=resultURL,
        timestamp=timestamp,
        intiatorIdentifier=intiatorIdentifier,
        securityCredential=securityCredential,
        shortCode=shortCode,
        primaryPartyIdentifier=primaryPartyIdentifier,
        receiverPartyIdentifier=receiverPartyIdentifier,
        amount=amount,
        currency=currency,
        posDeviceID=posDeviceID
    )
    print(request)
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    response = requests.post(url=url, data=request, headers=headers)
    print(response.content)

    decoded_response = response.content.decode('utf-8')
    response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
    print(response_json)
    return response_json


def refund(thirdPartyID,
           password,
           resultURL,
           timestamp,
           intiatorIdentifier,
           securityCredential,
           shortCode,
           primaryPartyIdentifier,
           receiverPartyIdentifier,
           amount,
           posDeviceID,
           phone,
           currency='ETB', url="http://172.30.10.3:8081/payment/services/APIRequestMgrService"):
    request = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://cps.huawei.com/cpsinterface/api_requestmgr" xmlns:req="http://cps.huawei.com/cpsinterface/request" xmlns:com="http://cps.huawei.com/cpsinterface/common">
    <soapenv:Header/>
    <soapenv:Body>
      <api:Request>
        <req:Header>
          <req:Version>1.0</req:Version>
          <req:CommandID>InitTrans_Salary Payment</req:CommandID>
          <req:OriginatorConversationID>426494503</req:OriginatorConversationID>
          <req:Caller>
            <req:CallerType>2</req:CallerType>
             <req:ThirdPartyID>{thirdPartyID}</req:ThirdPartyID>
             <req:Password>{password}=</req:Password>
             <req:ResultURL>{resultURL}</req:ResultURL>
          </req:Caller>
          <req:KeyOwner>1</req:KeyOwner>
          <req:Timestamp>{timestamp}</req:Timestamp>
        </req:Header>
        <req:Body>
          <req:Identity>
            <req:Initiator>
                <req:IdentifierType>11</req:IdentifierType>
                    <req:Identifier>{intiatorIdentifier}</req:Identifier>
                      <req:SecurityCredential>{securityCredential}</req:SecurityCredential>
                      <req:ShortCode>{shortCode}</req:ShortCode>
                   </req:Initiator>
                   <req:ReceiverParty>
                      <req:IdentifierType>1</req:IdentifierType>
                      <req:Identifier>{phone}</req:Identifier>
                   </req:ReceiverParty>
          </req:Identity>
          <req:TransactionRequest>
            <req:Parameters>
                <req:Amount>{amount}</req:Amount>
                <req:Currency>{currency}</req:Currency>
            </req:Parameters>
          </req:TransactionRequest>
        </req:Body>
      </api:Request>
    </soapenv:Body>
    </soapenv:Envelope> 
    """.format(
        thirdPartyID=thirdPartyID,
        password=password,
        resultURL=resultURL,
        timestamp=timestamp,
        intiatorIdentifier=intiatorIdentifier,
        securityCredential=securityCredential,
        shortCode=shortCode,
        primaryPartyIdentifier=primaryPartyIdentifier,
        receiverPartyIdentifier=receiverPartyIdentifier,
        amount=amount,
        currency=currency,
        phone=phone
    )
    print(request)
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    response = requests.post(url=url, data=request, headers=headers)
    print(response.content)

    decoded_response = response.content.decode('utf-8')
    response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
    print(response_json)
    return response_json


def parse_xml_to_dict(xml):
    return json.dumps(xmltodict.parse(xml))["soapenv:Envelope"]["soapenv:Body"]["res:Body"]


def cbebirrplus_payment(tillCode, amount, transactionId, transactionTime, companyName, key, token, callBackURL):
    payload = {
        "tillCode": str(tillCode),
        "amount": str(amount),
        "transactionId": str(transactionId),
        "transactionTime": str(transactionTime),
        "companyName": companyName,
        "key": key ,
        "token": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjI1MTkyOTA3MTQ4NyIsImV4cCI6MTY5NzQ5MjA4OH0.zRBQVQ91WckpvzWga0c5srdHi0WDmziZaVtPiCWGT_A',
        "callBackURL": callBackURL
    }
    # payload = {
    #     "tillCode": "1234",
    #     "amount": "1.00",
    #     "transactionId": "70098",
    #     "transactionTime": "2023-09-16 13: 54: 55.057044+00: 00",
    #     "companyName": "Guzo",
    #     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjI1MTkyOTA3MTQ4NyIsImV4cCI6MTY5ODU5NzM3MX0.RjNZJ6AkulDWlJ2eRireeRCFxZbdUpfDcPS9QurJFTo",
    #     "callBackURL": "https://google.com",
    #     "signature": "967a46315b90cd09961a1253f7edb216914fb7389cdfd946df1bd629b1c41ddd"
    # }

    sorted_payload = dict(OrderedDict(sorted(payload.items())))
    print(sorted_payload)
    hash_list = []
    for x, y in sorted_payload.items():
        hash_list.append(x +'=' +y)
    hash_str = '&'.join(hash_list)
    # hash_str = urlencode(sorted_payload)
    print(hash_str)
    signiture = sha256(hash_str.encode('utf-8')).hexdigest()
    del payload['key']
    payload['signature'] = signiture
    print(payload)

    # url = "https://8c50-196-191-60-207.ngrok-free.app/pay"
    url = "https://cbebirrpaymentgateway.cbe.com.et:8888/auth/pay"

    payload = json.dumps(payload)
    # {
    #     "tillCode": "1234",
    #     "amount": "1.00",
    #     "transactionId": "70098",
    #     "transactionTime": "2023-09-16 13: 54: 55.057044+00: 00",
    #     "companyName": "Guzo",
    #     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjI1MTkyOTA3MTQ4NyIsImV4cCI6MTY5ODU5NzM3MX0.RjNZJ6AkulDWlJ2eRireeRCFxZbdUpfDcPS9QurJFTo",
    #     "callBackURL": "https://google.com",
    #     "signature": "967a46315b90cd09961a1253f7edb216914fb7389cdfd946df1bd629b1c41ddd"
    # }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjI1MTkyOTA3MTQ4NyIsImV4cCI6MTY5NzQ5MjA4OH0.zRBQVQ91WckpvzWga0c5srdHi0WDmziZaVtPiCWGT_A'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print("Response: ", response.text)
    print("Status: ", response.status_code)
    if response.status_code == 200 or response.status_code == 201:
        return json.loads(response.content)
    else:
        return None
