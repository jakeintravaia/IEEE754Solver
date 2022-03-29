import math as m

global seperator
global precision
global expOffset
global signBit
global expDecimal
global mantDecimal

def main():
    global precision
    global seperator
    global signBit
    seperator = "="*25 # Create a text seperator to make it look pretty
    precision = 127 # Set our precision
    binNum = input("Enter IEEE-754 number (32-bits): ")
    bits = list(binNum) # Split our string input into a list
    signBit = int(bits[0]) # Select our sign bit
    #print("Sign bit: {}".format(signBit))
    expBits = bits[1:9] # Select our exponent bits
    #print("Exponent bits: {}".format(expBits))
    mantBits = bits[9:] # Select our mantissa bits
    #print("Mantissa bits: {}".format(mantBits))
    exponentBits(expBits)
    getOffset()
    mantissaBits(mantBits)
    decimalConversion()

def exponentBits(b):
    global seperator
    global expDecimal
    finalSum = 0
    power = 0
    print(seperator)
    print("EXPONENT BITS")
    print(seperator)
    for i in range(0, len(b)):
        if b[i] == '1':
            power = len(b) - (i + 1)
            print("2^{} * 1 = {}".format(power, int(m.pow(2,power))))
            finalSum += m.pow(2,power)
        elif b[i] == '0':
            print("2^{} * 0 = 0".format(power-1))
    print("Final decimal value: {}".format(int(finalSum)))
    expDecimal = finalSum

def getOffset():
    global precision
    global expDecimal
    global seperator
    global expOffset
    result = 0
    print(seperator)
    print("EXPONENT OFFSET")
    print(seperator)
    result = int(expDecimal) - int(precision)
    print("{} - {} = {}".format(int(expDecimal), precision, int(result)))
    expOffset = result

def mantissaBits(b):
    global seperator
    global mantDecimal
    finalSum = 0.0
    print(seperator)
    print("MANTISSA BITS")
    print(seperator)
    for i in range(0, len(b)):
        if b[i] == '1':
            print("2^{} * 1 = {}".format(-i-1, m.pow(2,-i-1)))
            finalSum += m.pow(2,-i-1)
        elif b[i] == '0':
            print("2^{} * 0 = 0".format(-i-1))
    print("Final decimal value: {}".format(finalSum))
    mantDecimal = finalSum

def decimalConversion():
    global seperator
    global signBit
    global mantDecimal
    global expOffset
    result = 0
    result = m.pow(-1,signBit) * (1 + mantDecimal) * m.pow(2, expOffset)
    print(seperator)
    print("FINAL RESULT")
    print(seperator)
    print("(-1)^{} * (1 + {}) * 2^{} = {}".format(signBit,mantDecimal,expOffset,result))
    
main()
