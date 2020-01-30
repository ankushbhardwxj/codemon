# Codemon 
### A CLI tool to ace Competitive Programming Contests.

Mostly, the time of a competitive programmer is wasted in compiling, adding inputs, 
and debugging. Typing commands again and again wastes time, which we cannot afford 
during a contest. 

#### Codemon takes care of everything else so that you only focus on writing correct code and implementing complex algorithms.

Note: Codemon currently supports C++ only. 

## How to install ?
- Type `git clone https://github.com/ankingcodes/codemon.git` to clone the package
- Type `cd codemon`
- Install the package locally using `pip install .`
  This command will place `codemon` executable at `/usr/local/bin` so that it can 
  be executed anywhere.

## CLI - commands
   ```
   codemon init <contestName>
   ```
    
  This creates a directory with the name of the contest and creates 6 `.cpp` files 
  as per contests in CodeForces.

  Copy your inputs for a respective coding question to the `input.txt` file.

  ```
  codemon listen 
  ```

  Type this command inside the directory of the contest(`cd contestName`). 
  It will start listening for changes in any of the files. Make changes to any 
  of the `.cpp` files and save it. 
  As soon as a file is saved, codemon recognizes it, compiles it and produces 
  output corresponding to the `input.txt` file. 

  Works flawlessly with VSCode.

## Contributions 
Don't hesitate to create issues and PRs for improving codemon. 
