class LogicGate():

    '''
        pargament:
                 label(str): gate name
                 out(bool):  Opt resualt

    '''
    def __init__(self, n):
        self.label = n
        self.out = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        return self._performGateLogic()
    
    def _performGateLogic(self):
        pass

class BinaryGate(LogicGate):
    def __init__(self, n, A=None, B=None):
        super(BinaryGate, self).__init__(n)
        self.pinA = A
        self.pinB = B

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')

    
class UnaryGate(LogicGate):
    def __init__(self, n, A=None):
        super(UnaryGate, self).__init__(n)
        self.pinA = A   

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            raise RuntimeError('Erroe: NO EMPTY PIN')

class AndGate(BinaryGate):
    '''
        andgate = AndGate('AndGate', True, True)
        andgate.getOutput()
    '''
    
    
    def __init__(self, n, A, B):
        super(AndGate, self).__init__(n, A, B)
    
    def _performGateLogic(self):
        if self.pinA and self.pinB:
            return True
        else:
            return False

class orGate(BinaryGate):
    def __init__(self, n, A, B):
        super(orGate, self).__init__(n, A, B)

    def _performGateLogic(self):
        if self.pinA or self.pinB:
            return True
        else:
            return False

class NorGate(UnaryGate):
    def __init__(self, n, A):
        super(NorGate, self).__init__(n, A)
    
    def _performGateLogic(self):
        return not self.pinA

class Connector:
    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromGate
    
    def getTo(self):
        return self.togate


