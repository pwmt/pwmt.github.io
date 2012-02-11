all: rebuild

pwmt: pwmt.hs
	@ghc --make pwmt.hs

rebuild: pwmt
	@./pwmt rebuild

build: pwmt
	@./pwmt build

preview: rebuild
	@./pwmt preview

clean:
	@./pwmt clean
	@rm -f pwmt pwmt.hi pwmt.o
