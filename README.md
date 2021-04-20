# ICSSgen v1.2
Input file generator for ICSS (2D-NICS) calculation.

Last update: 2021-04-20

Author: Zhe Wang

Personal website: https://www.wangzhe95.net

## Update history 
### v1.2 (2021-04-20)
1. Now you can customize grid quality through program.
2. More stable input file reader was introduced.
3. Running on Linux platform was tested.

### v1.1 (2021-04-20)
1. Program will not be terminated by error inputting when specify the map range.
3. Bug fix.

## Platform
This program is working normally on macOS 11.2.3 on MacBook Air (M1, 2020) and Redhat EL 8.3 with Intel Core i7-10700.

## How to use
NOTICE: This program is only for Gaussian input.
1. Prepare the input file including calculation method, title, charge and spin multiplicity, and Cartesian coordiante.

**EXAMPLE: Input file of benzene on XY plane**
```
%nprocshared=8
%mem=8gb
#p rb3lyp/6-31+g(d) nmr

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
-3 3

Please specify the range of Y axis (in angstrom, eg. -8 8):
-3.0 3.0
```

7. New input file name with "ICSS_plane_altitude.gjf" would be generated. Now you can use this input file for Gaussian calculation. Enjoy!
```
2D-ICSS(XY,1.0) map in [X: -3.0 to 3.0, Y: -3.0 to 3.0].

==============================
Normal termination of ICSSgen.
==============================
```

## Problem
1. ~~Once you get the input file for ICSS calculation, please open it by text editor before submit to Gaussian calculation. Sometimes the unnecessary line-break in original input file may be remain to the ICSS input file, these line-break will cause error during calculation.~~
This problem has been fixed but I still recommand you to check the input file befor submitting to Gaussian.
```
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300
                                                                 # <--- this is unnecessary line-break
Bq      -3.0      -3.0      1.0
Bq      -3.0      -2.8      1.0
Bq      -3.0      -2.6      1.0
```
2. The program may not work normally on Windows due to file path problem. Further update is planned.

## From author
If you found any bugs, please contact me. (wongzit@yahoo.co.jp)
Hope you enjoy this program!
