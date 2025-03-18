

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from dotenv import load_dotenv
import random, time
load_dotenv()
import os
# A random prog rammatic shadow client ID .

SHADOW_CLIENT = "myShadowClient10"


HOST_NAME = os.getenv('H_Name')

# The relative path to the correct root CA file for &IoT;,# which ypu have already saved onto this device .

ROOT_CA = "AmazonRootCA1.pem"

# The relative path to your private key file that# &IoT; generated for this device, which you

# have already saved onto this device .

PRIVATE_KEY = "private.pem.key"

# The relative path to your certificate file that# &IoT; generated for this device, which you

# have already saved onto this device .

CERT_FILE = "certificate.pem.crt"

# A programmatic shadow handler name prefix .

SHADOW_HANDLER = "Temperature_and_Humidity_Sensor"

# Automatically called whenever the shadow is updated .

def myShadowUpdateCallback(payload, responseStatus, token):
    print()

    # print( 'UPDATE: $aws things/' + SHADOW_HANDLER + '/ shadow/update/#' )
    #
    # print("payload = " + payload)
    #
    # # print (" responseStatus = " + responseStatus )
    #
    # print("token = " + token)

# Create, configure, and connect a shadow client .

myShadowClient = AWSIoTMQTTShadowClient( SHADOW_CLIENT)
myShadowClient.configureEndpoint (HOST_NAME, 8883)

myShadowClient.configureCredentials (ROOT_CA, PRIVATE_KEY,CERT_FILE)

myShadowClient.configureConnectDisconnectTimeout(10)

myShadowClient.configureMQTTOperationTimeout(5)

myShadowClient.connect()

# Create a prog rammatic representation of the shadow ,

myDeviceShadow = myShadowClient.createShadowHandlerWithName(SHADOW_HANDLER, True)


while True:

    tempreading = random.uniform(60.0, 70.0)  # Generating Temperature Readings

    message = '{"temperature":' + str(tempreading) + '}'

    myDeviceShadow.shadowUpdate( message, myShadowUpdateCallback, 5)

    time.sleep(5)


