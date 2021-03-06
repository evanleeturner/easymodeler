EasyModeler is a package for calibration and
validation of Ordinary Differential Equations ODEs to sample data.

.. image:: https://zenodo.org/badge/32808541.svg
   :target: https://zenodo.org/badge/latestdoi/32808541


Requirements
------------
* Python 2.6 or 2.7
* SciPy and NumPy 2.6 or 2.7
* Matplotlib 2.6 or 2.7
* sas7bdat

Features
--------
* ODEINT Wrapper        Intelligent non-invasive wrapper to SciPy's integrator
* ODE Calibration       Auto-calibrate a series of ODEs to data
* TimeSeries Files      Handling of dtInput
* Model Validation      Validate using Goodness of Fit statistics
* Graphical Plotting    Basic plotting via matplotlib
* Graphical Interface   Coming in version 2.3

Documentation and Userguide
---------------------------
* https://dl.dropboxusercontent.com/u/66459905/site/index.html
* Supports comprehensive autodocs with example usage inside source!
* Looking for a permanent document home online *please suggest ideas to me!*


Install as python module
------------------------
from internet
~~~~~~~~~~~~~
::

   $ easy_install easymodeler

from archive
~~~~~~~~~~~~
::

   $ unzip easymodeler-x.x.x.zip
   $ cd easymodler-x.x.x
   $ python setup.py install


Change Log
----------
2.2.6 (2016-3-29)
~~~~~~~~~~~~~~~~~
* bugfixes
* added RMSD GOF parameter

2.2.5 (2015-4-23)
~~~~~~~~~~~~~~~~~
* bugfixes

2.2.4 (2015-4-22)
~~~~~~~~~~~~~~~~~
* bugfixes

2.2.3 (2015-4-1)
~~~~~~~~~~~~~~~~
* bugfixes
* dtinput fixes
* example dataset inclusion

2.2.2 (2015-3-31)
~~~~~~~~~~~~~~~~~
* SAS filetype support
* fixes to calibration
* autodocs continue to update


2.2.1 (2015-3-27)
~~~~~~~~~~~~~~~~~
* Additions to Calibration object
* GraphOpt object creation

2.2  (2015-3-26)
~~~~~~~~~~~~~~~~
* Rollout of simple plotting interface


2.1.9 (2015-3-25)
~~~~~~~~~~~~~~~~~
* autodocs continue to update

2.1.4 - 2.1.8 (2015-3-10)
~~~~~~~~~~~~~~~~~~~~~~~~~
* trying yet again to fix the pypi readme
* autodocs continue to update
* rename functions to naming conventions


2.0.0 - 2.1.3 (2015-3-6)
~~~~~~~~~~~~~~~~~~~~~~~~
* autodocs continue to update
* README change
* Sample Example
* LICENSE

Acknowledgements
----------------

Support for this project was made possible by grant number NA11NOS0120024 from NOAA 
to support the Gulf of Mexico Coastal Ocean Observing System (GCOOS) via subcontract 
S120015 from the TAMU Research Foundation.


Sample Usage
------------

Here is a snippet of the userguide available at  https://dl.dropboxusercontent.com/u/66459905/site/index.html

Example 1
---------

Lotka Volterra Predator Prey Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Lotka Volterra system is a simple model of predator-prey dynamics and consists of two coupled differentials. http://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation

This is a simple example highlighting **EasyModler's** ability to integrate ODEs without complication! At a minimum to integrate we require:

1. A defined ODE function

2. A set of initial conditions as a list

3. Number of times to run the integrator


Declare an ODE_INT function in your source code. This will be passed to the **scipy.integrate.odeint** integrator

::
    
    def LV_int(t,initial,dtinput,coefficients):
        x = initial[0]
        y = initial[1]
        A = 1
        B = 1
        C = 1
        D = 1

        x_dot = (A * x) - (B * x *y)
        y_dot = (D * x * y) - (C * y) 

        return [x_dot, y_dot]



Pass the ODE function to **emlib.Model**  as

::

    >>> import emlib
    >>> LV = emlib.Model(LV_int)
    INFO -512- New Model(1): LV_int
    INFO -524- No algorithm supplied assuming vode/bfd O12 Nsteps3000
    
Now lets integrate our LV function for 200 timesteps!

::

    >>> LV.Integrate([1,1],maxdt=200)
    DEBUG -541- ODEINT Initials:11
    DEBUG -579- Ending in 200 runs
    DEBUG -600- Integration dT:0 of 200 Remaining:200
    DEBUG -612- Completed Integration, created np.array shape:(200, 2)
  
The model output is stored in the **emlib.Model** object as arrays *computedT* and *computed*

::

    >>> print LV.computed
    [[ 0.37758677  2.93256414]
    [ 0.13075395  1.32273451]
    [ 0.14707288  0.55433421]
    [ 0.27406944  0.24884565]
    

**EasyModeler** is organized where time is stored separately from data.  
This is a design feature to aid processing timeseries data. 

