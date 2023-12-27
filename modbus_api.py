"""
Author : HARSHAD M. KANANI
Date : 26-12-2023
Description : API for Receive Modbus Data.
"""


from flask import Flask, request
import json
from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusAsciiFramer
import time


client = ModbusSerialClient(port='COM3', timeout=2, baudrate=9600, parity='E', stopbits=1, bytesize=7, method = 'ascii',framer=ModbusAsciiFramer)
print(client)
client.connect()


app = Flask(__name__)

@app.route("/harshad", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return "welcome Harshad :::: GET"
    else:
        return "Hello???????"
    
    
    
@app.route("/modbus_data1", methods = ['GET', 'POST'])
def modbus_data1():

    try:
        if request.method == "GET":
            
            rr = client.read_holding_registers(address = 4096, count = 100, slave = 1)
            
            data = rr.registers

            print("Length of Data ::::", len(data))
            print("Data:::::", data)
            json_data = {}
            json_data["Register_Data"] = data
            json_data["Time_Stamp"] = time.strftime('%Y-%m-%d %H:%M:%S')
            Send_data = json.dumps(json_data)
            
            print("Send_data:::::::", Send_data)
        
            return Send_data
        else:
            return "Please use GET method only....."

    except Exception as e:
        print(e)
        return "Server is not responding. Please check your method"

    
    
if __name__ == '__main__':  

    app.run(host='0.0.0.0', port=5001,debug=True)