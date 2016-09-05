import numpy as np

# global variable did not work
num_data = 0
# coding parameter
in_chars = 6
out_chars = 8
bits_per_char = 7


# convert samples to char-array
def init_data(xx, yy):
    global num_data
    num_data = len(xx)
    # print "x_samples before convert:\n", xx, "\n", "y_samples before convert:\n", yy
    x_result = np.chararray(len(xx)*in_chars).reshape((len(xx), in_chars))
    y_result = np.chararray(len(xx)*out_chars).reshape((len(xx), out_chars))
    for i in range(len(xx)):
        j = 0
        while j < in_chars:
            if j < len(xx[i]):
                x_result[i][j] = xx[i][j]
            else:
                x_result[i][j] = ' '
            j += 1
    for i in range(len(yy)):
        j = 0
        while j < out_chars:
            if j < len(yy[i]):
                y_result[i][j] = yy[i][j]
            else:
                y_result[i][j] = ' '
            j += 1

    return x_result, y_result


def Encoding(x_samples, y_samples):
    # all 0
    x_input = np.random.randint(0, 1, num_data * in_chars * bits_per_char).reshape(
        num_data, in_chars * bits_per_char)
    y_input = np.random.randint(0, 1, num_data * out_chars * bits_per_char).reshape(
        num_data, out_chars * bits_per_char)
    first_char = ' '
    # encoding parameter : decimal to binary
    for n in range(num_data):
        for i in range(in_chars):
            if x_samples[n][i] == '':
                 a = a_ = 0
            else:
                a = a_ = ord(x_samples[n][i]) - ord(first_char)
            # print chr(a+ord(' ')), " ",  a, " in binary is : ",
            for j in range(bits_per_char):
                x_input[n][i * bits_per_char + j] = (-1 if (a % 2) == 0 else 1)
                a /= 2
                a_ /= 2

        for i in range(out_chars):
            if y_samples[n][i] == '':
                a = 0
            else:
                a = ord(y_samples[n][i]) - ord(first_char)
            for j in range(bits_per_char):
                y_input[n][i * bits_per_char + j] = (-1 if (a % 2) == 0 else 1)
                a /= 2
    # print "x_samples after encoding:\n",x_input
    # print "y_samples after encoding:\n",y_input
    return x_input, y_input


# decoding
def Decoding(output):
    global bits_per_char
    result = []
    k = len(output) / bits_per_char
    for i in range(k):
        p = 1
        a = 0
        # binary to decimal 01011 = 11
        for j in range(bits_per_char):
            b = output[i * bits_per_char + j]
            a += (0 if (b == -1) else 1) * p
            p *= 2
        result.append(chr(a+ord(' ')))
        print chr(a+ord(' ')),
    return result
