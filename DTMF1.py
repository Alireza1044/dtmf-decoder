import numpy as np

decode = {
    '1': [1209, 697],
    '2': [1336, 697],
    '3': [1477, 697],
    'A': [1633, 697],

    '4': [1209, 770],
    '5': [1336, 770],
    '6': [1477, 770],
    'B': [1633, 770],

    '7': [1209, 852],
    '8': [1336, 852],
    '9': [1477, 852],
    'C': [1633, 852],

    '*': [1209, 941],
    '0': [1336, 941],
    '#': [1477, 941],
    'D': [1633, 941],
}


def check(f, freqs, offset):
    energy_low = 0
    energy_high = 0
    res = ''
    for char, freq in decode.items():
        r0 = range(freq[0] - offset, freq[0] + offset + 1)
        r1 = range(freq[1] - offset, freq[1] + offset + 1)
        for i in range(len(r0)):
            if r0[i] in freqs and r1[i] in freqs and (f[int(r0[i])] > energy_low or f[int(r1[i])] > energy_high):
                res = char
                energy_low = f[int(r0[i])]
                energy_high = f[int(r1[i])]

    return res


def DTMF(signal, rate):
    result = ''
    f = np.fft.fft(signal, rate)

    for i in range(len(f)):
        f[i] = int(np.absolute(f[i]))

    lower_bound = np.average(f) * 11

    freqs = np.argwhere(f > lower_bound)

    offset = 0

    for i in range(freqs.size):
        r = range(freqs[i][0] - offset, freqs[i][0] + offset + 1)
        flag = False
        for j in r:
            if len(f) - j in freqs:
                flag = True
                continue
        if not flag:
            np.delete(freqs, i)

    offset = 2
    result = check(f, freqs, offset)

    return result
