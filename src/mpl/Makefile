include ~/theos/makefiles/common.mk
# sudo xcode-select /Applications/xcode7.2.1.app
TWEAK_NAME = mpl
mpl_FILES = Tweak.xm
mpl_PRIVATE_FRAMEWORKS = AppSupport
include ~/theos/makefiles/tweak.mk

after-install::
	install.exec "killall -9 SpringBoard"
