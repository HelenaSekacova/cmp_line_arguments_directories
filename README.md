<a name="readme-top"></a>
# cmp_line_arguments_directories
Comparison of two folders provided by command line arguments included scheduled synchronization


### Prerequisites

Download and install python's version which suits you at [https://www.python.org/](https://www.python.org/). After that import following packages:
  ```sh
  import os,sys, filecmp, schedule, time, logging, shutil  
  ```



<!-- USAGE EXAMPLES -->
## Usage
In the repository are two files that compare two directories.
1. Comparison of titles or/and content of files in directories. (only titles of files => main_name.py; content => main_content.py)
2. after specification of path of files which is needed for **"command line arguments"**,
    * are specified source and target directories,
    * which are compared:

      -deleted_files are only in target

      -changed_files have different content that means target's file will be overwritten (not included in main_name.py)

      -copied_files have both - target's and source's - files the same content

3. and user will receive this **"information in the console"** and **"in the new file"** (path3) as well thanks **"mylogs.addHandler()"**
4. after all this action is the target folder deleted and replaced by copy of source.

    a. **"shutil.rmtree"** and **"shutil.copytree"** for comparison of content of files as well

    b. **"sync"** for comparison of title of files

5. and last but not least is the definition for periodical synchronization in minutes. **"schedule"**

## Disadvantage
As mentioned on web:
- None of the cases consider a comparison of the directories with sub-directory/ies within.
- The amount of files in the directories could be significant for running (and speed) as well.
- The datatypes can have an influence as e.g.

    _floats_ https://stackoverflow.com/questions/73326701/how-do-i-compare-two-text-files-from-different-folders or
    
    _white_ space https://stackoverflow.com/questions/8420143/valueerror-could-not-convert-string-to-float-id (only basic testing done)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/"Suggestion"`)
3. Commit your Changes (`git commit -m 'Add some "Suggestion"'`)
4. Push to the Branch (`git push origin feature/"Suggestion"`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Project Link: https://github.com/HelenaSekacova/cmp_line_arguments_directories

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* https://stackoverflow.com/
* https://www.geeksforgeeks.org/
* https://thispointer.com/
* https://realpython.com/python-command-line-arguments/#arguments
* https://pythonhowtoprogram.com/logging-in-python-3-how-to-output-logs-to-file-and-console/
* https://docs.python.org/3/library/filecmp.html 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LINKS -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[template]: https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md#readme-top
