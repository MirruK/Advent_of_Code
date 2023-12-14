.PHONY: test solve

test: galaxies.c
	gcc -g -Wpedantic -o galaxies galaxies.c
	cat test.txt | ./galaxies

solve: galaxies.c
	gcc -g -Wpedantic -o galaxies galaxies.c
	cat input.txt | ./galaxies