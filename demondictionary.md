<h1 align = center>Demon's Dictionary</h1>

<h3> brackets: </h3>

<b>()</b> - Parameters <br>
<b>[]</b> - Returns <br>
<b>{}</b> - Description
<h2>Demon Brain:</h2>
class:
1. arb
2. unit
3. formula
4. unit 


<h3>Functions.py</h3>
<ol>
<li><b>derites</b> ( driver, value ) &rarr; [ value ]<br>descriptiion:  converts driver values into derites using their corresponding pdex values <br>
2. <b>actionExtractor</b> ( aan ), [ act ] , converts a string into corresponding action class. <br>
3. <b>objectExtractor</b> ( word ), [ obj ] , converts a string into its corresponding object class.<br>
4. <b>tagMatch</b> ( act, obj ), [ list ], checks what are the tags which matches between action and object<br>
5. <b>actDriverState</b> ( dtm ), [ driverState ] , converts action class into driver state class<br>
6. <b>matrixToDs</b>( matrix ), [ ds ] , converts a list or matrix to driver state<br>
7. <b>objectCombine</b> ( aon ), [ obj, combined object ] , combines driver state, properties , describers (support function )<br>
8. <b>actionDs</b> ( act, obje ), [ driver ], returns action and objects' driver state<br>
9. <b>objectPreference</b> ( obds, obds_pm ), [ ds ] , multiplies the driverState with preference matrix<br>
10. <b>addDriverState</b> ( a ), [ ds ] , adds wo or more driver state<br>
11. <b>deritesDecision</b> ( decision ), [ derites ], adds all the derites of a class : decision<br> 
12. <b>makeDec</b> ( dec ), [ final decision ], makes decision from list of decisions<br>
13. <b>store</b> ( o, d = None, p = None , a = None ), [ NULL ] , stores a decision into memory file<br>
14. <b>chunkClassifier</b> ( pos ), [ chunk ] , returns which chunk a particular position belongs to<br>
15. <b>delete</b> ( simobj ), [ NULL ] , deletes a simulation object from simulation world file<br>
16. <b>tlo</b><br>
17. <b>excecute</b> ( input, instruction = None ), [ output ] , executes a task with given instruction<br>
<h3>LRU:</h3><br>
18. <b>arbStr</b>( aki ), [ asi ],converts arb to string }<br>
19. <b>storeArb</b>( data ), [ ] { stores arb data into memory }<br>
20. <b>strArb</b>( aki ), [ asi ], { converts a string to arb class}<br>
21. <b>strArbSup</b> { supporting function to stri_arb() }<br>
22. <b>isArb</b>( aki ) [ bool ] { checks if a given sting is a arb or a arb convertable }<br>
23. <b>communicate</b>(sen)<br>
24. <b>arbDisplay</b>(str) { displays a arb like a normal sentence }<br>
25. <b>retrive</b>( a, r, b) [ final_list ] { retrives a list from memory that matches the inputted arb }<br>
26. <b>memArbClear</b>() [ ] { clears the memory }<br>
27. <b>DefineRelation</b>( relation, sen ) { stores the relation definintion into memory }<br>
28. <b>InfoTranslate</b>( arb ) [ data ] { translates the given arb to the predefined data ` from the data used to define the relation }<br>
<h3>ARU</h3><br>
29. <b>findRoots</b>( x, y ), [ list ] , used to find roots when u give x and y<br>
30. <b>generate</b> ( signal, variable, lower_limit, upperlimit, sampling_rate = 10 ), [ x, y ] , generates a signal with a given signal<br> 
