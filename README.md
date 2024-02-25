# File naming conventions
All files you create must follow these naming conventions. Do not use any
symbols other than letters or numbers in the basenames of files. You may
use a single period before a file extension, such as in the name “myFile.pdf”
or “my_file.py”. Do not use periods in file names other than the single period
to separate the basename of the file from the extension of the file. Do not
use any whitespace characters in the names of files. You may use either
camel casing or underscores when you have multiple words in a file name.
For example, the name ”my file” should not be used since it has a space in
the name. Instead the file should be named using camel casing as ”myFile”
or using underscores as “my file”


# How to clone this repository
1. First ssh into your hpc cluster. __ssh <tcnj-username>@elsa.hpc.tcjn.edu__
2. locate the public key which should be under ___~/.ssh/id_ecdsa.pub___
3. Copy and paste that into you github ssh keys setting which is located at [github keys](https://github.com/settings/keys)


## Setup Instructions

To set up the virtual environment and install the required packages, follow these steps:

1. Ensure you have Python 3.6.8 or newer installed on your system. (on the hpc by default)

2. Clone the repository:
   ```bash
   git clone https://github.com/k-kahora/ML-Project1
   cd ML-Project1
   python -i ml.py
   >>> train_system(100)
   ```

