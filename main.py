import json

import requests
import xmltodict

request = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://cps.huawei.com/cpsinterface/api_requestmgr" xmlns:req="http://cps.huawei.com/cpsinterface/request" xmlns:com="http://cps.huawei.com/cpsinterface/common">
   <soapenv:Header/>
   <soapenv:Body>
      <api:Request>
         <req:Header>
            <req:Version>1.0</req:Version>
            <req:CommandID>InitTrans_C2B Online Payment Request</req:CommandID>
            <req:OriginatorConversationID>S_X20171211143322046</req:OriginatorConversationID>
            <req:Caller>
               <req:CallerType>2</req:CallerType>
               <req:ThirdPartyID>serdo</req:ThirdPartyID>
               <req:Password>MEFgDcvzQdY=</req:Password>
               <req:ResultURL>http://equbde.com:31794/dequbcbedigital/result/</req:ResultURL>
            </req:Caller>
            <req:KeyOwner>1</req:KeyOwner>
            <req:Timestamp>20150101010101</req:Timestamp>
         </req:Header>
         <req:Body>
            <req:Identity>
               <req:Initiator>
                  <req:IdentifierType>11</req:IdentifierType>
                  <req:Identifier>Eba01</req:Identifier>
                  <req:SecurityCredential>A30pWRG8depVJtCDLpnSpg==</req:SecurityCredential>
                  <req:ShortCode>369589</req:ShortCode>
               </req:Initiator>
               <req:PrimaryParty>
                  <req:IdentifierType>1</req:IdentifierType>
                  <req:Identifier>251985028197</req:Identifier>
               </req:PrimaryParty>
               <req:ReceiverParty>
                  <req:IdentifierType>4</req:IdentifierType>
                  <req:Identifier>369589</req:Identifier>
               </req:ReceiverParty>
            </req:Identity>
            <req:TransactionRequest>
               <req:Parameters>
                  <req:Amount>10.0</req:Amount>
                  <req:Currency>ETB</req:Currency>
               </req:Parameters>
            </req:TransactionRequest>
            <req:ReferenceData>
               <req:ReferenceItem>
                  <com:Key>POSDeviceID</com:Key>
                  <com:Value>POS234789</com:Value>
               </req:ReferenceItem>
            </req:ReferenceData>
         </req:Body>
      </api:Request>
   </soapenv:Body>
</soapenv:Envelope>"""

def print_hi(name):
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    url = 'http://172.30.10.3:8081/payment/services/APIRequestMgrService'
    response = requests.post(url=url, data=request, headers=headers)
    print(response.content)

    decoded_response = response.content.decode('utf-8')
    response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
    print(response_json)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
