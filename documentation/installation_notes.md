# Installing ModelSim
Please note that this installation documentation is by no means exhaustive. If you run into any issues during the installation process, or find any distro-specific requirements, please open an issue and let us know.

## Linux
### Debian Stretch
_tested on kernel 4.9.0 x64_

1) Modify `vco` file located at `modelsim_ase/vco` to allow use of linux kernels above 3.x.

Find the snippet
```bash
      case $utype in
        2.4.[7-9]*)       vco="linux" ;;
        2.4.[1-9][0-9]*)  vco="linux" ;;
        2.[5-9]*)         vco="linux" ;;
        2.[1-9][0-9]*)    vco="linux" ;;
        3.[0-9]*)         vco="linux" ;;
        *)                vco="linux_rh60" ;;
      esac
```

and modify it to be
```bash
      case $utype in
        2.4.[7-9]*)       vco="linux" ;;
        2.4.[1-9][0-9]*)  vco="linux" ;;
        2.[5-9]*)         vco="linux" ;;
        2.[1-9][0-9]*)    vco="linux" ;;
        3.[0-9]*)         vco="linux" ;;
        4.[0-9]*)         vco="linux" ;;
        *)                vco="linux_rh60" ;;
      esac
```

2) Add 32 bit architecture to DPKG.

```bash
dpkg --add-architecture i386
```
```bash
apt-get update
```

3) Install 32 bit dependencies

```bash
sudo apt-get install libxft2 libxft2:i386 lib32ncurses5
```
4) Modify `vco` file located at `modelsim_ase/vco` to allow use of older version of freetype2.

Find the snippet
```bash
dir=`dirname "$arg0"`
```

and add the following after it
```bash
export LD_LIBRARY_PATH=${dir}/../lib32
```

5) Copy a version of freetype2 2.5.0.1-1 library files to the `lib32` directory specified.

The files required are:
```
libfreetype.so
libfreetype.so.6
libfreetype.so.6.10.2
```
