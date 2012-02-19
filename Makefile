all: rebuild

pwmt: pwmt.hs
	@ghc --make pwmt.hs

rebuild: pwmt
	@./pwmt rebuild
	$(MAKE) doxygen

build: pwmt
	@./pwmt build

preview: rebuild
	@./pwmt preview

clean:
	@./pwmt clean
	@rm -f pwmt pwmt.hi pwmt.o

doxygen:
	@./scripts/generate-doxygen.sh

sync:
	@rsync -ave ssh _site/* mlq@pwmt.org:/var/www/pwmt.org/site
