#!/usr/bin/env python
# -*- coding: utf-8 -*-

def PrimeList(ustsinir):
    prime=[True for i in range(ustsinir + 1)]
    p=2

    while p * p <= ustsinir:
        if prime[p] == True:
            for i in range(p * 2, ustsinir + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, ustsinir + 1):
        if prime[p]:
            print(p)
