class LogicGate:
    def __init__(self, label):
        self.output = None
        self.label = label
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            return int(input("Get pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PIN TO CONNECT")

class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, label, status='Good'):
        BinaryGate.__init__(self, label)
        self.status = status
    
    def printStatus(self):
        return self.status

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        if self.getPin() == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.setNextPin(self)
    
    def getFrom(self):
        return self.from_gate
    
    def getTo(self):
        return self.to_gate
    
    

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g3.getPinB())
    print(g4.getOutput())

if __name__ == "__main__":
    main()

