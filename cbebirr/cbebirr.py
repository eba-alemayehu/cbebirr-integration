import json
import requests
import xmltodict


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
              currency='ETB', url="http://172.30.10.3:8081/payment/services/APIRequestMgrService"):
    request = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://cps.huawei.com/cpsinterface/api_requestmgr" xmlns:req="http://cps.huawei.com/cpsinterface/request" xmlns:com="http://cps.huawei.com/cpsinterface/common">
       <soapenv:Header/>
       <soapenv:Body>
          <api:Request>
             <req:Header>
                <req:Version>1.0</req:Version>
                <req:CommandID>InitTrans_Salary Payment</req:CommandID>
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
                      <req:IdentifierType>4</req:IdentifierType>
                      <req:Identifier>{receiverPartyIdentifier}</req:Identifier>
                   </req:ReceiverParty>
                </req:Identity>
                <req:TransactionRequest>
                   <req:Parameters>
                      <req:Amount>{amount}</req:Amount>
                      <req:Currency>{currency}</req:Currency>
                      <req:ReasonType>Cash IN</req:ReasonType>
                   </req:Parameters>
                </req:TransactionRequest>
                <req:Remark>Test</req:Remark>
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
        currency=currency
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