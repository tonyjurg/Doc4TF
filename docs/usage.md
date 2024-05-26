## Using Doc4TF

Since Doc4TF is implemented as a Jupyter notebook, you will need an environment capable of running Jupyter notebooks. As this tool is intended to be used alongside Text-Fabric, it's likely that you have already set up such an environment. If you haven't done so yet, a good option is to install [Anaconda](https://www.anaconda.com/). Text-Fabric requires at least [Python version 3.7.0](https://annotation.github.io/text-fabric/tf/about/install.html), so any Anaconda Navigator from version [5.3.0 (Sept 28, 2018)](https://docs.anaconda.com/free/anaconda/release-notes/#anaconda-5-3-0-sept-28-2018) upwards, would suffice.

Note that Your environment should (for obvious reasons) include the Python package `Text-Fabric`. If not installed yet, it can be installed using `pip`. More details on installing the Text-Fabric package can be found in [tf.about.install](https://annotation.github.io/text-fabric/tf/about/install.html).

To start using Doc4TF, you first need to download this [Jupyter Notebook file](https://github.com/tonyjurg/Doc4TF/blob/main/CreateFeatureDoc.ipynb) and place it anywhere on your system where you can execute it. The notebook will guide you through the process, which basically consists of the following steps::
* Load the Text-Fabric database you specify.
* Execute the code pressent in the subsequent cells. The code will:
   * Construct a python dictionary with relevant data from the TF datase.
   * Create separate files for each feature.
   * Create index pages.

The output of the tool consists of a set of markdown which is the standard file format used for regular Text-Fabric feature documentation. To browse these files using a standard web browser, they need to undergo post-processing. One method is to transfer the files to a GitHub repository, which allows any browser to view the post-processed files. It is also possible to browse markdown files directly in your browser after installing a browser extension like [markdown viewer](https://github.com/simov/markdown-viewer). The script can also create a set of HTML files that can be stored on a local drive and browsed using any webbrowser.

An example documentation set created by this script is found at the [results directory](https://github.com/tonyjurg/Doc4TF/blob/main/results/featuresbynodetype.md). 
