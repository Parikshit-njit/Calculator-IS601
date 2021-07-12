# Calculator--IS601
<div>
  
![travis-ci](https://user-images.githubusercontent.com/81203429/124843974-26296180-df61-11eb-83b9-5031923a18c0.png)

  <hr><h3> Build Status </h3> <img src="https://travis-ci.com/Parikshit-njit/Calculator-IS601.svg?branch=main"></img>

</div>
<p align="justify">
  <h3>Description</h3>
  <hr>
  This project is part of <b>IS601</b> course. It is a calculator using Python that has automated unit tests. It performs operations such as addition, subtraction, multiplication, division, square root, square, mean, median, mode, random, variance and standard deviation. The unit tests file for specific operation contains 18 tests for addition, subtraction, multiplication, division, square root and square and 2 unit tests for each statistical operation. This project strictly follows the <b>SOLID</b> principle with a well-thought-out architecture. 
</p>

<div>
  <h3> Program Requirements </h3>
  <hr>
  <p align="justify">
    <ul>
      <li>Demonstrate inheritance by extending the calculator</li>
      <li>Demonstrate encapsulation by having the calculator have methods and a result property</li>
<li>Demonstrate abstraction by layering your code and using static methods.  Object methods should call static methods to perform the operation.</li>
      <li>Check values for being valid numbers and not strings</li>
      <li>Throw an exception for divide by zero </li>
      <li>Throw exception for empty list</li>
<li>Use random data for tests and be able to increase the number of calculations required i.e. be able to increase the list of numbers that the mean calculation is done on.  You can actually use built-in libraries or 3rd party libraries to check the calculations that you complete yourself.  i.e. you can use the standard deviation function from a stats library to compute the correct value for your list of random numbers and then use that to test that your own calculation is correct for that list.</li>
  </ul>
  </p>
</div>  

<hr>
<h3> Screenshot for successful build through Travis CI</h3>

![Screenshot 2021-07-11 at 11 22 44 PM](https://user-images.githubusercontent.com/81203429/125226355-f2bb3f80-e29e-11eb-9a28-ff33df7c136b.png)

<div>
  <h3> Configurations </h3>
  <hr>
  <p align="justify">
  There are two configurations for running this calculator:<br>
    <b>1. Main file:</b> To run the calculator for performing operations like addition, subtraction, division, multiplication, square, square root, etc. and statistical operations like mean, median, mode, standard deviation, variance, etc.<br>
    <b>2. Unit Tests:</b> The is run using docker file and the source code for this is in CalculatorTests.py<br>
  </p>
</div>  


