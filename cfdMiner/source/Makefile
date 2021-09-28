CC = g++
CFLAGS = -O3 -Wall
OBJECTS = gcgrowth.o ScanDBMine.o parameters.o PatternSet.o FPtree.o Global.o data.o fsout.o

TARGET = GcEqClass

$(TARGET) : $(OBJECTS) Makefile
	$(CC) $(CFLAGS) $(OBJECTS) -o $(TARGET)

Global.o: Global.cpp Global.h
	$(CC) -c $(CFLAGS) Global.cpp
	
ScanDBMine.o : ScanDBMine.cpp ScanDBMine.h Global.h FPtree.h data.h inline_routine.h
	$(CC) -c $(CFLAGS) ScanDBMine.cpp

FPtree.o : FPtree.cpp FPtree.h inline_routine.h
	$(CC) -c $(CFLAGS) FPtree.cpp
	
data.o : data.cpp data.h
	$(CC) -c $(CFLAGS) data.cpp

fsout.o: fsout.cpp fsout.h Global.h parameters.h 
	$(CC) -c $(CFLAGS) fsout.cpp

parameters.o: parameters.cpp parameters.h Global.h
	$(CC) -c $(CFLAGS) parameters.cpp

PatternSet.o: PatternSet.cpp PatternSet.h FPtree.h Global.h inline_routine.h fsout.h
	$(CC) -c $(CFLAGS) PatternSet.cpp

gcgrowth.o : gcgrowth.cpp ScanDBMine.h FPtree.h data.h fsout.h Global.h parameters.h inline_routine.h
	$(CC) -c $(CFLAGS) gcgrowth.cpp


clean :
	rm *.o