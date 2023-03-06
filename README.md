[Photorec/TestDisk](https://www.cgsecurity.org/wiki/PhotoRec) is a tool for recovering erased data on a computer drive.

While it does an amazing job at finding files due to its brute force mechanism, this approach generates a lot of data (corrupted, duplicated and old) which probably isn't what you are looking for. Because of this, once the recovery is done, the goal is to *find a needle in a haystack of data*.

That's why I wrote this script. It will help you with: 

- Using [the amazing photorec sorter](https://github.com/tfrdidi/sort-PhotorecRecoveredFiles), walk each of the folders within a given 
data type superfolder (e.g sort/PY, sort/CPP,...)

- Read line by line each of the files to find the keywords you are looking for.

Hope you enjoy!
