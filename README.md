# ICSSgen
Input file generator for ICSS (2D-NICS) calculation.

Last update: 2021-04-20

Author: Zhe Wang

Personal website: https://www.wangzhe95.net


## How to use
NOTICE: This program is only for Gaussian input.
1. Prepare the input file including calculation method, title, charge and spin multiplicity, and Cartesian coordiante.

**EXAMPLE: Input file of benzene on XY plane**
```
%nprocshared=8
%mem=8gb
#p rb3lyp/6-31g(d) nmr

benzene//ICSS_on_XY

0 1
 C                 -1.33923600   -0.39585300    0.00000500
 C                 -0.32668500   -1.35773000    0.00006900
 C                  1.01242100   -0.96187800   -0.00005500
 C                  1.33920200    0.39596500    0.00000800
 C                  0.32679800    1.35770000    0.00006200
 C                 -1.01250100    0.96179800   -0.00005800
 H                 -2.38133000   -0.70401000   -0.00006600
 H                 -0.58108600   -2.41424500    0.00007900
 H                  1.80037500   -1.71023400   -0.00015400
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300

```

2. Run ICSSgen_v1.py, the program is coded under Python 3.9.

3. Drag input file to the program, and press Enter.
```
Please specify the original input file:
/Users/wangzhe/Desktop/benzene.gjf 
```

4. Specify the plane for ICSS calculation, please input "xy", "xz" or "yz" (Not case-sensitive).
```
Please specify the plane for ICSS map (XY, XZ, YZ):
xY
```

5. Specify the altitude for ICSS calulation, for on-plane calculation, please input 0. The value is in angstrom.
```
Please input the altitude over the plane (in angstrom):
1
```

6. Range specification. Please input two numbers (float is okay) separated by space, eg. -10 10, the range will be set as [-10,10].
```
Please specify the range of X axis (in angstrom, eg. -10 10):
-10 10

Please specify the range of Y axis (in angstrom, eg. -8 8):
-6.6 5.6
```

7. New input file name with "ICSS_plane_altitude.gjf" would be generated. Now you can use this input file for Gaussian calculation. Enjoy!
```
2D-ICSS(XY,1.0) map in [X: -10.0 to 10.0, Y: -6.6 to 5.6].


==============================
Normal termination of ICSSgen.
==============================
```

## Problem
Once you get the input file for ICSS calculation, please open it by text editor before submit to Gaussian calculation. Sometimes the unnecessary line-break in original input file may be remain to the ICSS input file, these line-break will cause error during calculation.
```
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300
                      # <--- this is unnecessary line-break
Bq      -10.0      -6.6      1.0
Bq      -10.0      -6.4      1.0
Bq      -10.0      -6.2      1.0
```

