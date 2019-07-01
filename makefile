ios:
	cd src/mplios;\
	rm -rf packages;\
	make clean;\
	make package;\
	make -f Makefile --no-keep-going COLOR=1 --no-print-directory internal-tweak-all _THEOS_CURRENT_TYPE="tweak" THEOS_CURRENT_INSTANCE="mpl" _THEOS_CURRENT_OPERATION="all" THEOS_BUILD_DIR=".";\
	dpkg -x .theos/obj/debug/* new;\
	mv new/usr/bin/mplios ../../resources/mplios

mpl:
	cd src/mpl;\
	rm -rf packages;\
	make clean;\
	make package;\
	make -f Makefile --no-keep-going COLOR=1 --no-print-directory internal-tweak-all _THEOS_CURRENT_TYPE="tweak" THEOS_CURRENT_INSTANCE="mpl" _THEOS_CURRENT_OPERATION="all" THEOS_BUILD_DIR=".";\
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
