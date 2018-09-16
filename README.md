# gfortran Visual Studio Code Adapter

Fortran is always a big headache for modern-day programmers. But many people has make their effects. [Fortran Breakpoint Support](https://github.com/ekibun/FortranBreaker) has made fortran debuggable with [Visual Studio Code](https://github.com/Microsoft/vscode) (vscode).

However, parsing `gfortran`'s output is another headache, because of the abnormal output format of `gfortran` and the unavailability of modifying the output format of `gfortran` makes vscode's problemMatcher functionality unusable.

The target of this project is to make `gfortran`'s seriously fucked-up output capturable to Visual Studio Code's [`problemMatcher`](https://code.visualstudio.com/docs/editor/tasks#_defining-a-problem-matcher) for tasks.

## Usage

Provide whatever you want to call on `gfortran` to the `fuck_gfortran.py` program, it will make everything parsable.

Then write the vscode problemMatcher pattern as follows:
```json
{
    "problemMatcher": [
        {
            "fileLocation": "absolute",
            "pattern": {
                "regexp": "^(.*):(\\d+):(\\d+):(\\S+): (.*)",
                "file": 1,
                "line": 2,
                "column": 3,
                "severity": 4,
                "message": 5,
                "code": 6
            }
        }
    ],
}
```
