import numpy as np
import math as math
from writephrq import *

fglu  = 1.0e-3
ffe3  = 0.01
fsom  = 0.02
fmic  = 1.0e-6
glu_stoich = 0.4

fsom1o = fsom 
fsom2o = fsom

fsom1m = fsom
fsom2m = fsom

fsom3  = fsom

fferbo = 2.0*fmic 
fferbm = 2.0*fmic
fmeg   = fmic 
fbuf       = 1.0
o2scalar   = 1.0

fgluo = fglu 
fglum = fglu
ffe3o = ffe3
ffe3m = ffe3


ffe3co     = ffe3o 
ffe3cm     = ffe3m
ffe3ro     = ffe3o
ffe3rm     = ffe3m
ffe3to     = ffe3o
ffe3tm     = ffe3m
fgluco     = fgluo 
fglucm     = fglum
fgluro     = fgluo
fglurm     = fglum
fgluto     = fgluo
fglutm     = fglum
fsom1co    = fsom1o 
fsom1cm    = fsom1m
fsom1ro    = fsom1o
fsom1rm    = fsom1m
fsom1to    = fsom1o
fsom1tm    = fsom1m
fsom2co    = fsom2o
fsom2cm    = fsom2m
fsom2ro    = fsom2o
fsom2rm    = fsom2m
fsom2to    = fsom2o
fsom2tm    = fsom2m
fferbco    = fferbo 
fferbcm    = fferbm
fferbro    = fferbo
fferbrm    = fferbm
fferbto    = fferbo
fferbtm    = fferbm
fmegaco    = fmeg
fmegacm    = fmeg
fmegaro    = fmeg
fmegarm    = fmeg
fmegato    = fmeg
fmegatm    = fmeg
fmegh      = fmeg
 
totc = [0.045,  0.105, 0.104,  0.105,  0.074, 0.056]                #mol  total organic carbon
totw = [0.013588, 0.005854, 0.011788, 0.006379, 0.010690, 0.006620] #kg   water
tots = [1.41,    9.15,  3.21,   8.62,   4.31 , 8.38]                #g    soil dry mass
ph   = [5.02,    4.84,  5.21,   4.54,   5.23,  4.95]
cace = [6.370,  2.799, 0.057,  2.668,  1.026, 1.839]                #mM   acetate
cfe2 = [0.789, 22.234, 0.102, 22.973, 15.665, 7.177]                #mM   Fe
hdsp = [0.042528, 0.042528, 0.044005, 0.044005, 0.043575, 0.043575] #head space volume L
 
index = 0
writephrq('co', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fbuf, fgluco, fsom1co, fsom2co, fsom3, fferbco, fmegaco, fmegh, glu_stoich, o2scalar)
 
writephrq('co',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fbuf, fgluco, fsom1co, fsom2co, fsom3, fferbco, fmegaco, fmegh, glu_stoich, o2scalar)
 
writephrq('co',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fbuf, fgluco, fsom1co, fsom2co, fsom3, fferbco, fmegaco, fmegh, glu_stoich, o2scalar)
 
index = 1
writephrq('cm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fbuf, fglucm, fsom1cm, fsom2cm, fsom3, fferbcm, fmegacm, fmegh, glu_stoich, o2scalar)
 
writephrq('cm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fbuf, fglucm, fsom1cm, fsom2cm, fsom3, fferbcm, fmegacm, fmegh, glu_stoich, o2scalar)
 
writephrq('cm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fbuf, fglucm, fsom1cm, fsom2cm, fsom3, fferbcm, fmegacm, fmegh, glu_stoich, o2scalar)
 
index = 2
writephrq('ro', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fbuf, fgluro, fsom1ro, fsom2ro, fsom3, fferbro, fmegaro, fmegh, glu_stoich, o2scalar)
 
writephrq('ro',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fbuf, fgluro, fsom1ro, fsom2ro, fsom3, fferbro, fmegaro, fmegh, glu_stoich, o2scalar)
 
writephrq('ro',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fbuf, fgluro, fsom1ro, fsom2ro, fsom3, fferbro, fmegaro, fmegh, glu_stoich, o2scalar)
 
index = 3
writephrq('rm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fbuf, fglurm, fsom1rm, fsom2rm, fsom3, fferbrm, fmegarm, fmegh, glu_stoich, o2scalar)
 
writephrq('rm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fbuf, fglurm, fsom1rm, fsom2rm, fsom3, fferbrm, fmegarm, fmegh, glu_stoich, o2scalar)
 
writephrq('rm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fbuf, fglurm, fsom1rm, fsom2rm, fsom3, fferbrm, fmegarm, fmegh, glu_stoich, o2scalar)
 
index = 4
writephrq('to', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fbuf, fgluto, fsom1to, fsom2to, fsom3, fferbto, fmegato, fmegh, glu_stoich, o2scalar)
 
writephrq('to',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fbuf, fgluto, fsom1to, fsom2to, fsom3, fferbto, fmegato, fmegh, glu_stoich, o2scalar)
 
writephrq('to',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fbuf, fgluto, fsom1to, fsom2to, fsom3, fferbto, fmegato, fmegh, glu_stoich, o2scalar)
 
index = 5
writephrq('tm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fbuf, fglutm, fsom1tm, fsom2tm, fsom3, fferbtm, fmegatm, fmegh, glu_stoich, o2scalar)
 
writephrq('tm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fbuf, fglutm, fsom1tm, fsom2tm, fsom3, fferbtm, fmegatm, fmegh, glu_stoich, o2scalar)
 
writephrq('tm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fbuf, fglutm, fsom1tm, fsom2tm, fsom3, fferbtm, fmegatm, fmegh, glu_stoich, o2scalar)
 
 
