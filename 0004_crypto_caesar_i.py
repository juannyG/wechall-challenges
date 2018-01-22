def caesar_shift_char_by_i(c, i):
    normalized_c = ord(c) - 65
    return chr((normalized_c + i) % 26 + 65)

s = "JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW EV SQUIQH QDT OEKH KDYGKU IEBKJYED YI EEFIDUCUCECT"
for i in xrange(26):
    print "".join([
        caesar_shift_char_by_i(c, i) if c != ' ' else ' ' for c in s
    ])
