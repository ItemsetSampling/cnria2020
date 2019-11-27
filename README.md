<h1>FPOF et malédiction de la longue traîne </h1>

                                      Under submission for CNRIA'20


This directory contains our additional materials for submission to the CNRIA'20 conference. We mainly have a folder named <b>CFPOF</b> containing the source code of our method and the datasets used during the experimental phase. You will see that Organisation and Person datasets are zipped because their sizes exceed the maximum allowed by Github during the loarding phase. If someone wants to launch the CFPOF algorithm with these databases, he or she will need to unzip them first.

The main syntax to run the CFPOF algorithm is bellow : 

  <i>\>cfpof.py <b>dataset:</b>\<the name of the dataset\>  <b>maxLength:</b>\<the maximum length constraint\> <b>sampleSize:</b>\<the number of patterns to draw\> <b>printCFPOF:</b>\<<b>1</b> if you want to print the values, <b>0</b> otherwise\></i>

<b>NB:</b> Python 3.7 was used during the implementation. 

<h2> Somme experiments with the <i>chess</i> dataset </h2>

The minimum information that CFPOF requires is the name of the dataset. If the others required values are not given, then it uses the default ones.

      >cfpof.py dataset:chess.num
      ===========================BEGIN===========================
      ===============Under submission for CNRIA'20===============
      CFPOF calculation ...
      Dataset :  chess.num
              No given maximum length constraint.
                      Maximum length : 3 by default.
              Preprocessing time (s) : 0.09375
              No given sample size.
                      Sample size : 1000 by default.
              CFPOF computational time (s) : 0.859375
      ============================END============================
  
  
  Note that, if the printCFPOF argument is set to 1 in order to output the CFPOF values of the transactions, then these values are not ordered here.<br>
  The following result with printCFPOF means that given the dataset D=chess and the sampled patterns, the transaction with an id equals to 37 has a cfpof equals to 0.6637168141592921. Formally :
  cfpof(t, D)=0.6637168141592921 where id(t)=37 and D=chess.
      
      >cfpof.py dataset:chess.num printCFPOF:1
      =======================================================
      CFPOF calculation ...
      Dataset :  chess.num
              No given maximum length constraint.
                      Maximum length : 3 by default.
              Preprocessing time (s) : 0.09375
              No given sample size.
                      Sample size : 1000 by default.
              CFPOF computational time (s) : 1.046875
      ===========================END==========================
      {37: 0.6637168141592921, 94: 0.6548672566371682, 105: 0.7610619469026548, ..., 19075: 0.46017699115044247, 23660: 0.36283185840707965}
      
      
      
Now we define our own values for the difference arguments required by CFPOF :
      
      >cfpof.py dataset:chess.num maxLength:2 sampleSize:10000 printCFPOF:0
      ===========================BEGIN===========================
      ===============Under submission for CNRIA'20===============
      CFPOF calculation ...
      Dataset :  chess.num
              Preprocessing time (s) : 0.125
              CFPOF computational time (s) : 7.21875
      ============================END============================
      
      
 
