include $(THEOS)/makefiles/common.mk
# sudo xcode-select /Applications/xcode7.2.1.app
TWEAK_NAME = 'Mouse Substrate'
mpl_FILES = Tweak.xm
mpl_PRIVATE_FRAMEWORKS = AppSupport
include $(THEOS_MAKE_PATH)/tweak.mk

after-install::
	install.exec "killall -9 SpringBoard"
