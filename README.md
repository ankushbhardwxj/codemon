![1](https://user-images.githubusercontent.com/40923324/104605895-15c8b600-56a5-11eb-90e6-3671556b8c82.PNG)


[![Join the chat at https://gitter.im/codemon-py/community](https://badges.gitter.im/codemon-py/community.svg)](https://gitter.im/codemon-py/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Making the competitive programming workflow faster, one `Ctrl+S` at a time !

Competitive programming setups suck ! This was the motivation behind creating codemon. Who wants to use Sublime Text with two inefficient windows for I/O anyways ? Also, what about the Vim Lovers ?

Codemon is a build tool that works on the terminal, and aims to make the workflow for competitive programming faster than ever. Codemon integrates flawlessly with popular editors such as VSCode, Sublime Text and obviously Vim (❤) !

- Just give the contest number, codemon will create a nice directory structure and will fetch all your testcases (inputs & outputs 💥) from CodeForces. 
- Hit `Ctrl+S` and codemon will compile your code, run it on the testcases fetched and show you the output.
- In case, your output is wrong, don't worry ! Codemon makes debugging easier by pointing out exactly where your output didn't match.
- Apart from that, codemon allows you to create multiple code templates for various competitions and pulls them just in time.

![4](https://user-images.githubusercontent.com/40923324/104611023-ae156980-56aa-11eb-920a-9f0ef5f29c71.PNG)


## Installation Instructions
There are many ways to install **Codemon**. 
### Installation from Pypi using pip
```
pip install codemon
```

### Installation from Github
- To install setuptools, use `pip install setuptools`
- Type `git clone https://github.com/ankingcodes/codemon.git` to clone the package
- Type `cd codemon`
- Type `sudo python3 setup.py install`
- Type `sudo python setup.py bdist_wheel`
- Install the package locally using `pip install .`

  This command will place `codemon` executable at `/usr/local/bin` so that it can 
  be executed anywhere.
- Type `codemon` and you are ready to go.

## CLI - commands
###  Initializing a contest
```
codemon init <contestName>
```
This command is used to create a new contest directory for a CodeForces contest. The value of `<contestName>` should include the Contest Number of the CodeForces Contest. Codemon automatically fetches the inputs and outputs for each problem in that round and creates the directory & file structure accordingly. We can also use flags such as `-cpp, -py, -java` along with the codemon init command to specify which extension will be used to create the files. 

For example, for Codeforces Round number 1472,
```
codemon init CodeForces1472
```
Contest URL - https://codeforces.com/contest/1472/

Codemon creates a directory structure as follows:

![5](https://user-images.githubusercontent.com/40923324/104612853-a0f97a00-56ac-11eb-92d0-3922b8685d78.PNG)

The `.in` and `.op` files contain inputs and outputs respectively.

### Initializing a single file
```
codemon init -n <fileName>.<extension>
```
Creates a single file using a default template.

### Listening for changes
```
codemon listen
```
Once codemon starts listening, it would capture all modifications on the contest files created, that is, when an users saves their code using `ctrl + s`, codemon will catch that file, compile it using the respective compiler for that file (currently supports C++), and run it using the inputs already fetched in the `.in` file. 

Codemon then displays the output from the program on the terminal and also matches it with the sample outputs given in `.op` file. In case, both the outputs don't match, Codemon would point exactly where the error has occurred.

A correct output looks as follows:

![6](https://user-images.githubusercontent.com/40923324/104614539-5d077480-56ae-11eb-8537-36a7053a3244.PNG)

An incorrect output looks as follows:

![7](https://user-images.githubusercontent.com/40923324/104614547-5e38a180-56ae-11eb-826a-ab20bfddba93.PNG)

### Codemon Help
There are many more commands available, which can be viewed using `codemon --help`.

## Contributions 
Don't hesitate to create issues and PRs for improving codemon. 
All contributions are welcome.

## License 
The MIT License 

Copyright (c) 2021 Ankush Bhardwaj