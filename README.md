# CBEBirr integration

```python
import cbebirr

if __name__ == '__main__':
    cbebirr.push_ussd(
        thirdPartyID='THIRD_PARTY_ID', 
        primaryPartyIdentifier='PHONE',
        receiverPartyIdentifier='CUSTOMER_ID',
        intiatorIdentifier='IDENTIFIER',
        securityCredential='SECURITY_CREDENTIAL',
        posDeviceID='POS_DEVICE_ID', 
        shortCode='SHORT_CODE', 
        amount='10', 
        password='PASSWORD',
        timestamp='TIME_STAMP',
        resultURL='RETURN_URL', )

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

```