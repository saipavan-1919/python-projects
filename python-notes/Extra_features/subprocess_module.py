import subprocess

"""
    subprocess module:
        subprocess module is used to run process from the python scripts in the shell.
        This process allows us to spawn processes and connect input/output/error pipes, and obtain their return codes.

        It uses two methods to run the processes:
        1) subprocess.check_call   -> this calls the process and returns the status of the process.
        2) subprocess.check_output -> this calls the process and returns the output of process as a byte code (string)

        1.subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
        Parameters:
        args    =The command to be executed.Several commands can be passed as a string by separated by “;”.
        stdin   =Value of standard input stream to be passed as (os.pipe()).
        stdout  =Value of output obtained from standard output stream.
        stderr  =Value of error obtained(if any) from standard error stream.
        shell   =Boolean parameter.If True the commands get executed through a new shell environment.
        Return Value:
        The function returns the return code of the command.If the return code is zero, the function simply returns(command executed successfully) otherwise CalledProcessError is being raised.

        2.subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
        Parameters:
        args    =The command to be executed. Several commands can be passed as a string by separated by “;”.
        stdin   =Value of standard input stream to be passed as pipe(os.pipe()).
        stdout  =Value of output obtained from standard output stream.
        stderr  =Value of error obtained(if any) from standard error stream.
        shell   =boolean parameter.If True the commands get executed through a new shell environment.
        universal_newlines=Boolean parameter.If true files containing stdout and stderr are opened in universal newline mode.
        Return Value:
        The function returns the return code of the command.If the return code is zero, the function simply returns the output as a byte string(command executed successfully) otherwise CalledProcessError is being raised.

"""

# this executes the command and returns the status of the command execution (success returns 0,  failure returns CalledProcessError)
s = subprocess.check_call("python sample1.py", shell=True)  # here sample.py is another file
print(s)


# this executes the command and returns the output of the command as the byte code(string)
s1 = subprocess.check_output("python sample1.py", shell=True)
print(s1)

# we can decode the retuned value from check_output method into normal string using decode
print(s1.decode("utf-8"))
