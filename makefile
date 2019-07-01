ios:
	cd src/mplios;\
	rm -rf packages;\
	make clean;\
	make package;\
	dpkg -x packages/* new;\
	mv new/usr/bin/mplios ../../resources/mplios

mpl:
	cd src/mpl;\
	rm -rf packages;\
	make clean;\
	make package;\
	dpkg -x packages/* new;\
	mv new/Library/MobileSubstrate/DynamicLibraries/* ../../resources/;\
	rm -rf new

macos:
	cd src/mplmacos;\
	rm build/Release/mplmacos 2>/dev/null;\
	xcodebuild -target mplmacos -configuration Release;\
	rm ../../resources/mplmacos;\
	mv build/Release/mplmacos ../../resources/mplmacos

all: ios macos mpl 
