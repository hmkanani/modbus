# PLC MODBUS DATA READ AND WRITE


## Read data

API : /read_data

Method : GET

Response Data Sample(JSON) : {"Register_Data": [  ], "Time_Stamp": "2024-01-07 16:41:17"} 

Error : Server is Not Responding. Please Check Your Method

Wrong Method Error : Please Use GET Method Only.....


## Write data

API : /write_data

Method : POST

Post Data Sample(JSON) : {"Start_Address": 4099, "Values": [12, 34]}

Response Data Sample(JSON) : {"result": 1} For Success.
                             
                             {"result": 0} For Failed.


Error : Server is Not Responding. Please Check Your Method

Wrong Method Error : Please Use POST Method Only.....
