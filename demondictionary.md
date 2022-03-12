#Demon's Dictionary
### brackets:
**()** - Parameters \
**[]** - Returns \
**{}** - Description
##Demon Brain:
class:
1. arb
2. unit
3. formula
4. unit
###Functions.py
1. **derites** ( driver, value ), [ value ], converts driver values into derites using their corresponding pdex values
2. **actionExtractor** ( aan ), [ act ] , converts a string into corresponding action class.
3. **objectExtractor** ( word ), [ obj ] , converts a string into its corresponding object class.
4. **tagMatch** ( act, obj ), [ list ], checks what are the tags which matches between action and object
5. **actDriverState** ( dtm ), [ driverState ] , converts action class into driver state class
6. **matrixToDs**( matrix ), [ ds ] , converts a list or matrix to driver state
7. **objectCombine** ( aon ), [ obj, combined object ] , combines driver state, properties , describers (support function )
8. **actionDs** ( act, obje ), [ driver ], returns action and objects' driver state
9. **objectPreference** ( obds, obds_pm ), [ ds ] , multiplies the driverState with preference matrix
10. **addDriverState** ( a ), [ ds ] , adds wo or more driver state
11. **deritesDecision** ( decision ), [ derites ], adds all the derites of a class : decision 
12. **makeDec** ( dec ), [ final decision ], makes decision from list of decisions
13. **store** ( o, d = None, p = None , a = None ), [ NULL ] , stores a decision into memory file
14. **chunkClassifier** ( pos ), [ chunk ] , returns which chunk a particular position belongs to
15. **delete** ( simobj ), [ NULL ] , deletes a simulation object from simulation world file
16. **tlo**
17. **excecute** ( input, instruction = None ), [ output ] , executes a task with given instruction
###LRU:
18. **arb_str**( aki ), [ asi ],converts arb to string }
19. **store_arb**( data ), [ ] { stores arb data into memory }
20. **str_arb**( aki ), [ asi ], { converts a string to arb class}
21. **str_arb_sup** { supporting function to stri_arb() }
22. **is_arb**( aki ) [ bool ] { checks if a given sting is a arb or a arb convertable }
23. **communicate**(sen)
24. **arbDisplay**(str) { displays a arb like a normal sentence }
25. **retrive**( a, r, b) [ final_list ] { retrives a list from memory that matches the inputted arb }
26. **memArbClear**() [ ] { clears the memory }
27. **DefineRelation**( relation, sen ) { stores the relation definintion into memory }
28. **InfoTranslate**( arb ) [ data ] { translates the given arb to the predefined data ` from the data used to define the relation }
###ARU
29. **find_roots**( x, y ), [ list ] , used to find roots when u give x and y
30. **generate** ( signal, variable, lower_limit, upperlimit, sampling_rate = 10 ), [ x, y ] , generates a signal with a given signal 
