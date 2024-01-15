"""
Author : HARSHAD M. KANANI
Date : 15-01-2024
Description : API for Receive Modbus Data.
"""
version = 'Ver_Main_15.01.2024'

from flask import Flask, request
import json
from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusAsciiFramer
import time


app = Flask(__name__)

@app.route("/harshad", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return "welcome Harshad :::: GET"
    else:
        return "Hello???????"
    
@app.route("/read_data", methods = ['GET', 'POST'])
def read_data():

    if request.method == "GET":
        json_data = {'Register_Data': [], 'Time_Stamp': time.strftime('%Y-%m-%d %H:%M:%S')}
        try:
        
            # client = ModbusSerialClient(port = 'COM6', timeout = 2, baudrate = 9600, parity = 'E', stopbits = 1, bytesize = 7, method = 'ascii',framer=ModbusAsciiFramer)
            # print(client) 4096 default add
            # client.connect()
        
            rr = client.read_holding_registers(address = 4096, count = 100, slave = 1)
            
            data = rr.registers
            
            # client.close()

            print(f"[ READ DATA ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] [ LENGTH : {len(data)} ] : {data} ")
            
            json_data["Register_Data"] = data
            json_data["Time_Stamp"] = time.strftime('%Y-%m-%d %H:%M:%S')
            
        except Exception as e:
            print(f"[ NOT READ ] [ {request.url_rule} ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : ERROR IN CLIENT DATA READ : ", e)
            return "Server is Not Responding. Please Check Your Method"
        
        print(f"[ SEND DATA ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : {json_data} ")
        return json.dumps(json_data)  
            
    else:
        print(f"[ WRONG METHOD ] [ {request.url_rule} ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ]")
        return "Please Use GET Method Only....."

@app.route("/write_data", methods = ['GET', 'POST'])
def write_data():
    if request.method == "POST":
        respone_msg = {"result": 0 }
        try:
            result = request.json
            # print("result::::::: ", result)
            addr = int(result["Start_Address"])
            val = result["Values"]
            co_unt = len(val)
            
            print(f"[ WRITE DATA ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : [ START ADDRESS : {addr} ] [ COUNT : {co_unt} ] [ VALUES : {val} ] ")
            ww = client.write_registers(address = addr, values = val, count = co_unt, slave = 1)
            respone_msg['result'] = 1
        
        except Exception as e:
            print(f"[ NOT READ ] [ {request.url_rule} ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : ERROR IN CLIENT DATA WRITE : ", e)
            return "Server is Not Responding. Please Check Your Method"
        
        return json.dumps(respone_msg)  
        
    else:
        print(f"[ WRONG METHOD ] [ {request.url_rule} ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ]")
        return "Please Use POST Method Only....."

 
 
def detect_port():
    global client
    
    client = ModbusSerialClient(port='COM6', timeout=2, baudrate=9600, parity='E', stopbits=1, bytesize=7, method = 'ascii',framer=ModbusAsciiFramer)
    print(client)
    client.connect()
    # client.   
    
if __name__ == '__main__':
    print(f"[ STARTING ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : WELCOME ")
    
    client = ModbusSerialClient(port = 'COM6', timeout = 2, baudrate = 9600, parity = 'E', stopbits = 1, bytesize = 7, method = 'ascii',framer=ModbusAsciiFramer)
    print(f"[ CLIENT ] [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] : [ {client} ] ")
    client.connect()

    app.run(host='0.0.0.0', port=5009, debug=True, use_reloader = False)