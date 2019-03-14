# -*- coding: utf-8 -*-
import os

def main(RF, RFPLL, TF, TFPLL, IFPLL, BASE_O, SPAN, CLK):
    IF = BASE_O + IFPLL
    S = []
    name = []
    i = []
    a, b = mul(IFPLL, CLK, SPAN)
    name.append('IFPLL_CLK')
    S.append(a)
    i.append(b)
    a, b = mul(IF, CLK, SPAN)
    name.append('IF_CLK')
    S.append(a)
    i.append(b)
    a, b = mul(TFPLL, CLK, SPAN)
    name.append('TFPLL_CLK')
    S.append(a)
    i.append(b)
    a, b = mul(TF, CLK, SPAN)
    name.append('TF_CLK')
    S.append(a)
    i.append(b)
    a, b = mul(RFPLL, CLK, SPAN)
    name.append('RFPLL_CLK')
    S.append(a)
    i.append(b)
    a, b = mul(RF, CLK, SPAN)
    name.append('RF_CLK')
    S.append(a)
    i.append(b)

    a, b = mul(TFPLL, IFPLL, SPAN)
    name.append('TFPLL_IFPLL')
    S.append(a)
    i.append(b)
    a, b = mul(TF, IFPLL, SPAN)
    name.append('TF_IFPLL')
    S.append(a)
    i.append(b)
    a, b = mul(RFPLL, IFPLL, SPAN)
    name.append('RFPLL_IFPLL')
    S.append(a)
    i.append(b)
    a, b = mul(RF, IFPLL, SPAN)
    name.append('RF_IFPLL')
    S.append(a)
    i.append(b)

    a, b = mul(TFPLL, IF, SPAN)
    name.append('TFPLL_IF')
    S.append(a)
    i.append(b)
    a, b = mul(TF, IF, SPAN)
    name.append('TF_IF')
    S.append(a)
    i.append(b)
    a, b = mul(RFPLL, IF, SPAN)
    name.append('RFPLL_IF')
    S.append(a)
    i.append(b)
    a, b = mul(RF, IF, SPAN)
    name.append('RF_IF')
    S.append(a)
    i.append(b)

    m = RF // CLK + 1
    n1 = RF // IFPLL + 1
    n2 = RF // IF + 1
    a, b = modulation(RF, CLK, IFPLL, m, n1, SPAN)
    name.append('RF_CLK_IFPLL')
    S.append(a)
    i.append(b)
    a, b = modulation(RFPLL, CLK, IFPLL, m, n1, SPAN)
    name.append('RFPLL_CLK_IFPLL')
    S.append(a)
    i.append(b)
    a, b = modulation(TF, CLK, IFPLL, m, n1, SPAN)
    name.append('TF_CLK_IFPLL')
    S.append(a)
    i.append(b)
    a, b = modulation(TFPLL, CLK, IFPLL, m, n1, SPAN)
    name.append('TFPLL_CLK_IFPLL')
    S.append(a)
    i.append(b)

    a, b = modulation(RF, CLK, IF, m, n2, SPAN)
    name.append('RF_CLK_IF')
    S.append(a)
    i.append(b)
    a, b = modulation(RFPLL, CLK, IF, m, n2, SPAN)
    name.append('RFPLL_CLK_IF')
    S.append(a)
    i.append(b)
    a, b = modulation(TF, CLK, IF, m, n2, SPAN)
    name.append('TF_CLK_IF')
    S.append(a)
    i.append(b)
    a, b = modulation(TFPLL, CLK, IF, m, n2, SPAN)
    name.append('TFPLL_CLK_IF')
    S.append(a)
    i.append(b)

    return S, name, i


def mul(F, F0, SPAN):
    F_1 = F - SPAN/2
    F_2 = F + SPAN/2
    a = F_2//F0 + 1
    x = []
    y = []
    for i in range(2,int(a)):
        if ((F0 * i > F_1) and (F0 * i < F_2)):
            x.append(F0 * i)
            y.append(i)
    return x, y

def modulation(F, F0, F1, m, n, SPAN):
    x = []
    y = []
    F_1 = F - SPAN/2
    F_2 = F + SPAN/2
    for i in range(1, int(m)):
        for j in range(1, int(n)):
            temp = F0 * i + F1 * j
            if temp > F_1 and temp < F_2:
                x.append(temp)
                y.append([i, j])
    return x, y

if __name__ == '__main__':
    RF = 2083.948
    RFPLL = 2013.984
    TF = 2244.984
    TFPLL = 1894.98
    IFPLL = 340.5
    BASE_O = 20
    SPAN = 20
    CLK = 40
    a1, a2, a3 = main(RF, RFPLL, TF, TFPLL, IFPLL, BASE_O, SPAN, CLK)
    for i in range(len(a2)):
        if (len(a1[i]) != 0):
            print(a2[i],len(a1[i]))
            str_name = a2[i]
            str_name = str_name.split('_')
            str_name = str_name[1]
            for j in range(len(a1[i])):
                print(j + 1, str_name, '*', a3[i][j], '=', a1[i][j])
        else:
            continue