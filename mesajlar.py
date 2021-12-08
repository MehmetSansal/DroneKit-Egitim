

mikrosaniye = 0
milisaniye = 0

def listen_SYSTEM_TIME(iha):
    @iha.on_message("SYSTEM_TIME")
    def listener(self,name,msg):
        global mikrosaniye
        global milisaniye
        
        milisaniye = msg.time_boot_ms
        mikrosaniye = msg.time_unix_usec
    return milisaniye, mikrosaniye
