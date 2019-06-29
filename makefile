ios:
	cd src/mplios;\
	rm -rf packages;\
	make clean;\
	make package;\
	dpkg -x packages/* new;\
	mv new/usr/bin/mplios ../../resources/mplios

iospro:
	cd src/mpro;\
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

cydia-package:
	rm -rf .cydia-package
	# directory stucture
	mkdir .cydia-package
	mkdir .cydia-package/DEBIAN
	mkdir .cydia-package/usr
	mkdir .cydia-package/usr/local
	mkdir .cydia-package/usr/local/mouse
	mkdir .cydia-package/usr/local/bin
	echo "#!/bin/bash" >> .cydia-package/usr/local/bin/mouse
	echo "cd /usr/local/mouse" >> .cydia-package/usr/local/bin/mouse
	echo "python mouse.py" >> .cydia-package/usr/local/bin/mouse
	chmod +x .cydia-package/usr/local/bin/mouse
	# copy files
	cp mouse.py .cydia-package/usr/local/mouse
	cp -R modules .cydia-package/usr/local/mouse
	cp -R resources .cydia-package/usr/local/mouse
	# control file
	echo "Name: mouse" >> .cydia-package/DEBIAN/control
	echo "Package: com.lucasjackson.mouse" >> .cydia-package/DEBIAN/control
	echo "Version: 1.6" >> .cydia-package/DEBIAN/control
	echo "Description: iOS/macOS/Linux pentest tool" >> .cydia-package/DEBIAN/control
	echo "Architecture: iphoneos-arm" >> .cydia-package/DEBIAN/control
	echo "Author: Entynetproject <Ivan Nikolsky>" >> .cydia-package/DEBIAN/control
	echo "Maintainer: Entynetproject <Ivan Nikolsky>" >> .cydia-package/DEBIAN/control
	echo "Depends: python (>=2.7.8-1), com.lucasjackson.pysslfix (>=1.0)" >> .cydia-package/DEBIAN/control
	#postinst
	echo "#!/bin/bash" >> .cydia-package/DEBIAN/postinst
	echo "ldid -S /usr/bin/python" >> .cydia-package/DEBIAN/postinst
	chmod +x .cydia-package/DEBIAN/postinst
	dpkg -b .cydia-package mouse.deb

all: ios macos iospro cydia-package
