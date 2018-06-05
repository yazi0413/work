class login:
    def __init__(self):
        self.ip_pre="217.87"
        
    #get local IP
    def getIP(self):
        local_ip=socket.gethostbyname(socket.gethostname())
        if self.ip_pre in str(local_ip):
            return str(local_ip)
        ip_lists=socket.gethostbyname_ex(socket.gethostname())

        for ip_list in ip_lists:
            if isinstance(ip_list,list):
                for i in ip_list:
                    if self.ip_pre in str(i):
                        return str(i)
                    elif type(ip_list) is type.StringType:
                        if self.ip_pre in ip_list:
                            return ip_list

login=login()
