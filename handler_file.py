from utils import logger

'''logging.basicConfig(filename="newlogfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)'''

def function101(request_json):
    logger.info("function starting")
    return_json = {
        "Input": request_json,
        "Status": "Success",
        "Message": ""
    }
    try:
        if request_json['value'] > 10:
            variable_passed_value = {
                "Result": 15000
            }
        else:
            #variable_passed_value = {
            #    "Result": 25000
            #}
            raise Exception ("This is test of try/except")
        logger.info("this is a message")
        return_json["Message"]=variable_passed_value

    except Exception as e:
        return_json["Message"] = str(e)
        return_json["Status"] = "Failed"

    logger.info("return_json --> %s", str(return_json))
    return return_json