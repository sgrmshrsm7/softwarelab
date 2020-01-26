CC=gcc
CFLAGS=-c

all: compile


compile: main.o func.o
	$(CC) $^ -o power

main.o: main.c
	$(CC) $(CFLAGS) main.c

func.o: func.c
	$(CC) $(CFLAGS) func.c

clean:
	rm -rf *o power
