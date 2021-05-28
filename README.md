# ICSSgen v2.1
![ICSSgen_icon](ICSSgen_icon.png)

Input file generator for 2D-ICSS (2D-NICS) calculation.

**Homepage** https://www.wangzhe95.net/program-icssgen

First released at 2021-04-19

Last updated at 2021-05-21

Author: Zhe Wang

ORCiD: [0000-0002-9996-586X](https://orcid.org/0000-0002-9996-586X)

## Statement of need
2D isochemical shielding surface (2D-ICSS) maps, also known as 2D-NICS (nuclear independent
chemical shift) maps, are useful tools for investigating the aromaticity of cyclic molecules.
A large number of ghost atoms, in addition to the target molecules, must be included in the
input file for 2D-ICSS calculations. After completing the calculations, the magnetic shielding
tensors of all ghost atoms must be extracted from the output files. This process is a huge and
tiresome task; therefore, we present ICSSgen and ICSScsv, two open-source, highly efficient,
and user-friendly Python programs, to easily generate 2D-ICSS maps.

More information about ICSScsv, please check [ICSScsv](https://github.com/wongzit/ICSScsv)

## Update history
### v2.1 (2021-05-18)
1. Bug fix: Maximum value of ICSS map range (not displayed in older version)
3. Executable file for Mac could running on both Intel and Apple M1 chip. (macOS 10.15 or newer)
1. Now you can customize grid quality through program.
2. More stable input file reader was introduced.

### v1.1 (2021-04-20)
1. Program will not be terminated by error inputting when specify the map range.
3. Bug fix.

### v1.0 (2021-04-19)
1. First release of ICSSgen.

## How to run
For detail informations, please check the user manual.

### For all platform
Python source code is provided, if your computer already installed Python IDE, you can run ICSSgen with:

`python3 ICSSgen_vxx_source.py`

Executable files for macOS/Linux/Windows are in **execufiles.zip**.

**NOTICE:** Python 3.7 or newer is recommended, ICSSgen may not work normally under Python 2.

### For macOS
1. Double click the executable file **ICSSgen_vxx_mac**.
2. Package with source code. If for some reason the (1) could not work, you can package 
ICSSgen by yourself. For more information, please check the manual.

### For Linux
Before running for the first time, you may need to add permission by:
`chmod +x ./path_to_ICSSgen/ICSSgen_vxx_linux`

Add following command to environmental variables (for bash):
`alias icssgen=./path_to_ICSSgen/ICSSgen_vxx_linux`
and you can run ICSSgen by `icssgen`.

### For Microsoft Windows
Executable file **ICSSgen_vxx_win.exe** has been provided, double click to run it.

## How to use
**NOTICE:** ICSSgen only generates input file for Gaussian (Gaussian Inc.). For more details, please check the program manual.

1. Prepare the input file including calculation route lines, title, charge and spin multiplicity, and Cartesian coordinate.

**EXAMPLE: Input file of benzene on XY plane**
```
%nprocshared=8
%mem=10GB
#p nmr=giao rb3lyp/6-31g(d)

Benzene_opt

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

2. Run ICSSgen.

3. Drag the input file to the program, and press Enter. 
```
Please specify the original input file path:
(e.g.: /ICSSgen/example/benzene.gjf)
(user input): /Users/wangzhe/Desktop/ICSSgen/example/benzene.gjf 
```

4. Specify the plane for ICSS calculation, please input "xy", "xz" or "yz" (Not case-sensitive).
```
Please specify the plane for ICSS map (XY, XZ, YZ):
(user input): xy
```

5. Specify the altitude  for ICSS calculation, for on-plane calculation, please input 0. The value is in angstrom.
```
Please input the altitude over the plane (in angstrom):
(user input): 1
```

6. Range specification. Please input two numbers (float is okay) separated by space, eg. -10 10, the range will be set as [-10,10].
```
Please specify the range of X axis (in angstrom, e.g., -10 10):
(user input): -5 5

Please specify the range of Y axis (in angstrom, e.g., -8 8):
(user input): -5.0 5.0
```

7. Grid quality: smaller value will give you a smoother ICSS map but more expensive calculation cost is needed. The default value is 0.2.
```
Please specify the grid quality (value smaller than 0.25 is recommanded):
(press Enter to use default value 0.2)
(user input): (ENTER)
ICSSgen will use grid quality of 0.2.
```

8. New input file named with **ICSS_plane_altitude.gjf** would be generated. You can submit this input file for Gaussian calculation. Enjoy!

## From author
If you found any bugs, please contact me (wongzit@yahoo.co.jp).

More information about me, please check my [personal website](https://www.wangzhe95.net).

 **Hope you enjoy this program!**
