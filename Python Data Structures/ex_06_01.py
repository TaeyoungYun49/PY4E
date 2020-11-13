text = 'X-DSPAM-Confidence:    0.8475'
pos = text.find('0.8475')
print(float(text[pos:]))
print('Text Type:', type(text))
print('Pos Type:', type(pos))
