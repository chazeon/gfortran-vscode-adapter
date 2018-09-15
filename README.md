# gfortran Visual Studio Code Adapter

Fortran is always a big headache for modern-day programmers. But many people has make their effects. [Fortran Breakpoint Support](https://github.com/ekibun/FortranBreaker) has made fortran debuggable with Visual Studio Code (vscode).

However, parsing `gfortran`'s output is another headache, because of the abnormal output format of `gfortran` and the unavailability of modifying the output format of `gfortran` makes vscode's problemMatcher functionality unusable.

The target of this project is to make gfortran's seriously fucked-up output capturable to Visual Studio Code's problemMatcher.
