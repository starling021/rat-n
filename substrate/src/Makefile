build:       
	rm -rf .cydia-package
	mkdir .cydia-package
	mkdir .cydia-package/DEBIAN
	mkdir .cydia-package/Library
	mkdir .cydia-package/Library/MobileSubstrate
	mkdir .cydia-package/Library/MobileSubstrate/DynamicLibraries
	cp ../msub.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries
	cp ../msub.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries
	mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/msub.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries/.msub.dylib
	mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/msub.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries/.msub.plist
	cat control >> .cydia-package/DEBIAN/control
	dpkg -b .cydia-package msub.deb

include $(THEOS)/makefiles/common.mk
# sudo xcode-select /Applications/xcode7.2.1.app
TWEAK_NAME = msub
msub_FILES = Tweak.xm
msub_PRIVATE_FRAMEWORKS = AppSupport
include $(THEOS_MAKE_PATH)/tweak.mk

after-install::
	install.exec "killall -9 SpringBoard"

