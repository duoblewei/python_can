import visa
from ctypes import windll
import ctypes

# result = (ctypes.c_int * 100)()
# visaDLL = 'c:/windows/system32/visa64.dll'
# rm = visa.ResourceManager()
ip = '192.168.199.138'
# addr = "TCPIP::%s::INSTR" % ip
ip2 = '192.168.199.115'
# addr2 = "TCPIP::%s::INSTR" % ip2
# inst = rm.get_instrument(addr,timeout=10)
# inst = rm.open_resource(addr)
# # inst2 = rm.get_instrument(addr2,timeout=10)
# inst2 = rm.open_resource(addr2)

# R1 = result

class X_visa():
    def __init__(self):
        super(X_visa, self).__init__()
        visaDLL = 'c:/windows/system32/visa64.dll'
        self.rm = visaDLL.ResourceManager()

    def open(self):
        addr = "TCPIP::%s::INSTR" %ip
        try:
            self.inst = self.rm.open_resource(addr)
        except EnvironmentError as e:
            print(e)
        return self.inst.query("*IDN?")

    def output(self,state):
        if state == 1:
            self.inst.write("OUTP:ALL ON")
        else:
            self.inst.write("OUTP:ALL OFF")

    def w_FREQ(self,FREQ):
        self.inst.write("FREQ %s GHz" %FREQ)

    def w_LEVE(self,LEVE):
        self.inst.write("LEV %s dBm" %LEVE)

    def Freq_sweep(self,FREQ,MODE,SPAN,STEP,DWEL,LIN,TRI):
        self.inst.write("FREQ:MODE %s" %MODE)
        self.inst.write("FREQ:CENT %s GHz" %FREQ)
        self.inst.write("FREQ:SPAN %s KHz" %SPAN)
        self.inst.write("SWE:FREQ:STEP:LIN %s Hz" %STEP)
        self.inst.write("SWE:FREQ:DWEL %s ms" %DWEL)
        self.inst.write("SWE:SPAC %s" %LIN) #SWE:SPAC LOG  //RAMP
        self.inst.write("SOUR:SWE:SHAP %s" %TRI) #SWE:SHAP SAWT

    def w_MFREQ(self,INDEX,FREQ):
        self.inst.write("LFO%s:FREQ %%s KHz" % INDEX % FREQ)

    def w_MDEV(self,INDEX,DEV1 = None,DEV2 = None):
        if INDEX == 1:
            DEV = DEV1
        else:
            DEV = DEV2 / DEV1
        self.inst.write("PM%s:DEV %s"%INDEX %DEV)

    def modulation(self,INDEX,state):
        if state == 1:
            self.inst.write("PM%s:STATE ON"%INDEX)
        else:
            self.inst.write("PM%s:STATE OFF"%INDEX)

# print (inst.query("*IDN?"))
#
#
# inst.write("LEV 0 dBm")
# inst.write("FREQ 2 GHz")
#
# inst.write("PM:STATE ON")
# inst.write("PM2:STATE ON")
# inst.write("LFO2:FREQ 20 KHz")
#
# inst.write("OUTP:ALL OFF")
# inst.write("FREQ:MODE CW")
# inst.write("FREQ:MODE SWE")
# inst.write("SWE:FREQ:EXEC")
# inst.write("FREQ:CENT 2 GHz")
# inst.write("FREQ:SPAN 230 KHz")
# inst.write("SWE:FREQ:STEP:LIN 160 Hz")
# inst.write("SWE:FREQ:DWEL 5 ms")
#
# inst.write("PM:RAT 66.66")
# inst.write("PM1:DEV 0.6")
#
#
#
# inst2.write("CALC:DELT:BPOW:RES?")
# inst2.read()
#
# inst2.write("FREQ:CENT 2 GHz")
# inst2.write("FREQ:SPAN 230 KHz")
# DISP:TRAC:Y:RLEV -10dBm
# FREQ:CENT 100 MHz
# FREQ:CENT:STEP 10 MHz
# FREQ:CENT UP
# BAND 1 MHz
# inst2.write("BAND 30Hz")#BW
# inst2.write("CALC:DELT ON")
# inst2.write("CALC:MARK ON")
# inst2.write("INIT:CONT OFF")
# inst2.write("INIT;*WAI")
# inst2.write("CALC:MARK:Y?")
# inst2.write("CALC:DELT:Y?")
#
# inst2.write("CALC:DELT:LINK:TO:MARK2 ON")#跳到mark点上
# inst2.write("CALC:DELT:MREF 3")#会重新选取参考点
#
# inst2.write("CALC:MARK:X  131 KHz")
# inst2.write("CALC:DELT:X  131 KHz")
# # inst2.write("CALC:MARK:TRAC 1")
# # inst2.write("CALC:MARK:FUNC:FPE:SORT X")
# # inst2.write("CALC:MARK:FUNC:FPE 3;*WAI")
# # inst2.write("CALC:MARK:FUNC:FPE:Y?")
# inst2.read()